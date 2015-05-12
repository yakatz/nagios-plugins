#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nagios plugin to check if a debian based system needs to be rebooted.
Copyright (c) 2012 Peter Kropf. All rights reserved.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
On debian based systems, the existance of /var/run/reboot-required
(and /var/run/reboot-required.pkgs) lets the user know that the system
needs to be rebooted. The .pkgs file tells why.
This plugin looks for /var/run/reboot-required and returns a warning
if it's found. Otherwise it returns ok.
Example:
    ./check_reboot_required
"""


import sys
import os
from optparse import OptionParser


prefix = 'check_reboot_required'

class nagios:
    ok       = (0, 'OK')
    warning  = (1, 'WARNING')
    critical = (2, 'CRITICAL')
    unknown  = (3, 'UNKNOWN')


def exit(status, message):
    print prefix + ' ' + status[1] + ' - ' + message
    sys.exit(status[0])

reboot_required_path = '/var/run/reboot-required'

if os.path.exists(reboot_required_path):
    exit(nagios.warning, 'reboot required')

else:
    exit(nagios.ok, 'no reboot required')
