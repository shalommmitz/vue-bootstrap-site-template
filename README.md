Shalom Mitz                                               


Cyber safety
------------

This server is NOT safe to run on un-trusted networks.
Specifically, do not expose it to the public Internet.
The server currently uses http. The uwsgi server, however, supports https.

Software setup:
---------------

We use Xubuntu 18.04, but probably any other Linux system will work.
Also, you can probably use Windows, using either WSL or CygWin, to run the uwsgi server.
Another option, in case you are unfortunate enough to have to run Windows, is using a Virtual machine.

To install the software on Xubuntu:

 - Install UWSGI (an easy to configure web-server):
   `sudo apt install uwsgi uwsgi-plugin-python`
 - Install misc Python modules:
   `apt install python-cookies, python-numpy, python-yaml, python-mathplotlib`

Other Preparations:
------------------

- Adding users for the server

    Run `manage_users` and add users.
    Do not worry about the IP addresses: those will be updated next time the user login.

- Testing and development
  
  You can change the name of the PC used for development at the file "Utils.py". 
  This will force the server to enter simulator mode when running on this machine.

Licenses
========
This software is licensed under the MIT license.
This software uses a single image from pixabay.com. License terms are at: https://pixabay.com/service/license/
This software includes copies of both "bootstrap" and "vue-bootstrap". However, you might choose to use the copies from the original sites. Copies of the two liberties are present to allow use w/o connection to the Internet.
