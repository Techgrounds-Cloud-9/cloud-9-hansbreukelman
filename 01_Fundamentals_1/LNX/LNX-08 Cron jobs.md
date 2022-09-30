# LNX-08 Cron jobs
Working with Bash scripts in combination with Cron jobs.

## Key terminology
### Cronjob
A Cronjob or crontab is a Unix command that runs a program or script at a set time.

### Bash script
Bash script is a plain text file which contains a series of commands.

### Var/log
This folder contains overall system notifications and messages recorded at system boot.

## Exercise
- Create a Bash script that writes the current date and time to a file in your home directory.
- Register the script in your crontab so that it runs every minute.
- Create a script that writes available disk space to a log file in ‘/var/logs’. Use a cron job so that it runs weekly.

### Sources
https://stackoverflow.com/questions/5265702/how-to-get-full-path-of-a-file

https://www.youtube.com/watch?v=v952m13p-b4

https://crontab.guru/every-1-minute

https://stackoverflow.com/questions/8395358/creating-a-file-in-a-specific-directory-using-bash

https://www.howtogeek.com/409611/how-to-view-free-disk-space-and-disk-usage-from-the-linux-terminal/#:~:text=Bash%20contains%20two%20useful%20commands,terminal%20window%20to%20get%20started

https://www.baeldung.com/linux/create-crontab-script

https://www.cyberciti.biz/faq/sudo-append-data-text-to-file-on-linux-unix-macos/

https://ostechnix.com/how-to-manually-add-messages-to-linux-system-log-files/

### Overcome challenges
This took me quite a long time, the first two exercises were solved fairly quickly. With the last one I unfortunately got stuck. I did not succeed in getting a passage to the Var/log, and to create a file in it. Finally after a lot of searching I found the solution.

### Results
Made a bash script that writes the current date and time in to a file in my home directory

![rt](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bdd9acdf38bfae7562a8091195530dd501cd02a5/00_includes/Week%201/LNX/LNX-08_1%20Script.png)

![hj](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bdd9acdf38bfae7562a8091195530dd501cd02a5/00_includes/Week%201/LNX/LNX-08_2%20Result.png)

Registerd the script in the crontab so that it runs every minute.

![hj](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bdd9acdf38bfae7562a8091195530dd501cd02a5/00_includes/Week%201/LNX/LNX-08_3%20Crontab.png)

![hj](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bdd9acdf38bfae7562a8091195530dd501cd02a5/00_includes/Week%201/LNX/LNX-08_4%20Crontab.png)

![hj](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bdd9acdf38bfae7562a8091195530dd501cd02a5/00_includes/Week%201/LNX/LNX-08_5%20Result.png)

Created a script that writes available disk space to a log file in ‘/var/logs’. Used a cron job so that it runs weekly.

![hj](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bdd9acdf38bfae7562a8091195530dd501cd02a5/00_includes/Week%201/LNX/LNX-08_6%20Script.png)

![hj](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bdd9acdf38bfae7562a8091195530dd501cd02a5/00_includes/Week%201/LNX/LNX-08_7%20Log.png)

![hj](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bdd9acdf38bfae7562a8091195530dd501cd02a5/00_includes/Week%201/LNX/LNX-08_8%20Crontab.png)