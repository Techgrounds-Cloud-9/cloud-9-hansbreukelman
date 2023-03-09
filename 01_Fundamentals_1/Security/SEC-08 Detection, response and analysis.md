# **SEC-08 Detection, response and analysis**
[Give a short summary of the subject matter.]

## **Key terminology**
### Inbraakdetectiesystemen (IDS)

### Inbraakpreventiesystemen (IPS)

### Disaster recovery plan

### Business continuity plan

### Redundant site
In a redundant network, you use multiple connections. This can be a ring structure, for example, where data can be accessed both left and right. If one route then fails (for example, due to a break in the cable) then the network can still function via the other route.

### Recovery Point Objective; RPO

### Recovery Time Objective; RTO

### Automatic failover

## **Exercise**
## **Sources**
https://www.juniper.net/nl/nl/research-topics/what-is-ids-ips.html

https://www.techtarget.com/searchsecurity/feature/How-to-develop-a-data-breach-response-plan-5-steps

https://securityboulevard.com/2019/11/5-tips-for-responding-to-cyber-attacks/

https://www.vmware.com/topics/glossary/content/disaster-recovery-service-draas

https://cloudian.com/guides/disaster-recovery/understanding-disaster-recovery-in-the-cloud

https://www.techtarget.com/searchdisasterrecovery/definition/virtual-disaster-recovery

https://www.businesstechweekly.com/operational-efficiency/business-continuity/recovery-time-objective-rto-and-recovery-point-objective-rpo/

https://www.techopedia.com/definition/27075/automatic-failover
#

## **Overcome challenges**
[Give a short description of the challeges you encountered, and how you solved them.]

## **Results**
IDS is more for detecting a malware/hack. It observes a process performing something that is not good and then alerts when they are detected. 

IPS is for preventing a malware/hack from getting in at all. It blocks certain packets or incoming Internet traffic that the IPS system thinks is not good. It will prevent it to enter, it will report, block, or drop it, when it does occur. The downside to this is that it can also block traffic that may be good but the IPS system recognizes as not good, This can cause things to go wrong by, for example, certain software will not get its usual information or traffic needed to work. So as a result, certain software may not work.
#

### **Responding to Cyber Attacks**
1. Follow a communication plan.
Figuring out who to inform after a hacking attack is critical. What does the attack mean? Who should you tell? How do you tell them? When do you tell them? Implement a communication plan before the hacking attack occurs to carry it out once the attack takes place. 

2. Secure IT systems.
As soon as you realize the breach, secure your IT systems to limit the scope of the attack. 

3. Launch backups.
Hopefully, you’ve developed a good crash plan for your website. Now is the time to launch that crash plan and deploy your backups to protect your data from further harm. 

4. Notify authorities.
Let the authorities know about the cyber attack on your organization. This will help protect your customers and make a record of the attack so that authorities can respond. 

5. Create redundancy in your data.
This is a critical part of data security and protecting your assets. Data redundancy is a condition created within a database or data storage technology where the same piece of data is held in two separate places.
#

### **Systems hardening**
Systems hardening is a collection of tools, techniques, and best practices to reduce vulnerability in technology applications, systems, infrastructure, firmware, and other areas. The goal of systems hardening is to reduce security risk by eliminating potential attack vector s and condensing the system's attack surface.
#

### **Types of disaster recovery options**
Disaster recovery is a collection of measures, tools and procedures for the restoration or continuation of technological infrastructure and systems after a natural or man-made disaster. Disaster recovery focuses on the information technology (IT) or technological systems that support critical business functions, as opposed to business continuity.

Types DR:
- **Data center disaster recovery**
Data Center Disaster Recovery is the organizational planning to resume business operations following an unexpected event which may damage or destroy data, software and hardware systems.

- **Network disaster recovery.**
  A network disaster recovery plan is a set of procedures designed to prepare an organization to respond to an interruption of network services during a natural or manmade catastrophe. Voice, data, internet access and other network services often share the same network resources.

- **Virtualized disaster recovery.**
  Virtual disaster recovery is a type of DR that typically involves replication and allows a user to fail over to virtualized workloads. For the most efficient virtual disaster recovery, an organization should copy virtual machine (VM) workloads off-site on a regular basis.

- **Cloud disaster recovery.**
  The term cloud disaster recovery (cloud DR) refers to the strategies and services enterprises apply for the purpose of backing up applications, resources, and data into a cloud environment. Cloud DR helps protect corporate resources and ensure business continuity.

- **Disaster recovery as a service (DRaaS)**
  Disaster recovery as a service(DRaaS) is a cloud computing service model that allows an organization to back up its data and IT infrastructure in a third party cloud computing environment and provide all the DR orchestration, all through a SaaS solution, to regain access and functionality to IT infrastructure after a disaster.
#
### **Result Exercise 1**
The Recovery Point Objective of the database is 24 hours. Because they backup daily, the recovery point is 24 hours.

### **Result Exercise 2**
The procestime from the disaster/failure till recovery was 8 min. So in that case the RTO is 8 min.
