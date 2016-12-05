#!/bin/bash
source /root/.bash_profile

set -u
set -e

EXTENSION=`date -d 'yesterday' +'%Y-%m-%d'`".log"
LOGDIR=/data/tomcat/log

INSTANCE_IPS=`list_instances.rb --environment Production --group Backend | jq -r '.[] | .private_ip_address'` 
INSTANCE_IPS="$INSTANCE_IPS 10.0.102.22"
for HOST in $INSTANCE_IPS 
do
	echo $HOST
	set +e
	LOGFILES=`ssh $HOST ls $LOGDIR/*.$EXTENSION 2>/dev/null`
	set -e
	for LOGFILE in $LOGFILES ; do
echo $LOGFILE
        	DATE=`date --date="yesterday" +%Y%m%d`
		BUCKET="apx.logs"
		STORAGE_CLASS=REDUCED_REDUNDANCY
	        DST_NAME=`basename $LOGFILE .$EXTENSION `
	        DST_PATH="tomcat/$DATE/$DST_NAME/0000/$HOST.gz"
	        echo "Copy $LOGFILE@$HOST to s3://$BUCKET/$DST_PATH $STORAGE_CLASS"
	        scp root@$HOST:$LOGFILE /dev/stdout |gzip -c -3 > /tmp2/tmpupload; aws s3 cp  --sse --storage-class $STORAGE_CLASS /tmp2/tmpupload s3://$BUCKET/$DST_PATH
	        ssh $HOST mv $LOGFILE $LOGFILE.uploaded
		ssh $HOST touch /var/run/logupload-extra.flag
	done
done

