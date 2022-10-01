# LNX-06 Processes
Becoming familiar with processes.

## Key terminology
### Processes
Processes in Linux can be divided into three categories: Daemons, Services, and Programs

### Daemons
Daemon is the term used to describe a process that is active in the background to perform certain tasks.

### Telnet
Telnet is a command used to create a remote connection with a system over a TCP/IP network.

### $PATH
The system variable PATH ( $PATH ) specifies a set of directories where executable programs reside.

### PID
A PID is an abbreviation for Process Identification Number.
#

## Exercise
- Download and start Telnet Daemon
- Show the PID 
- Show how much memory Telnet uses
- Stop Telnet
#

### Sources
https://www.cyberciti.biz/faq/unix-restart-inetd-service-daemon/

https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap3sec21.html

https://www.dispersednet.com/linux-network-admin/module4/inetd-daemon-vitalComponent-unixSystem.php

https://www.digitalworldz.co.uk/threads/telnet-command-to-check-memory-usage.284579/

https://www.2daygeek.com/linux-commands-check-memory-usage/

https://www.javatpoint.com/linux-telnet-command

https://www.cyberciti.biz/faq/kill-process-in-linux-or-terminate-a-process-in-unix-or-linux-systems/
#

### Overcome challenges
I still spent quite a long time trying to start Telnet, finding the right command was quite difficult. I found out after much searching that it was more with the name INETD and that allowed me to search more specifically.

### Results
Start Telnet

![start](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a3f357b5ca41920c1b095d1a96a9b688d102a060/00_includes/Week%201/LNX/LNX-06_1%20Start.png)

PID

![PID](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a3f357b5ca41920c1b095d1a96a9b688d102a060/00_includes/Week%201/LNX/LNX-06_2%20PID.png)

How much memory is telnetd using?

![memory](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a3f357b5ca41920c1b095d1a96a9b688d102a060/00_includes/Week%201/LNX/LNX-06_3%20Memory.png)
