#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pexpect
import sys
import os
import time

f = open('./openVPNUsernamePassword.txt')
lines = f.read().splitlines()
right = len(lines) - 1
try:
    while lines[right] == '':
        right -= 1
except IndexError:
    print("No username and password found")
    exit(-1)
username, password = lines[right].strip().split(', ')
print([username, password])
print(lines)
child = pexpect.spawn('/bin/bash')
# child.logfile = sys.stdout
child.sendline("sudo protonvpn configure")
#time.sleep(0.5)
#child.expect("Please enter your choice or leave empty")
child.sendline('1')
time.sleep(0.2)
#child.expect(".*Enter your ProtonVPN OpenVPN username.*")
time.sleep(0.2)
child.sendline(username)
#child.expect(".*Enter your ProtonVPN OpenVPN password.*")
time.sleep(0.3)
child.sendline(password)
#child.expect(".*Confirm your OpenVPN password.*")
time.sleep(0.2)
child.sendline(password)
#child.expect(".*Username and Password has been updated!.*")
time.sleep(0.2)
