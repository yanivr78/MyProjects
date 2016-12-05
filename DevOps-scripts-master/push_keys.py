#!/usr/bin/python

from sys import argv
import subprocess

script, ip = argv

keys = raw_input("Please paste your keys:")
subprocess.call(["ssh", "root@" + ip, "-o", "StrictHostKeyChecking=no", "echo {} >> .ssh/authorized_keys".format(keys)]) 

