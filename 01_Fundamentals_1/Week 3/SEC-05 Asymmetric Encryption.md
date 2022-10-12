# SEC-05 Asymmetric Encryption
Learn all about Asymetric encryption and how to apply it.

## Key terminology
### Symmetric and asymmetric encryption

### A key pair generator

## Exercise
Applying the use of asymmetric encryption.

### Sources
https://cryptotools.net/dhe

https://www.tools4noobs.com/online_tools/encrypt/

https://generate-random.org/encryption-key-generator?count=1&bytes=32&cipher=des-cbc&string=&password=

https://www.devglan.com/online-tools/rsa-encryption-decryption

### Overcome challenges
It took a while to figure out if we were doing it the right way, but it all worked out in the end.

### Results
Generated a key pair

![gen](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-05_01%20Gen%20Key.png)

Preparing my message with my peer's public key

![d](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-05_02.png)

Now my peer puts my encrypted message in the decrypt column and combined with the peer's private key, he or she can make the message readable.

![e](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-05_03.png)
![e](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/bee2edf71099861cb9ecb7cdd8f503e4bace744b/00_includes/Week%203/SEC/SEC-05_04%20Message.png)