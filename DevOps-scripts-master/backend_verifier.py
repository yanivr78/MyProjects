#!/usr/bin/python

from sys import argv
import subprocess

script, ip = argv

command = raw_input("Type in the command that you would like to run :")
subprocess.call(["ssh", "root@" + ip, "-o", "StrictHostKeyChecking=no", "echo {} >> .ssh/authorized_keys".format(command)])
