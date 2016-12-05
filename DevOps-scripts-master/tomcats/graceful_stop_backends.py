#!/usr/bin/python

# Graceful restart backends version 1.0
# Written by : Yaniv Ron

# Importing modules
import subprocess
import paramiko

# Params (String for all backends)
ip=["10.0.2.84", "10.0.3.84", "10.0.2.85", "10.0.3.85", "10.0.2.94", "10.0.3.94"]

# Java stop command
# Sending a stop to "MessagingActivationManager" via JMXTERM CLI commands
stop_consumers="echo \"run stop -b saas.beans:name=MessagingActivationManager\" | java -jar jmxterm-1.0-alpha-4-uber.jar -i - -l 127.0.0.1:7009 2>/dev/null"

for i in range(len(ip)):
    print("-----Restarting %s--------") % (ip[i])
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(
    # Avoiding SSH KEY exchanges prompts (workaround)
    paramiko.AutoAddPolicy())
    ssh.connect(ip[i], username='root')
    stdin, stdout, stderr = ssh.exec_command(stop_consumers) 
    result1=stdout.read()
    result2=stderr.read()
    
    if result1:
      print("\n%s was restarted succesfuly:\nInfo: %s" % (ip[i],result1))
      stdin, stdout, stderr = ssh.exec_command("/etc/init.d/tomcat stop")
      # Exception handling
      tomcat_result=stdout.read()
      tomcat_err_result=stderr.read()

      if tomcat_result:
        print ("\nTomcat was stoped succesfuly for %s !\n" % ip[i])
      
      if tomcat_err_result:
        print("\nTomcat restart had errors for %s\nError info:\n%s" % (ip[i], tomcat_err_result))


    if result2:
      print("\nError: %s consumers stop have failed\nReason:\n%s" % (ip[i],result2))
