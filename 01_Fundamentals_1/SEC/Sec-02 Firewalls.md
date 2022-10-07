# Sec-02 Firewalls
Gaining knowledge about everything related to Firewalls and how to apply it.
#

## Key terminology
## Firewalls
### Stateless firewalls
The simplest firewall. This type of firewall checks only the outside of a packet. It only looks at the source IP address or port number, destination IP address or port number and the protocol number. Depending on what the user has set, it can deny certain messages, packets or other traffic based on that. Because it is the most simplistic it is also the lightest type of firewall, so it uses less working memory than any other type of firewall.

### Stateful firewalls
Stateful firewalls are actually the opposite of a stateless type of firewall. These do monitor all aspects of network traffic. They also intercept packets at the network layer and then extract and analyze data from all communication layers to improve security. Connection status information and other contextual data are stored and dynamically updated.

### Hardware firewalls
A hardware firewall is a physical device that acts as a router. It inspects data before sending it onto the network. They do have drawbacks: attacks can happen from within and they cannot always handle multiple connections at once.

### Software firewalls
A software firewall is a firewall in the form of an application that runs on a computer. Which then protects against attacks inside the network or directly from the Internet.

### CentOS
CentOS (The Community Enterprise Operating System) is een Linuxdistributie voor serversystemen. Tot en met CentOS 8 was CentOS een open-source en volledig gratis rebuild van het betaalde Red Hat Enterprise Linux (RHEL), maar Red Hat gaat zich nu met 'CentOS Stream' richten op een upstream ontwikkelplatform die voorop lopen op de stabiele releases van RHEL.

### REHL
Red Hat Enterprise Linux (RHEL) is een Linuxdistributie voor professioneel gebruik. De commerciële distributie wordt geleverd door Red Hat. RHEL is de officiële afstammeling van een van de eerste Linuxdistributies, Red Hat Linux. De oudste formele versie van Red Hat Linux dateert van 3 november 1993.

### Firewalld
Firewalld provides a dynamically managed firewall with support for network/firewall zones that define the trust level of network connections or interfaces.

### UFW
UFW, or the Uncomplicated Firewall is a commonly used firewall in Debian and Ubuntu. UFW is a management layer / frontend for iptables that aims to make managing your firewall easier. Connect via SSH / the vps console and use a root user, or sudo when running the commands in this article.
#

## Exercise
- Viewing Apache's default page
- Using the UFW to block web traffic, but not ssh access. And check that this works as well.
#

### Sources
https://www.youtube.com/watch?v=kDEX1HXybrU

https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04
#

### Overcome challenges
Again, another fun assignment, only at first I got stuck reaching the default page of Apache (my VM's web server). Between the IP address and the port I had a 'dot' instead of a 'colon', this is why I couldn't get connected to the default page.

After installing the UFW(Firewall of the VM) and I had changed the settings. I still got connection to the default page. Which made me think I had changed the settings incorrectly, I only found out later that I only needed to refresh the browser.
#

### Results
See if Apache is still present

![a](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/6983c7b94f38f14e1cd6f8b0b1ecb295f4563946/00_includes/Week%202/SEC/SEC-02_01%20Apache.png)

Viewing the status of Apache

![a](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/6983c7b94f38f14e1cd6f8b0b1ecb295f4563946/00_includes/Week%202/SEC/SEC-02_02%20Stat%20Apa.png)

Apache's default page

![a](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/6983c7b94f38f14e1cd6f8b0b1ecb295f4563946/00_includes/Week%202/SEC/SEC-02_03%20Default.png)

Installing UFW

![a](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/6983c7b94f38f14e1cd6f8b0b1ecb295f4563946/00_includes/Week%202/SEC/SEC-02_04%20Inst%20UFW.png)

Allow ssh and deny internet traffic

![a](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/6983c7b94f38f14e1cd6f8b0b1ecb295f4563946/00_includes/Week%202/SEC/SEC-02_05%20Allow%20deny.png)

Viewing the UFW status

![a](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/6983c7b94f38f14e1cd6f8b0b1ecb295f4563946/00_includes/Week%202/SEC/SEC-02_06%20Status.png)

Result of changes

![a](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/6983c7b94f38f14e1cd6f8b0b1ecb295f4563946/00_includes/Week%202/SEC/SEC-02_07%20Denied.png)
