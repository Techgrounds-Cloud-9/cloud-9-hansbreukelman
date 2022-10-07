# NTW-02 Network Devices
[Give a short summary of the subject matter.]

## Key terminology
### Hub
The central part of a wheel. A HUB can allow multiple devices on the same LAN connection to communicate with each other. What it receives from one device to be transmitted, it sends to all devices connected to it. This without checking what the specific destination is.

### Switch
Switches generally have a more intelligent role than hubs. A switch is a multiport device that improves network efficiency. It is basically the same as the HUB, only unlike the HUB, it is capable of sending certain messages/commands to a specific receiver.

### Router
Routers are general-purpose devices that interconnect two or more of different origins networks.
Each router interface has its own Address Resolution Protocol (ARP) module, its own LAN address (network card address) and its own Internet Protocol (IP) address.

### Bridge
Bridges are used to connect two or more hosts or network segments together. The basic role of bridges in network architecture is storing and forwarding frames between the different segments that the bridge connects.

### Gateway
Gateways normally work at the Transport and Session layers of the OSI model. At the Transport layer and above, there are numerous protocols and standards from different vendors; gateways are used to deal with them. 

### Modem
Modems (modulators-demodulators) are used to transmit digital signals over analog telephone lines. Thus, digital signals are converted by the modem into analog signals of different frequencies and transmitted to a modem at the receiving location.

### Repeater
A repeater is an electronic device that amplifies the signal it receives. You can think of repeater as a device which receives a signal and retransmits it at a higher level or higher power so that the signal can cover longer distances, more than 100 meters for standard LAN cables. Repeaters work on the Physical layer.

### Access Point
While an access point (AP) can technically involve either a wired or wireless connection, it commonly means a wireless device. An AP works at the second OSI layer, the Data Link layer, and it can operate either as a bridge connecting a standard wired network to wireless devices or as a router passing data transmissions from one access point to another.

## Exercise
### Sources
Everything about networking
https://www.youtube.com/watch?v=S7MNX_UD7vY&list=RDCMUC9x0AN7BWHpCDHSm9NiJFJQ&index=2

Network devices
https://blog.netwrix.com/2019/01/08/network-devices-explained/

https://www.techtarget.com/searchnetworking/tip/An-introduction-to-8-types-of-network-devices

https://www.youtube.com/watch?v=9eH16Fxeb9o&list=RDCMUC9x0AN7BWHpCDHSm9NiJFJQ&index=3

https://en.wikiversity.org/wiki/Network%2B/Standards/OSI_Model/OSI_Components

### Overcome challenges
Since I didn't have access to a router myself, I asked Jeena to help me in another breakout room. With the information/solutions I had gathered myself, we went through all the steps with her screen.

### Results
The OSI model in relation to these network devices

![new](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/19a751ba531b0ed56e62f64454694661e2c0cf67/00_includes/Week%202/NTW-02%20OSI%20model%20dev.png)

First, I figured out what the IP address is by going to the command prompt, entering "ipconfig" here. The numbers indicated on the Default Gateway section is your router's IP Address.

The ip address of the router, I copy and paste into an Internet browser. This leads me to the routers management page. Here, under the connected devices tab, I can see which devices are connected to the router

![ret](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/e7848e7673253fb910491ffab6b7d7d5db62bd7e/00_includes/Week%202/NTW-02%20Con%20dev.png)

To see where the DHCP server is on my network and what its configurations are, I enter "configip/all in the command prompt.

![gt](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/e7848e7673253fb910491ffab6b7d7d5db62bd7e/00_includes/Week%202/NTW-02%20DHCP.png)

