#!/usr/bin/env python3
'''
tester.py: Test program for PySticks

Requires: pygame

Copyright (C) Simon D. Levy 2016

This file is part of Hackflight.

Hackflight is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.  This code is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU Lesser General Public License along
with this code.  If not, see <http:#www.gnu.org/licenses/>.
'''

from pysticks import get_controller

con = get_controller()

while True:

    try:

        con.update()

        print(('Throttle: %+2.2f   Roll: %+2.2f   Pitch: %+2.2f   ' +
               'Yaw: %+2.2f   Aux: %+2.2f') %
              (
                 con.getThrottle(),
                 con.getRoll(),
                 con.getPitch(),
                 con.getYaw(),
                 con.getAux()),
              end='\r')

    except KeyboardInterrupt:

        break
