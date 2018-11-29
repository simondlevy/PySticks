This Python library simplifies the task of flying an actual or simulated aerial
vehicle, like a quadcopter, using a joystick or game controller.  The code automatically
detects what kind of device you're using and, for game controllers, sets the axes (throttle,
aileron/roll, elevator/pitch, rudder/yaw) to the popular
[Mode 2](http://www.spektrumrc.com/Articles/Article.aspx?ArticleID=2105)
configuration.  The right trigger is used for toggling the auxiliary channel.
Stick values (including the auxiliary) are returned in the interval [-1,+1].

This library has been tested on Windows 10 and Ubuntu 18.04, with the following
devices:

* PS3 controller
* PS4 controller
* Xbox 360 controller
* Logitech Extreme 3D Pro joystick
* Spektrum transmitter with WS1000 wireless simulator dongle
* FrSky Taranis TX9 RC transmitter with mini USB cable 

If your controller isn't in this list, you can add a new controller as follows:

1. Run the <b>joyreporter.py</b> script to see the name of your controller and how its axes are mapped on your OS
2. Add this information as an entry in the <tt>controllers</tt> dictionary in <b>pysticks/__init__.py</b> 

