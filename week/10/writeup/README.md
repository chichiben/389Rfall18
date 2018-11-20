Writeup 10 - Crypto II
=====

Name: Christina Benjamin
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Christina Benjamin

## Assignment 10 Writeup

### Part 1 (70 Pts)
For part 1, I had access to a digital notary that could generate signatures or test the validity of a signature. I was given the information that a new secret would be generated for every new signature, but the secret would stay the same between validity tests. My first step was to open a socket connection with the notary so that I could send in a message and receive its valid signature, containing the encoded secret. The stub code then initialized an MD5 hash object with the legitimate hash that I had received from the server. Since this hash object contains the secret that will be used to test signatures, we can append a malicious message to the end of it and obtain its hexdigest in order to craft a "valid" signature. The second step was to guess the amount of padding needed to align the block, knowing that the secret is between 6-15 bytes long. Since the secret does not change between validity tests, I could loop through each of the lengths between 6-15 bytes and check if each one resulted in a valid signature. For each length, we know that an MD5 block is 64 bytes long with 8 of these bytes allocated for the length of the secret and message, leaving 56 bytes for the secret, message, and padding. Within the loop, I subtracted the respective length of each secret and constant length of the message from the 56 bytes allocated, and then crafted padding with the remaining bytes: one byte of 1 and remainder bytes of 0s. Then I encoded the length of the respective secret + message in little endian, and concatenated it to the end of the padding. The final payload consisted of the message, padding, and malicious message. By sending the fake hash from part 1 and the payload from part 2 into the notary's signature validity test, I could check if I was able to construct a 'valid' signature without knowing the secret. Eventually, after a few loops, I received the flag and message: CMSC389R-{i_still_put_the_M_between_the_DV} Made in Maryland - Substantial.

### Part 2 (30 Pts)
The relevant commands were:
- generating keys: gpg --gen-key
- importing someone else's public key: gpg --import pgpassignment.key
- encrypting a message for someone else and dumping it into a file: echo "message" | gpg -ear "president@csec.umiacs.umd.edu" > message.private
- listing out public keys: gpg --list-keys
- decrypting a message: --decrypt message.private

For this exercise, I first generated my own private/public key pair to test the encryption command. Once I saw that the message was correctly encrypted and decrypted, I imported the public key given in github, listed the keys to grab the email address as an identifier, and encrypted the message with the email address and outputted to the filename message.private. 
