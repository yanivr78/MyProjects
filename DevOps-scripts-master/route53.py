#!/bin/python
# Date : 28/Jul/2015
# Route 53 PTR Import utility version 0.1
# Written by : Yaniv Ron

import boto.route53
from boto.route53.record import ResourceRecordSets


# PARAMS

conn = boto.route53.connect_to_region('eu-central-1')
change_set = ResourceRecordSets(conn, "Z2FRPEUUP8KSK8")



# START WORK

change = change_set.add_change("CREATE", "utm-b.appoxee-eu.local", "PTR")
change.add_value("10.0.3.7")
result = change_set.commit()

