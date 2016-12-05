#!/bin/bash

set +e
set -u

if [ -z "$1" ]; then
  echo "Host not provided"
  exit 1
fi

echo "Stopping consumers in $1"
stopped=`echo "run stop -b saas.beans:name=MessagingActivationManager" | java -jar jmxterm-1.0-alpha-4-uber.jar -i - -l $1:7009 2>/dev/null`
#if [ $stopped == "true" ]; then
if true; then
  echo "Restarting $1"
  ssh root@$1 /etc/init.d/tomcat stop
  ssh root@$1 "source /etc/aws/cred.profile; source /usr/local/bin/get_current_instance_id.sh ; /usr/local/bin/extract_backend.sh > /var/log/deploy.log 2> /var/log/deploy.log"
  ssh root@$1 /etc/init.d/tomcat start
  echo "Done"
else
  echo "Could not stop consumers. aborting"
fi
