# NTW-06 Subnetting
Delving into subnets and creating networks. And realizing an outlined network architecture. 
#

## Key terminology
### LAN
'Local Area Network', a LAN cable is the connection between computers, printers, switches, etc. creating a network (LAN).

### Subnet
A subnet is a subnet in a network, operating according to the Internet Protocol. The verb subnets means dividing a set of consecutive IP addresses (an IP range) for addressing on separate physical networks.

### Subnet mask
A subnet mask is a 32-bit number created by setting host bits to all 0s and setting network bits to all 1s.

### CIDR
CIDR is the short for Classless Inter-Domain Routing, an IP addressing scheme that replaces the older system based on classes A, B, and C. A single IP address can be used to designate many unique IP addresses with CIDR.

### Broadcast address
A broadcast address is a network address used to transmit to all devices connected to a multiple-access communications network.

## Exercise
Create a network architecture in the form of a diagram. 

### Sources
https://www.subnet-calculator.com/

https://app.diagrams.net/

https://www.youtube.com/c/PracticalNetworking
#

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

## Results
### Explaining Subnetting
Since the number of desired hosts/ip addresses is 50, I look and select on the cheat sheet which group size is most appropriate for this. Here I end up with 64. From here I see which numbers below are associated with this.

![CS](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/5f5c8738f43204d83ffb3a2a9e60022798b1f649/00_includes/Week%202/NTW-06%20Cheatsheet.png)

For the subnet I come up with 192. So my subnet mask number ends at 192. This is then 255.255.255.192
The CIDR number is 26

For the first host IP address (the IP address after the first IP address or Network ID) very simply count 1 above the network ID. The first host IP address is then 192.168.72.1

To determine what the broadcast address is, subtract 1 from the next network. The next network address is 192.168.72.64 minus 1 = 192.168.72.63 = broadcast address. Now we can also determine what the address is for the last host. Namely, this is the broadcast addres minus 1. The address for the last host is then 192.168.72.62

To determine the addresses on the following networks, each time counting from the next network address.

![dia](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/56d4be96e8f8089801830c8bd0f0b6160ca4ef8e/00_includes/Week%202/NTW-06%20Diagram.png)

