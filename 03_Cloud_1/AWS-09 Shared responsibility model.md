# AWS-09 Shared responsibility model
Studying the AWS Shared Responsibility Model.

## Key terminology
[Write a list of key terminology with a short description. To prevent duplication you can reference to previous excercises.]

## Exercise
### Sources
[List the sources you used for solving the exercise]

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

## Results
### **Shared Responsibility Model**
Is a model that shows who is responsible for what. Broadly speaking, AWS is responsible for security "OF" the Cloud and the customer is responsible for security "IN" the Cloud.

Better explained, anything where configurations and personal adjustments are involved in security, the responsibility then lies with the customer. Everything in which these configurations and customizations are possible there AWS is responsible for(Framework).
#
### **Shared Responsibility Model**
| Customer||
| ----------- | ----------- |
|Responsible for everything **'IN'** the Cloud||
| Customer Data ||
| Platform, applications, identity & acces management| |
| Operating systems, network, firewall coniguration| |
| Client side data, encryption & data intergrity, authentication | Server side encryption, file system and/or data|
|Networking traffic protection, encryption, intergrity, identity| |
#
| AWS|||
| ----------- | ----------- | ----------- |
|Responsible for everything **'OF'** the Cloud|||
| Software |||
| Compute, storage, data-base, networking| ||
| Hardware, AWS global infrastructure| ||
| Regions|Availibility Zone's| Edge Locations|
