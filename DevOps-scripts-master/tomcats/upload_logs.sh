#!/bin/bash
source /root/.bash_profile

set -u
set -e

EXTENSION="s3"
LOGDIR=/data/tomcat/log

INSTANCE_IPS=`list_instances.rb --environment Production --group Backend | jq -r '.[] | .private_ip_address'`
for HOST in $INSTANCE_IPS 
do
	echo $HOST
	set +e
	ssh $HOST rm $LOGDIR/*.uploaded
	LOGFILES=`ssh $HOST ls $LOGDIR/*.$EXTENSION 2>/dev/null`
	set -e
	for LOGFILE in $LOGFILES ; do
echo $LOGFILE
        	DATETIME=`echo $LOGFILE | grep -P -o '(\d{8,14})' || date --date="1 days ago" +%Y%m%d`
        	DATE=`echo $LOGFILE | grep -P -o '(\d{8})' || date --date="1 days ago" +%Y%m%d`
        	HOUR=`echo $LOGFILE | grep -P -o '(?<=\d{8})(\d{4})' || echo "0000"`
        	if [[ $LOGFILE == *.log* ]]
	        then
        	        BUCKET=apx.logs.permanent;
			STORAGE_CLASS=STANDARD
	        else
	                BUCKET=apx.logs;
			STORAGE_CLASS=REDUCED_REDUNDANCY
	        fi
	        DST_NAME=`basename $LOGFILE .$EXTENSION| sed -e "s/$DATETIME//" -e 's/\.\././' -e 's/-//' -e 's/\.DONE//' `
	        DST_PATH="tomcat/$DATE/$DST_NAME/$HOUR/$HOST.gz"
	        echo "Copy $LOGFILE@$HOST to s3://$BUCKET/$DST_PATH $STORAGE_CLASS"
	        scp root@$HOST:$LOGFILE /dev/stdout |gzip -c -3 > /tmp2/tmpupload; aws s3 cp  --sse --storage-class $STORAGE_CLASS /tmp2/tmpupload s3://$BUCKET/$DST_PATH
	        ssh $HOST mv $LOGFILE $LOGFILE.uploaded
		ssh $HOST touch /var/run/logupload.flag
	done
done

