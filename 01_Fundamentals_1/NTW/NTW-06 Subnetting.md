# NTW-06 Subnetting
[Give a short summary of the subject matter.]

## Key terminology
[Write a list of key terminology with a short description. To prevent duplication you can reference to previous excercises.]

## Exercise
### Sources
https://www.subnet-calculator.com/

https://app.diagrams.net/

https://www.youtube.com/c/PracticalNetworking

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

