This Python library simplifies the task of flying an actual or simulated aerial
vehicle, like a quadcopter, using a game controller.  The code automatically
detects what kind of controller you're using and sets the axes (throttle,
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
