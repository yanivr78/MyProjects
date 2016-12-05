#!/bin/bash
multitail -l 'ssh root@10.0.102.9 tail -F /data/tomcat/log/catalina.out' -l 'ssh root@10.0.102.10 tail -F /data/tomcat/log/catalina.out' -l 'ssh root@10.0.102.11 tail -F /data/tomcat/log/catalina.out' -l 'ssh root@10.0.102.12 tail -F /data/tomcat/log/catalina.out' -l 'ssh root@10.0.102.13 tail -F /data/tomcat/log/catalina.out'
