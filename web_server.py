import Utils, time, cgi, web_pages, json, threading, hashlib

u = Utils.Utils()

seconds_between_updates = "2"
if u.dev_env: seconds_between_updates = "20"


def application(env, start_response):

    ########################## Preprations ########################## 
    if not u.init_successful:
        start_response('200 OK', [('Content-Type','text/html')])
        return "<h1>Failed in initiing class Utils - Please correct and restart server</h1>"

    # parse params
    path = env['PATH_INFO'][1:].split("?")[0]
    u.toLog("<-- "+str(path))
    params = { }
    p = cgi.parse_qs(env['QUERY_STRING'], True)
    if p.keys():
        u.toLog("<--(params) "+str(p))
        for key in p.keys():
            params[key] = p[key][0]

    postData = { }
    if env['REQUEST_METHOD'] == 'POST':
        post_env = env.copy()
        post_env['QUERY_STRING'] = ''
        postData = cgi.FieldStorage( fp=env['wsgi.input'], environ=post_env).value
        if len(postData):
           u.toLog("<--(post data) "+str(postData))

    ########################## handle user authentication ########################## 
    raw_cookie = ""
    if "HTTP_COOKIE" in env.keys():
        raw_cookie =  env["HTTP_COOKIE"]
    user_from_cookie, hashed_pwd_from_cookie = u.parse_cookie(raw_cookie)
    client_ip = str(env["REMOTE_ADDR"])
 
    u.status["user_authenticated"] = False
    # Try to authenticate by login
    if path=="signin.html":
        client_ip = str(env["REMOTE_ADDR"])
        u.toLog("Attempt to sign in from IP '"+ client_ip +"'")
        user = None
        if "user" in params.keys():
            user = params["user"]
            u.toLog("User '"+ user +"' attmpted login")
        hashed_pwd = None
        if "pwd" in params.keys():
            pwd = params["pwd"]
            hashed_pwd = hashlib.sha256(pwd).hexdigest()
            u.toLog("Hashed-pwd from user is '"+ hashed_pwd +"'")

        if user in u.users.keys():
            u.toLog("User '"+ user +"' exists in users file.")
            if hashed_pwd == u.users[user]["hashed_pwd"]:
                u.toLog("User '"+ user +"' is authonticated by submiting matching user and pwd.")
                u.status["user_authenticated"] = True
        if u.status["user_authenticated"]:
            if client_ip != u.users[user]["ip"]:
                u.toLog("    Modifient user database to reflect current IP")
                u.users[user]["ip"] = client_ip
                u.save_users_database()
            u.toLog("    Sending cookie to user and redirecting")
            u.set_status_starting("Login")    # To clear 'not authenticated from status
            u.set_status_done(True, "")
            cookie = u.genrate_cookie(user, hashed_pwd)
            headers = [ ]
            headers.append( ('Set-Cookie', cookie ) )
            headers.append( ('Location','EXAMPLE_PAGE1.html') )
            start_response('302 Moved Temporarily', headers)
            return ""

    # Try to authenticate by cookie
    if not u.status["user_authenticated"]:
        if user_from_cookie in u.users.keys():
            u.toLog("Cookie: User '"+ user_from_cookie +"' exists in users file.")
            if hashed_pwd_from_cookie == u.users[user_from_cookie]["hashed_pwd"]:
                u.toLog("     Cookie: pwds match.")
                if client_ip == u.users[user_from_cookie]["ip"]:
                    u.toLog("User '"+ user_from_cookie +"' is authonticated from client-cookie.")
                    u.status["user_authenticated"] = True
                else:
                    u.toLog("User '"+ user_from_cookie +"' is NOT authonticated, because stored IP and actual IP do not match")
                    u.toLog("     Cookie: pwd in file  :"+ u.users[user_from_cookie]["hashed_pwd"])
                    u.toLog("     Cookie: pwd in cookie:"+ hashed_pwd_from_cookie)
    # "getStatus" are honored even if we are not authenticated, so we can communicated to the user the need to auththenticate
    if path=="getStatus":
        start_response('200 OK', [('Content-Type','application/json')])
        return json.dumps( u.get_status() )


    # If we are here, we are not authenticated (=not by cookie and not by submiting user/pwd)
    if not u.status["user_authenticated"]:
        u.toLog("User is not authenticated - will get the login page")
        u.set_status_to_failed("You are not authenticated - please login")
        start_response('200 OK', [('Content-Type','text/html')])
        page  = web_pages.gen_page_start("EXAMPLE TITLE")
        page += web_pages.gen_signin_page()
        page += web_pages.gen_page_end()
        return str(page)

    ########################## Information requests ########################## 

    if path=="getEXAMPLEVAR":
        start_response('200 OK', [('Content-Type','application/json')])
        return json.dumps( u.EXAMPLE_VAR )

    ########################## Actions ########################## 

    if path=="setEXAMPLEVAR":
        start_response('200 OK', [('Content-Type','application/json')])
        if u.status["currently_executing"]:
            return json.dumps( {"success": False, "message": "System is busy - please try later"} )
        u.set_status_starting("set EXAMPLE VAR")
        val1 = params["val1"]
        try:
            val = int(val)
        except:
            return json.dumps( {"success": False, "message": "Unexpected value at the val1 param"} )
        val2 = params["val2"]
        try:
            val = int(val)
        except:
            return json.dumps( {"success": False, "message": "Unexpected value at the val2 param"} )

        #Long operation, so we span a new thread
        thread = threading.Thread( target=u.set_EXAMPLE_VAR, args=(val1, val2) )
        thread.start()

        return json.dumps( {"success": True, "message": ""} )

    if path=="zero_EXAMPLE_VAR":
        start_response('200 OK', [('Content-Type','application/json')])
        u.zero_EXAMPLE_VAR()
        return json.dumps( {"success": True, "message": ""} )

    if path=="abort":
        u.abort_pending = True
        u.toLog("Abort requested by client")
        return json.dumps( {"success": True, "message": ""} )

    ########################## User Interface ########################## 
    start_response('200 OK', [('Content-Type','text/html')])
    page  = web_pages.gen_page_start("EXAMPLE TITLE")
    if   path=="EXAMPLE_PAGE1.html":
        page += web_pages.gen_EXAMPLE_PAGE1_page(seconds_between_updates)
    elif path=="EXAMPLE_PAGE2.html":
        page += web_pages.gen_EXAMPLE_PAGE2_page(seconds_between_updates)
    else:
        page += web_pages.gen_EXAMPLE_DEFAULT_PAGE_page(seconds_between_updates)
    page += web_pages.gen_page_end()
    return str(page)
