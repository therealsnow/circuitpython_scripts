This script uses powershell to disable windows firewall allowing for backdooring through windows explorer. This script contains an if loop preventing it from running if jobdone.txt is present. In order to get this to run you must first remove jobdone.txt

#Changelog

1. V1 initial upload
2. V1.1 Added code to output IP addresses of target machine to jobdone.txt to store IP address information of target machine
