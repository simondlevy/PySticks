#!/usr/bin/env python3
'''
pysticks.py: Python classes for flying with joysticks, R/C controllers

Requires: pygame

Copyright (C) Simon D. Levy 2016

This file is part of PySticks.

PySticks is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License 
along with this PySticks.  If not, see <http:#www.gnu.org/licenses/>.
'''

import pygame
import time

class Controller(object):

    STICK_DEADBAND = .05

    def __init__(self, axis_map):

        self.joystick = None
        self.axis_map = axis_map
        
    def update(self):

        pygame.event.pump()

    def getThrottle(self):

        return self._getAxis(0)

    def getRoll(self):

        return self._getAxis(1)

    def getPitch(self):

        return self._getAxis(2)

    def getYaw(self):

        return self._getAxis(3)

    def _getAxis(self, k):

        j = self.axis_map[k]
        val = self.joystick.get_axis(abs(j))
        if abs(val) < Controller.STICK_DEADBAND:
            val = 0
        return (-1 if j<0 else +1) * val

class _GameController(Controller):

    def __init__(self, axis_map, button_id):

        Controller.__init__(self, axis_map)
        self.button_id = button_id
        self.button_is_down = False
        self.switch_value = -1

    def _getAuxValue(self):

        return self.joystick.get_button(self.button_id)
        
    def getAux(self):

        if self._getAuxValue():
            if not self.button_is_down:
                self.switch_value = -self.switch_value
            self.button_is_down = True
        else:
            self.button_is_down = False
        return self.switch_value

class _SpringyThrottleController(_GameController):

    def __init__(self, axis_map, button_id):

        _GameController.__init__(self, axis_map, button_id)
        
        self.throttleval = -1

        self.prevtime = 0

    def getThrottle(self):

        currtime = time.time()

        # Scale throttle increment by time difference from last update
        self.throttleval += self._getAxis(0) * (currtime-self.prevtime)

        # Constrain throttle to [-1,+1]
        self.throttleval = min(max(self.throttleval, -1), +1)

        self.prevtime = currtime

        return self.throttleval

class _RcTransmitter(Controller):

    def __init__(self, axis_map, aux_id):

        Controller.__init__(self, axis_map)
        self.aux_id = aux_id
        
    def getAux(self):

        return +1 if self.joystick.get_axis(self.aux_id) > 0 else -1
        
class _Xbox360(_SpringyThrottleController):

    def __init__(self, axes, aux):

        _SpringyThrottleController.__init__(self, axes, None)

        self.aux = aux

    def _getAuxValue(self):

        return self.joystick.get_axis(self.aux) < -.5

class _Playstation(_SpringyThrottleController):

    def __init__(self, axes):

        _SpringyThrottleController.__init__(self, axes, 7)
        

# Different OSs have different names for the same controller, so we don't
# need to check OS when setting up the axes.
controllers = {
    'Controller (Rock Candy Gamepad for Xbox 360)'       : _Xbox360((-1,4,-3,0), 2), 
    'Rock Candy Gamepad for Xbox 360'                    : _Xbox360((-1,3,-4,0), 5), 
    '2In1 USB Joystick'                                  : _Playstation((-1,2,-3,0)),
    'Wireless Controller'                                : _Playstation((-1,2,-3,0)),
    'SHANWAN Android Gamepad'                            : _Playstation((-1,2,-3,0)),
    'MY-POWER CO.,LTD. 2In1 USB Joystick'                : _Playstation((-1,2,-3,0)),
    'Sony Interactive Entertainment Wireless Controller' : _Playstation((-1,3,-4,0)),
    'Logitech Extreme 3D'                                : _GameController((-2,0,-1,3), 0),
    'Logitech Logitech Extreme 3D'                       : _GameController((-3,0,-1,2), 0),
    'FrSky Taranis Joystick'                             : _RcTransmitter((0,1,2,5), 3),
    'FrSky FrSky Taranis Joystick'                       : _RcTransmitter((0,1,2,3), 5),
    'SPEKTRUM RECEIVER'                                  : _RcTransmitter((1,2,5,0), 4),
    'Horizon Hobby SPEKTRUM RECEIVER'                    : _RcTransmitter((1,2,3,0), 4)
    }

def get_controller():

    # Initialize pygame for joystick support
    pygame.display.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Find your controller
    controller_name = joystick.get_name()
    if not controller_name in controllers.keys():
        print('Unrecognized controller: %s' % controller_name)
        exit(1)
    controller = controllers[controller_name]
    controller.joystick = joystick

    return controller
