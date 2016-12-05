#/bin/python
from boto.s3.connection import S3Connection

bucket = conn.get_bucket('apx.logs')

for key in bucket.list():
    print key.name.encode('utf-8')
