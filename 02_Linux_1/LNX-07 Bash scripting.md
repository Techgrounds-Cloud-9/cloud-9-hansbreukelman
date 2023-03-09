# LNX-07 Bash scripting
Using scripts, Variables and conditions.

## Key terminology
### Bash shell
Bash, which stands for Bourne Again Shell, is a shell for POSIX systems and is used on Linux and macOS.

### Bash Script
A bash script is a series of commands written in a file. These are read and executed by the bash program. The program executes line by line.

### Variables
A variable is a character string to which we assign a value. The value assigned could be a number, text, filename, device, or any other type of data.

### Conditions
Conditional expressions always evaluate to true or false which is represented by 0 and 1, respectively.

### Loops
The for loop operates on lists of items. It repeats a set of commands for every item in a list.

### Httpd
Hypertext Transfer Protocol daemon, is an HTTP server daemon produced by the Apache Foundation.
#

## Exercises
### Exerxise 1
- Making a new directory
- Add the directory to the path
- Create multible scripts with different actions

### Exercise 2
- Create a script with a variable

### Exercise 3
- Create a script with a variable and also with a if statment directing to a textfile.
#

### Sources
https://linuxize.com/post/how-to-add-directory-to-path-in-linux/

https://www.youtube.com/watch?v=SPwyp2NG-bE

https://youtu.be/l9YxTXDiiFY

https://linuxhint.com/generate-random-number-bash/#:~:text=The%20random%20number%20or%20a,RANDOM%20with%20a%20specific%20value.

https://medium.com/@ertorrez/use-a-script-to-install-and-launch-an-apache-server-on-centos-8-6db6e4b81cbf 

https://www.w3schools.com/js/js_if_else.asp

https://www.w3schools.com/python/python_conditions.asp

https://www.tutorialspoint.com/unix/if-else-statement.htm


### Overcome challenges
This was a big assignment with many exercises. In some exercises, there were sometimes multiple options. I did enjoy the assignment, which did make me work on it longer than necessary. This was because I was trying out a lot of things.  

### Results
Making a new directory and put in path

![dir](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a295c25c72b466d9028873a042e88dd8e30c38e7/00_includes/Week%201/LNX/LNX-07-Ex1_1%20Scripts.png)

Created a script that appends a line of text to a text file whenever it is executed

![er](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a295c25c72b466d9028873a042e88dd8e30c38e7/00_includes/Week%201/LNX/LNX-07-Ex1_2%20Path.png)

Created a script that installs the httpd package, activates httpd, and enables httpd. Finally, the script print the status of httpd in the terminal.

![tr](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a295c25c72b466d9028873a042e88dd8e30c38e7/00_includes/Week%201/LNX/LNX-07-Ex1_3%20Httpd.png)

![tr](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a295c25c72b466d9028873a042e88dd8e30c38e7/00_includes/Week%201/LNX/LNX-07-Ex1_4%20Status.png)

Created a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file.

![yu](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a295c25c72b466d9028873a042e88dd8e30c38e7/00_includes/Week%201/LNX/LNX-07-Ex2_1%20Script.png)

![bn](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a295c25c72b466d9028873a042e88dd8e30c38e7/00_includes/Week%201/LNX/LNX-07-Ex2_2%20Result.png)

Created a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it append a line of text to that same text file instead.

![ty](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a295c25c72b466d9028873a042e88dd8e30c38e7/00_includes/Week%201/LNX/LNX-07-Ex3_1%20Script.png)

![kl](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/a295c25c72b466d9028873a042e88dd8e30c38e7/00_includes/Week%201/LNX/LNX-07-Ex3_2%20Result.jpeg)
