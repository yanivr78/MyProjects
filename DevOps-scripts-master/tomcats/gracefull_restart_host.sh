#!/bin/bash

set -e
set -u

if [ -z "$1" ]; then
  echo "Host not provided"
  exit 1
fi

echo "Stopping consumers in $1"
stopped=`echo "run stop -b saas.beans:name=MessagingActivationManager" | java -jar jmxterm-1.0-alpha-4-uber.jar -i - -l $1:7009 2>/dev/null`
echo $stopped
if [ $stopped == "true" ]; then
  echo "Restarting $1"
  ssh root@$1 /etc/init.d/tomcat stop
  sleep 1
  ssh root@$1 /etc/init.d/tomcat start
  echo "Done"
else
  echo "Could not stop consumers. aborting"
fi
