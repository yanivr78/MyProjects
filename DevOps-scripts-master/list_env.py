#!/usr/bin/python
# Date : 28/Jul/2015
# Show AWS enviorment version 1.0
# Written by : Yaniv Ron

import boto.ec2

# PARAMS

# Start work


def print_all_instances(connection):
	reservations = connection.get_all_instances()
	for res in reservations:
	    for inst in res.instances:
		if 'Name' in inst.tags:
		    print ("{} {} {} {} {}".format(inst.tags['Name'], inst.id, inst.state, inst.ip_address, inst.private_ip_address))
		else:
		    print "%s [%s]" % (inst.id, inst.state)


for region in ("us-east-1", "eu-central-1"):
	print("\nRegion: {0}".format(region))
	print_all_instances(boto.ec2.connect_to_region(region))

