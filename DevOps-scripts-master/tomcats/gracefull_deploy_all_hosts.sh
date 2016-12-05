#!/bin/bash

cat tomcat_hosts | xargs -P 20 -n 1 ./gracefull_deploy_host.sh
