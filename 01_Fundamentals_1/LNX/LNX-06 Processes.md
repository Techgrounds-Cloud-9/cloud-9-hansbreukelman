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
### Sources
- Download and start Telnet Daemon
- Show the PID 
- Show how much memory Telnet uses
- Stop Telnet

### Overcome challenges
I still spent quite a long time trying to start Telnet, finding the right command was quite difficult. I found out after much searching that it was more with the name INETD and that allowed me to search more specifically.

### Results
Start Telnet

![start](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a3f357b5ca41920c1b095d1a96a9b688d102a060/00_includes/Week%201/LNX/LNX-06_1%20Start.png)

PID

![PID](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a3f357b5ca41920c1b095d1a96a9b688d102a060/00_includes/Week%201/LNX/LNX-06_2%20PID.png)

How much memory is telnetd using?

![memory](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a3f357b5ca41920c1b095d1a96a9b688d102a060/00_includes/Week%201/LNX/LNX-06_3%20Memory.png)