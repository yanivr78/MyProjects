#!/bin/sh
set -e 
set -u
VERSION=$1


AUTO_SCALING_GROUPS="ASG_Frontend_Multi_AZ ASG_Biz_Multi_AZ"

for ASG in $AUTO_SCALING_GROUPS ; do
  echo now setting for $ASG
  aws autoscaling create-or-update-tags --tags "ResourceId=$ASG,ResourceType=auto-scaling-group,Key=Version,Value=$VERSION,PropagateAtLaunch=true"
done
