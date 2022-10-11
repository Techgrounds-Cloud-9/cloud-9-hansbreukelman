# SEC-04 Symmetric Encryption
[Give a short summary of the subject matter.]

## Key terminology
### Encryption

### Cryptography

### Ciphers

## Exercise
### Sources
https://www.youtube.com/watch?v=KXq065YrpiU

https://www.theguardian.com/childrens-books-site/2015/sep/10/top-10-codes-keys-and-ciphers

https://cryptii.com/pipes/caesar-cipher

https://www.tcsion.com/OnlineAssessment/ScientificCalculator/Calculator.html#nogo

https://cryptotools.net/dhe

https://www.tools4noobs.com/online_tools/encrypt/

https://generate-random.org/encryption-key-generator?count=1&bytes=32&cipher=des-cbc&string=&password=

https://www.devglan.com/online-tools/rsa-encryption-decryption

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

## Results
### Historic ciphers
### Alberti's disk
The Alberti cipher, created in 1467 by Italian architect Leon Battista Alberti, was one of the first polyalphabetic ciphers.

The process of encrypting into the Alberti cipher is simplified by Alberti's discs. On the inner disc was a mark which could be lined up with a letter on the outer disc as a key, so that if you wanted to encrypt or decrypt a message you only needed to know the correct letter to match the mark to.
#

### Egyptian hieroglyphics

The first encrypted messages were developed in ancient Egypt as series of disordered hieroglyphics. This means of encryption was very simple, utilizing a method called simple substitution. The original message, or plaintext, was encoded using a substitution cipher (a cipher is a method of encryption)

Egyptian hieroglyphics constitute the script of ancient Egypt. By the Egyptians themselves, they were called Medu Netjer or "Divine Words," referring to the lore that the god Thoth once gave writing to the Egyptians.
#

### Digital ciphers that are being used today
### - Triple DES
3DES, pronounced "triple DES," is an encryption algorithm. It uses the now considered crackable Data Encryption Standard or DES algorithm for short, but in such a way that it is much harder to crack.

### - AES
In cryptography, Advanced Encryption Standard is a computer encryption technique. It is the successor to the "Data Encryption Standard." AES is a subset of the Rijndael algorithm where the block size is 128 bits, and the key is 128, 192 or 256 bits.

### - Blowfish
Blowfish is een door Bruce Schneier ontwikkeld versleutelingsalgoritme. Het is voor het eerst gepubliceerd in 1993. Blowfish is een symmetrische blokversleutelingstechniek, die met sleutellengtes van 32 tot 448 bits overweg kan. Blowfish is een krachtig algoritme.
#

### Symmetrically encrypted message
For symmetric encryption, I used the the Caesar cipher combined with Diffie-Hellman method as a key. 

The key in this is the number that comes out of the encryption from the Diffie-Hellman method. 

The number that comes out of this can be used to determine how much is shifted in the Caesar cipher.

Once the number is determined then each individual can begin encrypting his or her message. 

To determine a number for shifting the Caesar figure, I and Jeena for the Diffie-Hellman method have a prime number and a generic number, these two are not private or secret and can be shared. 

Prime number = 13
Generic number = 6

In addition, we both chose a private number for ourselves. These are secret though.
But to generate a public key, we use the private number, the prime number and the generic number. 

My private number is 9

The math then looks like this:

(6^9) mod 13 = 5 

My public number is 5
I share this with Jeena so that she can arrive at our common private number using the same arithmetic. I can then do the same with her public number. Jeena's public number is 7

![pk](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/2e627ad2b087264e4a938635405af6896126b461/00_includes/Week%203/SEC/SEC-04%20Exchange%20Public.png)

The arithmetic I have to do then looks like this:

(7^9) mod 13 = 8

8 is our shared private number (private key) This is the number of shifts to be made in the Caesar cipher. 

![prk](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/2e627ad2b087264e4a938635405af6896126b461/00_includes/Week%203/SEC/SEC-04%20CC.png)

![res](https://github.com/Techgrounds-Cloud-9/cloud-9-hansbreukelman/blob/2e627ad2b087264e4a938635405af6896126b461/00_includes/Week%203/SEC/SEC-04%20Result.png)




