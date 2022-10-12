# SEC-06 Public Key Infrastructure
Studying Public Key Infrastructure (PKI).
#

## Key terminology
### Public Key Infrastructure (PKI)

### X.509 standard

## Exercise
- Created a self-signed certificate on my VM.
- Analyzed some certification paths from websites
- Finded all the list of trusted certificate roots on my systems

### Sources
https://www.youtube.com/watch?v=0ctat6RBrFo

https://linuxize.com/post/creating-a-self-signed-ssl-certificate/

https://www.globalsign.com/en/blog/how-to-view-ssl-certificate-details

https://support.apple.com/en-us/HT207189

https://support.nmi.com/hc/en-gb/articles/360021544791-How-to-Check-If-the-Correct-Certificates-Are-Installed-on-Linux

https://unix.stackexchange.com/questions/97244/list-all-available-ssl-ca-certificates

### Overcome challenges
Information and solutions were readily available on the interenet.

### Results
Created a self-signed certificate in my VM

![cer](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_02%20Create%20cer%20.png)

Output

![cerv](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_03%20View%20cer.png)
#

Analyzed some certification paths.
To do this, you can click on the lock icon in the address bar. This will bring up a menu where you can find all the information about the security certificate.

![b](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_04%20Tech.png)

Techgrounds

![b](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_05%20path%20alg.png)
![b](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_06%20path%20det.png)
#
Google

![b](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_07%20google%20alg.png)
![b](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_08%20google%20det.png)
#
ING

![b](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_09%20ing%20alg.png)
![b](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_10%20ing%20det.png)
#
I searched for the list of trusted certificate roots on my system and find it.

![b](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_11%20truststore.png)

![b](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_12%20list%20cer.png)

Also find it on my VM.

![b](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-06_13%20list%20cer%20VM.png)
