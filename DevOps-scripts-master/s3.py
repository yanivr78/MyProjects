#!/usr/bin/env python
import os
from boto.s3.connection import S3Connection

BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "example-logs-bucket")

conn = S3Connection()
bucket = conn.get_bucket(BUCKET_NAME)

for key in bucket.list():
    print(key.name.encode("utf-8"))
