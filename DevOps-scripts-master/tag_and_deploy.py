#!/usr/bin/env python
# Change Amazon EC2 tag for Frontends and run the deployment script

import os
import subprocess

INSTANCE_ID = os.environ.get("EC2_INSTANCE_ID", "i-00000000example")
ver = raw_input("Please enter the version number: ")
subprocess.call([
    "aws", "ec2", "create-tags",
    "--resources", INSTANCE_ID,
    "--tags", "Key=Version,Value={0}".format(ver),
])
subprocess.call("/var/lib/cloud/scripts/per-boot/01deploy_frontend.sh", shell=True)
