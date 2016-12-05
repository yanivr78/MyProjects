#!/bin/sh
set -e 
set -u
VERSION=$1

INSTANCE_IDS=`list_instances.rb --environment Production --group Frontend | jq -r '.[] | .instance_id'|tr "\\n" " " ``list_instances.rb --environment Production --group Frontend-Engage | jq -r '.[] | .instance_id'|tr "\\n" " "`
echo $INSTANCE_IDS
sleep 4
INSTANCE_IPS=`list_instances.rb --environment Production --group Frontend | jq -r '.[] | .private_ip_address'`" "`list_instances.rb --environment Production --group Biz | jq -r '.[] | .private_ip_address'`

aws ec2 create-tags --resources $INSTANCE_IDS --tags Key=Version,Value=$VERSION
set +e
echo -e $INSTANCE_IPS| tr " " "\\n"|pssh -i -p10 -h /dev/stdin killall -9 phantomjs
set -u
echo -e $INSTANCE_IPS| tr " " "\\n"|pssh -i -t0 -p10 -h /dev/stdin /var/lib/cloud/scripts/per-boot/01deploy_frontend.sh
echo -e $INSTANCE_IPS| tr " " "\\n"|pssh -i -t0 -p10 -h /dev/stdin /var/lib/cloud/scripts/per-boot/02deploy_config.sh

