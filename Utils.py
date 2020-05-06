#!/usr/bin/env python

# functions currently not in use:
#    def add_EXAMPLE_DATA(self, x, y_1, y_2):
#    def delete_EXAMPLE_DATA(self, x):
#    def get_interpolated_EXAMPLE_VAR(self, x):
#    def get_EXAMPLE_VAR(self):
#    def gen_axis_graph(self, short_axis, full_axis):


import serial, sys, time, datetime, os, yaml, copy, numpy, json, cookies, re
import matplotlib.pyplot as plt

DEV_HOST_NAMES = ['b']
POLY_DEG = 2

class Utils(object):

    def __init__(self):
        self.init_successful = False
        self.abort_pending = False
        self.dev_env = False
        if os.popen("hostname").read().strip() in DEV_HOST_NAMES:
            self.dev_env = True
        self._init_status()
        self._init_EXAMPLE_DATA()
        try:
            self.users = yaml.load(open("users.yaml"))
        except:
            self.toLog("Could not read file 'users.yaml' - Please create this file using 'manage-users'.")
            self.toLog("    Aborting.")
            exit() 
        self.init_successful = True

    def _init_EXAMPLE_DATA(self):
        self.EXAMPLE_DATA = yaml.load(open("EXAMPLE_DATA.yaml"))

        X = []; Y_1 = []; Y_2 = [ ]
        for DATA in self.EXAMPLE_DATA:
            X.append(DATA["x"])
            Y_1.append(DATA["y_1"])
            Y_2.append(DATA["y_1"])

        x = numpy.array(X)
        y_1 = numpy.array(Y_1)
        y_2 = numpy.array(Y_2)

        POLY_DEG = 2 #degree of the polynomial fit
        self.polynomial_fit_coeff_y_1 = numpy.polyfit(x, y_1, POLY_DEG)
        self.polynomial_fit_coeff_y_2 = numpy.polyfit(x, y_2, POLY_DEG)

    def add_EXAMPLE_DATA(self, x, y_1, y_2):
        self.toLog("add_EXAMPLE_DATA: got request to add EXAMPLE at '"+ x +"'")
        self.toLog("add_EXAMPLE_DATA:     y_1:%s, y_2:%s:%s"%(y_1, y_2))
        tmpEXAMPLE_DATA = [ ]; EXAMPLE_DATA_added = False
        for DATA in self.EXAMPLE_DATA:
            if DATA["x"]<x:
                EXAMPLE_DATA_added = True
                tmpEXAMPLE_DATA.append({ "x":x, "y_1": y_1, "y_2": y_2})
            tmpEXAMPLE_DATA.append(DATA)
        if not EXAMPLE_DATA_added:
            tmpEXAMPLE_DATA.append({ "x":x, "y_1": y_1, "y_2": y_2})
        self.toLog("add_EXAMPLE_DATA: added x '"+ x +"'. Old file TARed.")            

    def delete_EXAMPLE_DATA(self, x):
        self.toLog("delete_EXAMPLE_DATA: got request to delete x at '"+ x +"'")
        tmpEXAMPLE_DATA = [ ]; EXAMPLE_DATA_deleted = False
        for DATA in self.EXAMPLE_DATA:
            if DATA["x"]==x:
                EXAMPLE_DATA_deleted = True
            else:
                tmpEXAMPLE_DATA.append(DATA)
        if EXAMPLE_DATA_deleted:
            self._set_EXAMPLE_DATA(tmpEXAMPLE_DATA)
            self.toLog("delete_EXAMPLE_DATA: deleted x '"+ x +"'. Old file TARed.")            
        else:
            self.toLog("delete_EXAMPLE_DATA: nothing deleted")
        return

    def _set_EXAMPLE_DATA(self, new_EXAMPLE_DATA):
        time_stamp = datetime.datetime.strftime(datetime.datetime.now(),"%d%b%Y_%H%M%S")
        res = os.popen("tar czf EXAMPLE_DATA.bu."+ time_stamp +".tar EXAMPLE_DATA.yaml").read()
        self.toLog("Result of tar operation: '"+ res +"'")
        self.EXAMPLE_DATA = new_EXAMPLE_DATA
        yaml.dump(self.EXAMPLE_DATA, open("EXAMPLE_DATA.yaml", 'w'))

    def _init_status(self):
        self.status = { }
        self.status["user_authenticated"] = False
        self.status["message"] = ""
        self.status["currently_executing"] = ""
        self.status["failure"] = False
        if self.dev_env:
            now = datetime.datetime.now()
            seconds = "%02d" % now.second
            x = "1."+seconds
            y_1 = "20." + seconds
            y_2 = "300." + seconds
        else:
            x = y_1 = y_2 = 0
        self.set_EXAMPLE_VAR(x, y_1, y_2)


    def save_users_database(self):
        yaml.dump(self.users, open("users.yaml", 'w'))

    def genrate_cookie(self, user, hashed_pwd):
        cookie_data = json.dumps( { "user": user, "hashed_pwd": hashed_pwd } )
        lease_in_seconds = 30 * 24 * 60 * 60  # 30 days in seconds
        end = time.gmtime(time.time() + lease_in_seconds)
        expires = time.strftime("%a, %d-%b-%Y %T GMT", end)
        cookie = cookies.Cookie.from_dict({'name': 'account_info', 'value': cookie_data, 'expires': expires})
        return cookie.render_response()            
   
    def parse_cookie(self, raw_cookie):
        raw_cookie = str(raw_cookie)
        self.toLog("parse_cookie: raw_cookie is '"+ raw_cookie +"'")
        user = ""; hashed_pwd = ""
        try:
        #for i in [1]:
            cookie_data = cookies.Cookies.from_request(raw_cookie)["account_info"]
            cookie_data = cookie_data.to_dict()
            if cookie_data["name"]=="account_info":
                cookie_data = json.loads( cookie_data["value"] )
                user = cookie_data["user"]
                hashed_pwd = cookie_data["hashed_pwd"]
        except:
            self.toLog("parse_cookie: Failed parsing cookie" )
        self.toLog("parse_cookie: Got from cookie: user: '"+ user +"', hashed_pwd: '"+ hashed_pwd +"'" )
        return user, hashed_pwd
    

    def toLog(self, msg):
       timeStamp = datetime.datetime.strftime(datetime.datetime.now(), "%d %H:%M.%S ")
       open("PROJECT.log", 'a').write(timeStamp + msg +"\n")
       if len(msg)>77:
           print msg[:77] +"..."
       else:
           print msg

    def get_status(self):
        if not self.status["user_authenticated"]:
           s = { }
           s["EXAMPLE_VAR_float"] = {"x": float(0), "y_1": float(0), "y_2": float(0)}
           s["EXAMPLE_VAR_str"] = "000.00 000.00 000.00"
           s["message"] = "NOT AUTHENTICATED. Click on 'PROJECT' at the top menu and login"
           s["currently_executing"] = ""
           s["failure"] = True
           s["user_authenticated"] = False
           return s 
        status = copy.deepcopy(self.status)
        return status

    def set_status_starting(self, currently_executing):
        self.toLog("Execution starting. Currently executing: "+ currently_executing)  
        self.status["message"] = ""
        self.status["currently_executing"] = currently_executing
        self.abort_pending = False
        self.status["failure"] = False
        return self.status

    def set_status_done(self, success, msg):
        self.toLog("Execution done")  
        self.status["failure"] = not success
        if not success:
           self.toLog("     Function failed")
        if msg:
           self.toLog("     Functin reported: "+ msg)    
        self.status["message"] = msg
        self.status["currently_executing"] = ""
        self.abort_pending = False
        return self.status

    def set_status_to_failed(self, msg):
        self.status["failure"] = True
        self.toLog("     FAILURE (and setting status to failed)")
        self.status["message"] = msg
   
    def _print_same_line(self, msg):
        sys.stdout.write(msg.ljust(70) + '\r')
        sys.stdout.flush()

    def _exe(self, cmd):
        #Example of simulated action
        if self.dev_env:  
            ans = ""
            if cmd=="get_EXAMPLE_DATA":
                ans = self.status["EXAMLE_VAR_str"]
            return ans
        prompt_seen, rep = self.GET_SOME_ANSWERS(cmd)
        if not prompt_seen:
            self.toLog("Expected prompt not present")
            self.toLog( "Got: "+ str(rep) )
            exit()
        return rep[0]

     
    ################## Top level functions #################################

    def get_interpolated_EXAMPLE_VAR(self, x):
        y_1 = round(numpy.polyval(self.polynomial_fit_coeff_y_1, x), POLY_DEG)
        y_2 = round(numpy.polyval(self.polynomial_fit_coeff_y_2, x), POLY_DEG)
        return {"y_1": y_1, "y_2": y_2 }

    def set_EXAMPLE_VAR(self, x, y_1, y_2):
        cmd = "set example var "+ x +" "+  y_1 +" "+ y_2
        self.toLog("set_EXAMPLE_VAR: about to send command: "+cmd)
        self._exe(cmd)
        self.set_status_done(True, "")

    def zero_EXAMPLE_VAR(self):
        cmd = "set example var 0 0 0"
        self.toLog("zero_EXAMPLE_VAR: about to send command: "+cmd)
        self._exe(cmd)
        self.set_status_done(True, "")

    def get_EXAMPLE_VAR(self):
        # do something_useful
        return self.status["EXAMPLE_VAR"]

    def gen_axis_graph(self, short_axis, full_axis):
        def _get_x_y(all_EXAMPLE_INDEX_ITMEs, x_key, y_key):
            x=[]
            y=[]
            EXAMPLE_INDEX_ITME_keys = all_EXAMPLE_INDEX_ITMEs.keys(); EXAMPLE_INDEX_ITME_keys.sort()
            for EXAMPLE_INDEX_ITME_key in EXAMPLE_INDEX_ITME_keys:
                EXAMPLE_INDEX_ITME = all_EXAMPLE_INDEX_ITMEs[EXAMPLE_INDEX_ITME_key]
                if x_key in EXAMPLE_INDEX_ITME.keys() and y_key in EXAMPLE_INDEX_ITME.keys():
                    if EXAMPLE_INDEX_ITME[x_key]!='' and EXAMPLE_INDEX_ITME[y_key]!='':
                        x.append(float(EXAMPLE_INDEX_ITME[x_key]))
                        y.append(float(EXAMPLE_INDEX_ITME[y_key]))
            return (x,y)

        (x1,y1) = _get_x_y(self.EXAMPLE_DATA, "x","y_1")
        (x2,y2) = _get_x_y(self.EXAMPLE_DATA, "x","y_2")

        plt.plot(x1,y1,x2,y2)

        plt.title('x Vs EXAMPLE_DATA')
        plt.xlabel('x')
        plt.ylabel('y_1 y_2')

        plt.savefig("static_files/example_data.png")



if __name__=="__main__":

    u = Utils()

    if not u.init_successful:
        print "Failed initing the Utils class"
        print "Aborting"
        exit()

    u.toLog( "Intrpulated var:"+ str(u.get_interpolated_EXAMPLE_VAR(13)) )
    exit()

    u.set_EXAMPLE_VAR(1,2,3)

    u.toLog("EXAMPLE VAR:", u.get_EXAMPLE_VAR())
