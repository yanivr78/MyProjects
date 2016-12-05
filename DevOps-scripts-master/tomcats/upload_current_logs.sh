#!/bin/bash
set -e 
set -u


BACKUP_DATE=$(date +%Y%m%d)

INSTANCE_IPS=`list_instances.rb --environment Production --group Backend | jq -r '.[] | .private_ip_address'`
for HOST in $INSTANCE_IPS 
do
	echo $HOST
	FILES=`ssh root@$HOST ls /data/tomcat/log/*.log /data/tomcat/log/catalina.out|xargs -n1 basename`
	for FILE in $FILES
	do
		scp root@$HOST:/data/tomcat/log/$FILE /dev/stdout | gzip -c > /tmp/tmpupload ; aws s3 cp /tmp/tmpupload s3://apx.logs/tomcat/$HOST/$BACKUP_DATE/$FILE.gz --storage-class REDUCED_REDUNDANCY --sse; rm -f /tmp/tmpupload


	done

done
