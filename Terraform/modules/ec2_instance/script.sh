#!/bin/bash
echo "nameserver 10.230.36.2" >> /etc/resolv.conf
apt-get -y install nginx
