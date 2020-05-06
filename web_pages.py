import yaml
############################ Genrate page parts #########################################
def gen_page_start(title):
   return '''
<!DOCTYPE html>
<html lang=en>
<head>
  <meta charset=utf-8>
  <meta name=viewport content="width=device-width,initial-scale=1">
  <meta http-equiv="expires" content="1" />
  <meta http-equiv="Pragma" content="no-cache">
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <title>'''+ title +'''</title>
  <link type="text/css" rel="stylesheet" href="bootstrap.css" />
  <link type="text/css" rel="stylesheet" href="bootstrap-vue.css" />
  <script src="vue.js"></script>
  <script src="bootstrap-vue.js"></script>
</head>
<body class="bg-light">
'''
def _gen_menu_html(site_name):
    return '''\
    <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
      <a class="navbar-brand" href="EXAMPLE_DEFAULT_PAGE.html">'''+ site_name +'''</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <li v-bind:class="{'nav-item': true, 'active': isMenuItemActive()}">
            <a class="nav-link" active href="EXAMPLE_PAGE1.html">Choose PAGE1</a>
          </li>
          <li v-bind:class="{'nav-item': true, 'active': isMenuItemActive()}">
            <a class="nav-link" href="EXAMPLE_PAGE2.html">Choose PAGE2<span class="sr-only">(current)</span></a>
          </li>
          <li v-bind:class="{'nav-item': true, 'active': isMenuItemActive()}">
            <a class="nav-link" active href="EXAMPLE_PAGE3.html">Choose PAGE3</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="help.html">Help</a>
          </li>
        </ul>
        <!--         
        <form class="form-inline mt-2 mt-md-0">
          <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
        -->
      </div>
    </nav>

'''

def gen_page_end():
    return '''
</body>
</html>
'''

def _gen_login_html():
    return '''
<div>

  <b-modal id="bv-modal-example" hide-footer>
               <form class="form-signin" method="get" action="signin.html">
                <h2 class="form-signin-heading">Please sign in</h2>
                <label for="inputUser" class="sr-only">User</label>
                <input type="text" name="user" id="inputUser" class="form-control" placeholder="User" required autofocus>          <label for="inputPassword" class="sr-only">Password</label>
                <input type="password" id="inputPassword" name="pwd" class="form-control" placeholder="Password" required>
                <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
              </form>
  </b-modal>
</div>
'''
def _gen_status_html():
    return '''
      <br>
      <div class="my-3 p-3 bg-white rounded box-shadow">
        <div class="alert alert-info" role="alert" v-if="!(status['currently_executing']=='')">
          Currently running: {{status["currently_executing"]}}
        </div>
        <div class="alert alert-danger" role="alert" v-else-if="status['failure']">
          Operation Failed: {{JSON.stringify(status["message"])}}
        </div>
        <div class="alert alert-success" role="alert" v-else>
          Operation completed successfully
        </div>
        <h4> Current EXAMPLE_INDEX_VAR: 
          <strong>
            {{ EXAMPLE_INDEX_VAR.EAXMAPLE_VAR1+" "+ EXAMPLE_INDEX_VAR.EAXMAPLE_SUBVAR_B+" "+ EXAMPLE_INDEX_VAR.EAXMAPLE_SUBVAR_C }}
          </strong> 
        </h4>
        <!--
        <p> 
          message: {{JSON.stringify(status["message"])}}<br>
          Currently executing: {{status["currently_executing"]}}<br>
          Is fail: {{JSON.stringify(status["failure"])}}<br>
          Status: {{JSON.stringify(status)}}<br>
          ---> 
        </p>
      </div>
'''

def _gen_status_variable():
    return """\
          status: { currently_executing: "Loading", user_authenticated: false },
"""
def _gen_EXAMPLE_LIST_related_methods():
    return '''
          addNewEXAMPLEListItem: function () {
            var xhr = new XMLHttpRequest()
            var self = this
            console.log( "deleteEXAMPLEListItem: 1")
            var args  = 'EXAMPLE_INDEX_VAR='+this.new_EXAMPLE_list_item_INDEX_VAR
                args += '&EAXMAPLE_VAR1='+this.EXAMPLE_INDEX_VAR["EAXMAPLE_VAR1"]
                args += '&EAXMAPLE_VAR2='+this.EXAMPLE_INDEX_VAR["EAXMAPLE_VAR2"]
                args += '&EAXMAPLE_VAR3='+this.EXAMPLE_INDEX_VAR["EAXMAPLE_VAR3"]
            xhr.open('GET', "addEXAMPLEListItem?"+args)
            xhr.onload = function () {
              self.EXAMPLE_list_items = JSON.parse(xhr.responseText)
              console.log( "addNewEXAMPLEListItem: Got EXAMPLE Items: "+JSON.stringify(self.EXAMPLE_list_items) )
            }
            console.log( 'addNewEXAMPLEListItem: Sending request to add EXAMPLE_INDEX_ITME '+this.new_EXAMPLE_list_item_INDEX )
            xhr.send()
          },
          deleteEXAMPLEListItem: function (EXAMPLE_INDEX_VAR) {
            var xhr = new XMLHttpRequest()
            var self = this
            console.log( "deleteEXAMPLEListItem: 1")
            xhr.open('GET', "deleteEXAMPLEListItem?EXAMPLE_INDEX_VAR='"+EXAMPLE_INDEX_VAR+"'")
            xhr.onload = function () {
              self.EXAMPLE_list_items = JSON.parse(xhr.responseText)
              console.log( "deleteEXAMPLEListItem: Got EXAMPLE items: "+JSON.stringify(self.EXAMPLE_list_items) )
            }
            console.log( 'deleteEXAMPLEListItem: Sending request to del EXAMPLE_INDEX_ITME '+EXAMPLE_INDEX_VAR )
            xhr.send()
          },
          fetchEXAMPLEListItems: function () {
            var xhr = new XMLHttpRequest()
            var self = this
            xhr.open('GET', "getEXAMPLEListItems")
            xhr.onload = function () {
              self.EXAMPLE_list_items = JSON.parse(xhr.responseText)
              console.log( "fetchEXAMPLEListItems: Got EXAMPLE items: "+JSON.stringify(self.EXAMPLE_INDEX_VAR) )
            }
            console.log( 'fetchEXAMPLEListItems: Sending request' )
            xhr.send()
          },
'''
def _gen_abort_and_status_related_methods():
    return '''
          abortCurrentOperation: function () {
            var xhr = new XMLHttpRequest()
            var self = this
            xhr.open('GET', "abort")
            console.log( 'abortCurrentOperation: Sending request' )
            xhr.send()
          },
          fetchEXAMPLE_INDEX_VAR: function () {
            var xhr = new XMLHttpRequest()
            var self = this
            xhr.open('GET', "getEXAMPLE_INDEX_VAR")
            xhr.onload = function () {
              self.EXAMPLE_INDEX_VAR = JSON.parse(xhr.responseText)
              self.last_operation_result = JSON.parse(xhr.responseText)
              console.log( "fetchEXAMPLE_INDEX_VAR: Got EXAMPLE_INDEX_VAR: "+JSON.stringify(self.EXAMPLE_INDEX_VAR) )
            }
            console.log( 'fetchEXAMPLE_INDEX_VAR: Sending request' )
            xhr.send()
            self.last_operation_result = { 'success': '...', 'message': 'fetchEXAMPLE_INDEX_VAR ongoing' } 
          },
          fetchStatus: function () {
            var xhr = new XMLHttpRequest()
            var self = this
            xhr.open('GET', "getStatus")
            xhr.onload = function () {
              self.status = JSON.parse(xhr.responseText)
              self.EXAMPLE_INDEX_VAR = JSON.parse(xhr.responseText).EXAMPLE_INDEX_VAR_float
              console.log( "fetchStatus: Got status: "+JSON.stringify(self.status) )
            }
            console.log( 'fetchStatus: Sending request' )
            xhr.send()
            self.last_operation_result = { 'success': '...', 'message': 'fetchStatus ongoing' } 
          },
          isMenuItemActive: function () {
            return this.status['user_authenticated'];
          },

'''

def _gen_abortButton():
    return '''
      <b-button 
        class="mt-3" 
        v-on:click="abortCurrentOperation()" 
        variant="danger" :disabled="status['currently_executing']==''">
        Abort Current Operation
      </b-button>
'''

def _gen_canvas_html():
    return '''
      <div>
        <canvas ref="EXAMPLE_INDEX_ITMEs_canvas" 
          :width="(EXAMPLE_var1_end - EXAMPLE_var1_start)*canvas_magnification" 
          :height="(EXAMPLE_var2_end-EXAMPLE_var2_start)*canvas_magnification">
        </canvas>
      </div>
      <div>
        <canvas ref="EXAMPLE_canvas_hidden" style="display:none;" 
          :width="(EXAMPLE_var1_end - EXAMPLE_var1_start)*canvas_magnification" 
          :height="(EXAMPLE_var2_end-EXAMPLE_var2_start)*canvas_magnification">
        </canvas>
      </div>
'''

def _gen_canvas_data():
    return '''\
          EXAMPLE_var1_start: 99,
          EXAMPLE_var1_end: 261,
          EXAMPLE_var2_start: 5,
          EXAMPLE_var2_end: 55,
          canvas_magnification: 6,
          canvas: null,
          canvas_hidden: null,
          ctx: null,
          ctx_hidden: null,
'''

def _gen_canvas_js():
    # Add to the app js script:
    #   mounted: function (){
    #     this.setup_canvas();
    #   },
    return '''
          setup_canvas: function () {
            console.log("setup_canvas: starting");
            this.canvas = this.$refs.EXAMPLE_INDEX_ITMEs_canvas;
            this.ctx = this.canvas.getContext("2d");
            this.draw_rulers_background();
            for (EXAMPLE_INDEX_ITME of this.EXAMPLE_list_items) {
              this.draw_EXAMPLE_INDEX_ITME(EXAMPLE_INDEX_ITME.EXAMPLE_VAR1, EXAMPLE_INDEX_ITME.EXAMPLE_VAR3, EXAMPLE_INDEX_ITME.EXAMPLE_INDEX_VAR)
            };
            this.canvas_hidden = this.$refs.EXAMPLE_canvas_hidden;
            this.ctx_hidden = this.canvas_hidden.getContext("2d");
            this.ctx_hidden.drawImage(this.canvas, 0, 0)
          },
          draw_EXAMPLE_INDEX_ITME: function (EXAMPLE_VAR1, EXAMPLE_VAR3, EXAMPLE_INDEX_VAR) {
            x = this.EXAMPLE_var1_to_x(this.canvas, EXAMPLE_VAR1);
            y = this.EXAMPLE_var2_to_y(this.canvas, EXAMPLE_VAR3)-70;
            r = 8

            this.ctx.strokeStyle = "#000000";
            this.ctx.font = "14px Arial";
            text_y = (y*2)-330;
            if (EXAMPLE_INDEX_VAR=="30.5E") text_y -= 30;
            for (var i = 0; i < EXAMPLE_INDEX_VAR.length; i++) {
              this.ctx.strokeText(EXAMPLE_INDEX_VAR.charAt(i), x - 6 + (i*12), y + 30 + (i*10) ); 
            };
                
            // this.ctx.strokeText(EXAMPLE_INDEX_VAR, x-25, text_y );


            this.ctx.strokeStyle = "#0000FF";
            this.ctx.beginPath();
            this.ctx.moveTo(x-r, y-r);
            this.ctx.lineTo(x+r, y-r);
            this.ctx.lineTo(x+r, y+r);
            this.ctx.lineTo(x-r, y+r);
            this.ctx.lineTo(x-r, y-r);
            this.ctx.stroke();
          },
          draw_EXAMPLE: function (EXAMPLE_VAR1, EXAMPLE_VAR3) {
            this.ctx.drawImage(this.canvas_hidden, 0, 0)
            x = this.EXAMPLE_var1_to_x(this.canvas, EXAMPLE_VAR1);
            y = this.EXAMPLE_var2_to_y(this.canvas, EXAMPLE_VAR3) -70;
            this.ctx.fillStyle = "#FF0000";

            <!--
            this.ctx.globalCompositeOperation = 'destination-out'
            this.ctx.beginPath();
            this.ctx.arc(this.prev_x,this.prev_y,4,0,2*Math.PI);
            this.ctx.stroke();
            this.ctx.fill();
            this.prev_x = x;
            this.prev_y = y;

            this.ctx.globalCompositeOperation = 'source-over'
            -->
            this.ctx.beginPath();
            this.ctx.arc(x,y,4,0,2*Math.PI);
            this.ctx.stroke();
            this.ctx.fill();
          },
          EXAMPLE_var1_to_x: function (canvas, EXAMPLE_VAR1) {
            x = (EXAMPLE_VAR1 - this.EXAMPLE_var1_start) * this.canvas_magnification;
            return x;
          },
          EXAMPLE_var2_to_y: function (canvas, EXAMPLE_VAR3) {
            y = (EXAMPLE_VAR3 - this.EXAMPLE_var2_start) * this.canvas_magnification;
            return y;
          },
          draw_rulers_background: function () {
            this.ctx.fillStyle = "#f0f1f2";
            this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
            this.ctx.beginPath();
            for(var i=0;i<this.canvas.width;i+=10){
              var y=(i/100==parseInt(i/100))?0:10;
              this.ctx.moveTo(i+15,y);
              this.ctx.lineTo(i+15,15);
              var x=(i/100==parseInt(i/100))?0:10;
              this.ctx.moveTo(x,i+15);
              this.ctx.lineTo(15,i+15);
            }
            this.ctx.stroke()
          },
'''
def _gen_EXAMPLEACTION_btnGroup(EXAMPLE_SUBVAR, variant):
    btnGroup = '''\
      <div class="mt-3">
        <b-button-group>
          <h4 style="width:117px;">{{'::EXAMPLE_SUBVAR::'.charAt(0).toUpperCase()  + '::EXAMPLE_SUBVAR::'.slice(1)}}</h4>
          <b-button pill class="mr-1" v-on:click="doEXAMPLEACTION('::EXAMPLE_SUBVAR::', 'minus', '10')" 
                    variant="::variant::" :disabled="!(status['currently_executing']=='')">- 1 S</b-button>
          <b-button pill class="mr-1" v-on:click="doEXAMPLEACTION('::EXAMPLE_SUBVAR::', 'minus', '1')" 
                    variant="::variant::" :disabled="!(status['currently_executing']=='')">- 0.1 S</b-button>
          <b-button pill class="mr-1" v-on:click="doEXAMPLEACTION('::EXAMPLE_SUBVAR::', 'plus', '1')" 
                    variant="::variant::" :disabled="!(status['currently_executing']=='')">+ 0.1 S</b-button>
          <b-button pill class="mr-3" v-on:click="doEXAMPLEACTION('::EXAMPLE_SUBVAR::', 'plus', '10')" 
                    variant="::variant::" :disabled="!(status['currently_executing']=='')">+ 1 S</b-button>
          <b-btn variant="::variant::" v-on:click="::EXAMPLE_SUBVAR::_candidate=getCurrentEXAMPLEVALUE('::EXAMPLE_SUBVAR::')">Get</b-btn>
          <div>
            <b-form-input v-model="::EXAMPLE_SUBVAR::_candidate" style="width:100px;">
            </b-form-input>
          </div>
          <b-btn v-on:click="moveSingleEXAMPLESUBVAR('::EXAMPLE_SUBVAR::', ::EXAMPLE_SUBVAR::_candidate)" 
                 variant="::variant::" :disabled="!(status['currently_executing']=='')">Move EXAMPLE_SUBVAR</b-btn>
          <h4 class="ml-2">Current value: {{getCurrentEXAMPLEVALUE('::EXAMPLE_SUBVAR::')}}</h4>
        </b-button-group>
      </div>
'''
    return btnGroup.replace("::EXAMPLE_SUBVAR::", EXAMPLE_SUBVAR).replace("::variant::", variant)

############################ Genrate full pages #########################################


def gen_signin_page():
    return '''
  <div id="firstPageApp">
    <b-container>
'''+ _gen_menu_html("EXAMPLE SITE NAME")+'''\
      <b-jumbotron header="EXAMPLE MAIN HEADER OF THIS SITE" lead="EXAMPLE additional info">
        <div class="container-fluid">
          <div class="row">
            <div class="col-4">
              <img src="example_picture.jpg" class="img-fluid" style="max-width: 80%;">
            </div>
            <div class="col-2">    </div>
            <div class="col-4" v-if="status['user_authenticated']">
              <h2>You are signed in</h2>
            </div>
            <div class="col-4" v-else>
              <form class="form-signin" method="get" action="signin.html">
                <h2 class="form-signin-heading">Please sign in</h2>
                <label for="inputUser" class="sr-only">User</label>
                <input type="text" name="user" id="inputUser" class="form-control" placeholder="User" required autofocus>          <label for="inputPassword" class="sr-only">Password</label>
                <input type="password" id="inputPassword" name="pwd" class="form-control" placeholder="Password" required>
                <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
              </form>
            </div>
            <div class="col-2">    </div>
          </div>
        </div>
      </b-jumbotron>
    </b-container>
  </div>



  <script>
    window.app = new Vue({
      el: '#firstPageApp',
      data: {
''' + _gen_status_variable() + '''\
      },
      created: function () {
        this.fetchStatus(); 
      },
      methods: {
''' + _gen_abort_and_status_related_methods() + '''
      }
  })
   </script>
'''

def gen_EXAMPLE_DEFAULT_PAGE_page(seconds_between_updates):
    vue_app = '''
  <div id="EXAMPLE_VAR_App">
    <b-container>
'''+ _gen_menu_html("EXAMPLE SITE NAME")+'''\
      </------make EXAMPLE ITEM active------/->
      <div class="mt-3 ">
        <h4>Move to EXAMPLE_INDEX_ITME:</h4>
        <b-button-group v-for="EXAMPLE_list_item in EXAMPLE_list_items">
          <div class="col-2">
            <b-button v-on:click="moveToEXAMPLE_INDEX_ITME(EXAMPLE_list_item.EXAMPLE_INDEX_VAR)" variant="primary"  
              v-b-tooltip.hover v-bind:title="EXAMPLE_list_item.EXAMPLE_VAR1+' '+EXAMPLE_list_item.EXAMPLE_INDEX_VAR+' '+EXAMPLE_list_item.EXAMPLE_VAR3" class="mb-3"
              :disabled="!(status['currently_executing']=='')">
              {{EXAMPLE_list_item.EXAMPLE_INDEX_VAR}}
            </b-button>
          </div>
        </b-button-group>
      </div>


''' + _gen_abortButton() + '''\
''' + _gen_status_html() + '''\
''' + _gen_canvas_html() + '''\

    </b-container>
  </div>

    <!----------------- Start of app ---------------------------------->
    <script>
      window.app = new Vue({
        el: '#EXAMPLE_VAR_App',
        data: {
          EXAMPLE_INDEX_VAR: { "EAXMAPLE_SUBVAR_C": 0, "EAXMAPLE_SUBVAR_B": 0, "EAXMAPLE_VAR1": 0 },
          timer: '',
''' + _gen_status_variable() + '''\
          last_operation_result: '',
          EXAMPLE_list_items: null,
''' + _gen_canvas_data() + '''\
        },
        created: function () {
          this.fetchStatus(); 
          this.timer = setInterval(this.fetchStatus, ::seconds_between_updates::000);
        },
        mounted: function (){
          this.fetchEXAMPLEListItems()
        },
        watch: {
          EXAMPLE_INDEX_VAR: function () {
            this.draw_EXAMPLE(parseFloat(this.EXAMPLE_INDEX_VAR.EAXMAPLE_VAR1), parseFloat(this.EXAMPLE_INDEX_VAR.EAXMAPLE_SUBVAR_C))
          },
          EXAMPLE_list_items: function () {
            this.setup_canvas()
          }
        },
        beforeDestroy () {
          clearInterval(this.timer)
        },
        methods: {
''' + _gen_abort_and_status_related_methods() + '''
''' + _gen_canvas_js() + '''
''' +_gen_EXAMPLE_LIST_related_methods() + '''\
          moveToEXAMPLE_INDEX_ITME: function (EXAMPLE_INDEX_ITME) {
            status['currently_executing']='Move to EXAMPLE_INDEX_ITME'
            var xhr = new XMLHttpRequest()
            var self = this
            var url = 'move_to_EXAMPLE_INDEX_ITME?EXAMPLE_INDEX_ITME='+EXAMPLE_INDEX_ITME
            console.log("moveToEXAMPLE_INDEX_ITME: url is: "+url)
            xhr.open('GET', url)
            xhr.onload = function () {
              self.last_operation_result = JSON.parse(xhr.responseText)
              console.log( "moveToEXAMPLE_INDEX_ITME: Got from server: "+JSON.stringify(self.last_operation_result) )
            }
            xhr.send()
            self.last_operation_result = { 'success': '...', 'message': 'moveToEXAMPLE_INDEX_ITME ongoing' } 
          },
        },
      })
    </script>
'''
    return vue_app.replace("::seconds_between_updates::", seconds_between_updates)



def gen_EXAMPLE_PAGE1_page(seconds_between_updates):
    vue_app = '''
  <div id="EXAMPLE_INDEX_VARApp">
    <b-container>
'''+ _gen_menu_html("EXAMPLE SITE NAME")+'''\
''' + _gen_EXAMPLEACTION_btnGroup('EAXMAPLE_VAR1', "warning") + '''\
''' + _gen_EXAMPLEACTION_btnGroup('EAXMAPLE_SUBVAR_B', "info") + '''\
''' + _gen_EXAMPLEACTION_btnGroup('EAXMAPLE_SUBVAR_C', "primary") + '''\
      <br> 
''' + _gen_abortButton() + '''\
''' + _gen_status_html() + '''\
    </b-container>
  </div>

    <!-- Start running your app -->
    <script>
      window.app = new Vue({
        el: '#EXAMPLE_INDEX_VARApp',
        data: {
          EXAMPLE_SUBVARes: ["EAXMAPLE_VAR1", "EAXMAPLE_SUBVAR_B", "EAXMAPLE_SUBVAR_C"],
          EXAMPLE_INDEX_ITME_INDEX: 0.,
          EAXMAPLE_VAR1_candidate: '',
          EAXMAPLE_SUBVAR_B_candidate: '',
          EAXMAPLE_SUBVAR_C_candidate: '',
''' + _gen_status_variable() + '''\
          EXAMPLE_INDEX_VAR: { "EAXMAPLE_SUBVAR_C": 0, "EAXMAPLE_SUBVAR_B": 0, "EAXMAPLE_VAR1": 0 },
          timer: '',
          last_operation_result: '',
        },
        created: function () {
          this.fetchStatus(); 
          this.timer = setInterval(this.fetchStatus, ::seconds_between_updates::000);
        },
        beforeDestroy () {
          clearInterval(this.timer)
        },
        computed: {
          getEXAMPLE_INDEX_VARAsText() {
            return this.EXAMPLE_INDEX_VAR["EAXMAPLE_VAR1"]+" "+this.EXAMPLE_INDEX_VAR["EAXMAPLE_SUBVAR_C"]
          }
        },
        methods: {
''' + _gen_abort_and_status_related_methods() + '''\
          doEXAMPLEACTION: function (EXAMPLE_SUBVAR, directionToMove, duration) {
            status['currently_executing']='DO EXAMPLE ACTION'
            var xhr = new XMLHttpRequest()
            var self = this
            var url = 'do_EXAMPLE_ACTION?EXAMPLE_SUBVAR='+EXAMPLE_SUBVAR+'&direction='+directionToMove+'&duration='+duration
            console.log("doEXAMPLEACTION: url is: "+url)
            xhr.open('GET', url)
            xhr.onload = function () {
              self.last_operation_result = JSON.parse(xhr.responseText)
              console.log( "doEXAMPLEACTION: Got from server: "+JSON.stringify(self.last_operation_result) )
            }
            xhr.send()
            self.last_operation_result = { 'success': '...', 'message': 'EXAMPLE ACTION ongoing' } 
          },
          moveSingleEXAMPLESUBVAR: function (EXAMPLE_SUBVAR, target) {
            status['currently_executing']='EXAMPLE ACTION'
            var xhr = new XMLHttpRequest()
            var self = this
            console.log("moveSingleEXAMPLESUBVAR: Starting")
            xhr.open('GET', 'do_EXAMPLE_ACTION?EXAMPLE_SUBVAR='+EXAMPLE_SUBVAR+'&target='+target)
            xhr.onload = function () {
              self.last_operation_result = JSON.parse(xhr.responseText)
              console.log( "moveSingleEXAMPLESUBVAR: Got from server: "+JSON.stringify(self.last_operation_result) )
            }
            xhr.send()
            self.last_operation_result = { 'success': '...', 'message': 'EXAMPLE ACTION ongoing' } 
          },
          getCurrentEXAMPLEVALUE(EXAMPLE_SUBVAR) { 
            return this.EXAMPLE_INDEX_VAR[EXAMPLE_SUBVAR]
          }
        },
      })
    </script>
'''
    return vue_app.replace("::seconds_between_updates::", seconds_between_updates)


def gen_EXAMPLE_PAGE2_page(seconds_between_updates):
    # Functionality of this Vue app:
    #     Show EXAMPLE_INDEX_ITME table

    vue_app = '''
  <div id="EXAMPLE_VAR_App">
    <b-container>
'''+ _gen_menu_html("EXAMPLE SITE NAME")+'''\
      </------Show current EXAMPLE_INDEX_VAR------/->
     
      <div class="container">
        <h4> Current EXAMPLE_INDEX_VAR: 
          <strong>
            {{ EXAMPLE_INDEX_VAR.EAXMAPLE_VAR1+" "+ EXAMPLE_INDEX_VAR.EAXMAPLE_SUBVAR_B+" "+ EXAMPLE_INDEX_VAR.EAXMAPLE_SUBVAR_C }}
          </strong> 
        </h4>
        <div class="row">
          <h4 class="control-label col-5">Add current EXAMPLE_INDEX_VAR as new EXAMPLE Item index:</h4>
          <b-form-input class="col-1" v-model="new_EXAMPLE_list_item_INDEX">
          </b-form-input>
          <b-btn class="col-2" v-on:click="addNewEXAMPLEListItem()" variant="info">
            Add
          </b-btn>
          <div class="col-5"></div>
        </div>
      </div>


      <br> <br> 
      <div>
        <h4>EXAMPLE Items:</h4>
        <b-table-simple hover small caption-top responsive>
          <b-thead head-variant="dark">
            <b-tr>
              <b-th>EXAMPLE_INDEX_VAR</b-th>
              <b-th>EAXMAPLE_VAR1</b-th>
              <b-th>EAXMAPLE_SUBVAR_B</b-th>
              <b-th>EAXMAPLE_SUBVAR_C</b-th>
            </b-tr>
          </b-thead>
          <b-tbody>
            <b-tr v-for="EXAMPLE_INDEX_ITME in EXAMPLE_list_items">
              <b-td v-text="EXAMPLE_INDEX_ITME.EXAMPLE_INDEX_VAR"></b-td>
              <b-td v-text="EXAMPLE_INDEX_ITME.EXAMPLE_VAR1"></b-td>
              <b-td v-text="EXAMPLE_INDEX_ITME.EXAMPLE_VAR2"></b-td>
              <b-td v-text="EXAMPLE_INDEX_ITME.EXAMPLE_VAR3"></b-td>
              <b-td><b-button @click="deleteEXAMPLEListItem(EXAMPLE_INDEX_ITME.EXAMPLE_INDEX_VAR)">Delete</b-button></b-td>
            </b-tr>
          </b-tbody>
        </b-table-simple>
      </div>

      <br> <br> 
      <h4>All EXAMPLE_INDEX_ITMEs:</h4>
      <div>
        <b-table striped hover :items="EXAMPLE_INDEX_ITMEs"></b-table>
      </div>

    </b-container>
  </div>

    <!----------------- Start of app ---------------------------------->
    <script>
      window.app = new Vue({
        el: '#EXAMPLE_VAR_App',
        data: {
          EXAMPLE_INDEX_VAR: { "EAXMAPLE_SUBVAR_C": 0, "EAXMAPLE_SUBVAR_B": 0, "EAXMAPLE_VAR1": 0 },
          timer: '',
''' + _gen_status_variable() + '''\
          EXAMPLE_list_items: null,
          new_EXAMPLE_list_item_INDEX_VAR: "",
          EXAMPLE_INDEX_ITMEs: ::EXAMPLE_INDEX_ITMEs::
        },
        created: function () {
          this.fetchStatus(); 
          this.timer = setInterval(this.fetchStatus, ::seconds_between_updates::000);
        },
        mounted: function (){
          this.fetchEXAMPLEListItems()
        },

        beforeDestroy () {
          clearInterval(this.timer)
        },
        methods: {
''' + _gen_abort_and_status_related_methods() + '''
''' +_gen_EXAMPLE_LIST_related_methods() + '''\

        },
      })
    </script>
'''

    EXAMPLE_STATIC_ITMEs = yaml.load( open("EXAMPLE_DATA.yaml") )
    s = " [\n"
    for ITEM in EXAMPLE_STATIC_ITMEs:
        s += "    { EXAMPLE_INDEX: '"+ str(ITEM["x"]) + "', EXAMPLE_y_1: '"+ str(ITEM["y_1"]) +"', EXAMPLE_y_2: '"+ str(ITEM["y_2"]) +"' },\n"
    s = s[:-2]+"\n"    # Get rid of the last comma
    s += "]\n"

    EXAMPLE_ITMEs = "??????"
    return vue_app.replace("::seconds_between_updates::", seconds_between_updates).replace("::EXAMPLE_ITMEs::", EXAMPLE_ITMEs)



