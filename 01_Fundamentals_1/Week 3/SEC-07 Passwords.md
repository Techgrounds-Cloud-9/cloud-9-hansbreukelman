# SEC-07 Passwords
[Give a short summary of the subject matter.]

## Key terminology
[Write a list of key terminology with a short description. To prevent duplication you can reference to previous excercises.]

## Exercise
### Sources
https://www.cybercrimeinfo.nl/van-a-tot-z/
hashing

https://www.beyondidentity.com/glossary/rainbow-table-attack

https://www.youtube.com/watch?v=b4b8ktEV4Bg

https://www.youtube.com/watch?v=GI790E1JMgw

https://www.youtube.com/watch?v=SOV0AeHuHaQ

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

## Results
Hashing is usually used to ensure the integrity of data, primarily when we’re storing large amounts of it, while encryption is aimed more at protecting the privacy of small amounts of data while in transit;

Hashing is one-way, while encryption is two-way. Encryption turns plain text into ciphertext, which is unreadable, but you can decrypt it with a relevant key. Hashing scrambles a plain text into a unique encoded hash unit, which can't be reverted into a readable form.

### Rainbow Table
A rainbow table attack is a password cracking method that uses a special table (a “rainbow table”) to crack the password hashes in a database. Applications don’t store passwords in plaintext, but instead encrypt passwords using hashes. After the user enters their password to login, it is converted to hashes, and the result is compared with the stored hashes on the server to look for a match. If they match, the user is authenticated and able to login to the application. 

The rainbow table itself refers to a precomputed table that contains the password hash value for each plain text character used during the authentication process. If hackers gain access to the list of password hashes, they can crack all passwords very quickly with a rainbow table.

Hackers must first gain access to leaked hashes in order to carry out rainbow table attacks. The password database itself might be poorly secured, or they may have gained access to the Active Directory. Others gain access through phishing techniques of those that might have access to the password database. On top of all these techniques, there are already millions and millions of leaked password hashes on the dark web that are available to hackers. 

Once they have the password hashes the rainbow table is used to help decrypt the password hashes. As long as the password hashes don't include a “salt,” (explained above) they’ll be able to translate the encrypted passwords into plaintext easily.