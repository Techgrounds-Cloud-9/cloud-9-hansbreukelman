# Sec-02 Firewalls
Gaining knowledge about everything related to Firewalls and how to apply it.

## Key terminology
## Firewalls
### Stateful firewalls

### Stateless firewalls

### Hardware firewalls

### Software firewalls

### CentOS

### REHL

### Firewalld

### UFW

### Iptables

## Exercise
- Viewing Apache's default page
- Using the UFW to block web traffic, but not ssh access. And check that this works as well.
#

### Sources
https://www.youtube.com/watch?v=kDEX1HXybrU

https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04

### Overcome challenges
Again, another fun assignment, only at first I got stuck reaching the default page of Apache (my VM's web server). Between the IP address and the port I had a 'dot' instead of a 'colon', this is why I couldn't get connected to the default page.

After installing the UFW(Firewall of the VM) and I had changed the settings. I still got connection to the default page. Which made me think I had changed the settings incorrectly, I only found out later that I only needed to refresh the browser.

### Results
![a]()

![a]()

![a]()

![a]()

![a]()

![a]()

![a]()

![a]()
