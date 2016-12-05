#!/bin/bash

cat tomcat_hosts | xargs -P 12 -n 1 ./gracefull_shutdown_host.sh
