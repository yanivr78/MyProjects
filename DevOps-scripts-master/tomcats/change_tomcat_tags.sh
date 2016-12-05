#!/bin/sh
set -e 
set -u
VERSION=$1

INSTANCE_IDS=`list_instances.rb --environment Production --group Backend | jq -r '.[] | .instance_id'|tr "\\n" " "`

aws ec2 create-tags --resources $INSTANCE_IDS --tags Key=Version,Value=$VERSION

