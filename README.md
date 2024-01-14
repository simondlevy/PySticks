This Python library simplifies the task of flying an actual or simulated aerial
vehicle, like a quadcopter, using a joystick or game controller.  The code
automatically detects what kind of device you're using and, for game
controllers, sets the axes (throttle, aileron/roll, elevator/pitch, rudder/yaw)
to the popular
[Mode 2](https://www.rc-airplane-world.com/rc-transmitter-modes.html)
configuration.  The right shoulder button is used for toggling the auxiliary
channel.  Stick values (including the auxiliary) are returned in the interval
[-1,+1].

To install the library, run a command (terminal) window, change to the
<b>PySticks</b> directory and run the command <tt>pip3 install -e .</tt> You
can then test your controller by running the <b>tester.py</b> script.

If your controller isn't suported (or isn't behaving as expected), you can
add a new controller (or remedy the problem) as follows:

1. Run the <b>joyreporter.py</b> script to see the name of your controller and
how its axes are mapped on your OS

2. Add (modify) this information as in the <tt>controllers</tt> dictionary in
<b>pysticks/\_\_init\_\_.py</b> 

