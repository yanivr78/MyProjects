#! /usr/bin/python

import boto.s3

connection = boto.s3.connect_to_region("us-east-1")
bucket = connection.get_bucket("apx.uploads.int")
keys = bucket.list("uploads/sounds/130376")
for key in keys:
	print(key)
versions = bucket.list_versions("uploads/sounds/130376")
for version in versions:
	print("{} {} {}".format(version.name, version.last_modified, version.version_id))


