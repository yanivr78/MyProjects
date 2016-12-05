#!/bin/bash
source /root/.bash_profile

set -u
set -e

EXTENSION="s3"
LOGDIR=/data/tomcat/log

INSTANCE_IPS='10.0.102.14'
for HOST in $INSTANCE_IPS 
do
	echo $HOST
	set +e
	ssh $HOST rm $LOGDIR/*.uploaded
	LOGFILES=`ssh $HOST ls $LOGDIR/*.$EXTENSION`
	set -e
	for LOGFILE in $LOGFILES ; do
echo $LOGFILE
        	DATE=`echo $LOGFILE | grep -P -o '(\d{8})' || date --date="0 days ago" +%Y%m%d`
        	if [[ $LOGFILE == *.log* ]]
	        then
        	        BUCKET=apx.logs.permanent;
			STORAGE_CLASS=STANDARD
	        else
	                BUCKET=apx.logs;
			STORAGE_CLASS=REDUCED_REDUNDANCY
	        fi
	        DST_NAME=`basename $LOGFILE .$EXTENSION| sed -e "s/$DATE//" -e 's/\.\././' -e 's/-//' `
	        DST_PATH="tomcat/$DATE/$DST_NAME/$HOST.pre360.gz"
	        echo "Copy $LOGFILE@$HOST to s3://$BUCKET/$DST_PATH $STORAGE_CLASS"
	        scp root@$HOST:$LOGFILE /dev/stdout |gzip -c -3 > /tmp/tmpupload; aws s3 cp  --sse --storage-class $STORAGE_CLASS /tmp/tmpupload s3://$BUCKET/$DST_PATH
	        ssh $HOST mv $LOGFILE $LOGFILE.uploaded
		ssh $HOST touch /var/run/logupload.flag
	done
done

