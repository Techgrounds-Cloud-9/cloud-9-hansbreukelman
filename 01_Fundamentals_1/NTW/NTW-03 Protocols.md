# NTW-03 Protocols
[Give a short summary of the subject matter.]

## Key terminology
### Network protocol
A network protocol is regulations that define how things are sent between different devices on the same network.

### UDP
The User Datagram Protocol (UDP) is one of the basic protocols of the Internet. The protocol operates at the same level as TCP. UDP is considered unreliable: the protocol does not check that the data is actually sent properly and arrives in the same order, which is the case with TCP.

### ‘Fire and forget’ strategy
Fundamentally UDP is a fire and forget protocol. You send a data packet to a target, and that's that!

### ‘Three-way handshake’
A three-way handshake establishes a reliable connection between client and server, and is vital for online communication.

![twh](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/da4b2c0fe0aa7415d99c43e2b36f5f16b190317e/00_includes/Week%202/NTW-03%20TWH.png)

### HTTPS
Https in full stands for Hyper Text Transfer Protocol Secure and, like http, is a way to send data over the Internet. But then in a secure way.

### Wireshark
Wireshark is a network protocol analyzer, or an application that captures packets from a network connection, such as from your computer to your home office or the internet.

### QUIC
QUIC (Quick UDP Internet Connections) is een nieuw transportprotocol voor het internet, ontwikkeld door Google.

## Exercise
- Looked up other protocols and the corresponding OSI layer. 

- Figured out what protocols we use and what it would take to implement a proprietary protocol.

- Downloaded and installed Wireshark. 
Captured my own network data. 
Picked a protocol and highlighted it.


### Sources
https://nl.wikipedia.org/wiki/User_Datagram_Protocol

https://www.redhat.com/architect/http3

https://www.geeksforgeeks.org/tcp-3-way-handshake-process/

https://www.youtube.com/watch?v=-rSqbgI7oZM&t=570s

https://docs.oracle.com/cd/E19683-01/806-4075/ipov-10/index.html

https://peering.google.com/#/learn-more/quic
#

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

### Results
Identify other protocols and their connection to OSI layers. 

![op](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/3a90497d22a999aee40f9bcbc0a22e1a19b1c30e/00_includes/Week%202/NTW-02%20Prot.png)

### What is needed to introduce your own protocol.
You can always create another protocol in your own network without having to depend on other authorities. 

To begin, it is helpful to have a foundation and start with OSI's 7 layers as a guideline. And from here look at what you want to improve to your standards. Apply these within your own network and test how this goes.

If you want it to be public and recognized so that other users of the Internet can use it, you will have to apply to various agencies to have it implemented. Including Internet Engineering Task Force (IETF) develop the maintain high quality relevant technical standards, mainly network protocols. The network protocol standards are developed under a platform, called as Request for Comments (RFCs).

### Understanding QUIC
What I understand from it is that QUIC is a protocol that is especially much associated with the use of Google Chrome. It is also realized by Google.

![go](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/40e29e992861fd8c4f4b9d01e74f32f817775416/00_includes/Week%202/NTW-03%20Cap.png)

The QUIC protocol also constantly communicates between my IP address and with an IP address originating from Google. 

![go](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/40e29e992861fd8c4f4b9d01e74f32f817775416/00_includes/Week%202/NTW-03%20QUIC.png)