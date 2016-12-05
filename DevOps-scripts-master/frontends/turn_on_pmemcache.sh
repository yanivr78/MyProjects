#!/bin/sh

INSTANCE_IDS=`list_instances.rb --environment Production --group Frontend | jq -r '.[] | .instance_id'|tr "\\n" " "`
INSTANCE_IPS=`list_instances.rb --environment Production --group Frontend | jq -r '.[] | .private_ip_address'`

aws ec2 create-tags --resources $INSTANCE_IDS --tags Key=Config,Value=09072014
echo -e $INSTANCE_IPS| tr " " "\\n"|pssh -i -h /dev/stdin killall -9 phantomjs
echo -e $INSTANCE_IPS| tr " " "\\n"|pssh -i -t0 -h /dev/stdin /var/lib/cloud/scripts/per-boot/02deploy_config.sh
