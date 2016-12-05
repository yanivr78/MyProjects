#!/usr/bin/python
# Change amazon tag for Frontends and run the deployment

import subprocess

ver = raw_input("Please enter the version number:")
subprocess.call(["aws", "ec2", "create-tags", "--resources",  "i-a4293345", "--tags", "Key=Version,Value={0}".format(ver)])
subprocess.call("/var/lib/cloud/scripts/per-boot/01deploy_frontend.sh", shell=True)
~                                                                                     
