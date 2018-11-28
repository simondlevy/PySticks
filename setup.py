'''
Python distutils setup file for installing PySticks

Copyright (C) Simon D. Levy 2018

This file is part of PySticks.

PySticks is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
PySticks is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MEReceiverHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PySticks.  If not, see <http://www.gnu.org/licenses/>.
'''

from distutils.core import setup

setup (name = 'PySticks',
       packages = ['pysticks'],
       requires = ['pygame'],
       version = '0.1',
       description = 'Python API for flying with game controllers',
       author_email='simon.d.levy@gmail.com',
       url='https://github.com/simondlevy/PySticks',
       license='LGPL',
       platforms='Linux; Windows')

