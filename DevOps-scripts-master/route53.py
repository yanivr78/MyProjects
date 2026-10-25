#!/usr/bin/env python
# Date : 28/Jul/2015
# Route 53 PTR Import utility version 0.1
# Written by : Yaniv Ron

import os
import boto.route53
from boto.route53.record import ResourceRecordSets

REGION = os.environ.get("AWS_REGION", "eu-central-1")
HOSTED_ZONE_ID = os.environ.get("ROUTE53_ZONE_ID", "Z0000000000EXAMPLE")
PTR_RECORD_NAME = os.environ.get("PTR_RECORD_NAME", "host-b.internal.example.local")
PTR_TARGET_IP = os.environ.get("PTR_TARGET_IP", "192.0.2.7")

conn = boto.route53.connect_to_region(REGION)
change_set = ResourceRecordSets(conn, HOSTED_ZONE_ID)

change = change_set.add_change("CREATE", PTR_RECORD_NAME, "PTR")
change.add_value(PTR_TARGET_IP)
result = change_set.commit()
