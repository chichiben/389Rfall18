Writeup 9 - Crypto I
=====

Name: Christina Benjamin
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Christina Benjamin

## Assignment 9 Writeup

### Part 1 (60 Pts)
The goal for part 1 was to use a password list and given salts and hashing algorithm in order to identify hashed passwords. Using the given hashes, my method was to hash the password list using the different salts and compare it with the hashed passwords to identify which passwords in the wordlist are being used. To do this, I looped through each of the salts (every letter of the alphabet) and then looped through each password in the wordlist. For each password, I stripped any whitespace, prepended the salt, and then hashed the new word with SHA512 algorithm as specified in the README. Then I checked if that hash was equal to any of the hashes in the given hash list, and printed the salted password and hash if they matched. At first, I ran into some issues with stripping, so I wrote the results of the hashes into a file and continued tweaking the code until I found the matches I needed.

Matching Hashes / Salted Passwords:
9a23df618219099dae46ccb917fbc42ddf1bcf80583ec980d95eaab4ebee49c7a6e1bac13882cf5dd8d3850c137fdff378e53810e98f7e9508ca8516e883458e
kneptune
c35eb97205dd1c1a251ad9ea824c384e5d0668899ce7fbf269f99f6457bd06055440fba178593b1f9d4bfbc7e968d48709bc03e7ff57056230a79bc6b85d92c8
mjordan
70a2fc11b142c8974c10a8935b218186e9ecdad4d1c4f28ec2e91553bd60cfff2cc9b5be07e206a2dae3906b75c83062e1afe28ebe0748a214307bcb03ad116f
ppizza
d39d933d91c3e4455beb4add6de0a48dafcf9cb7acd23e3c066542161dcc8a719cbac9ae1eb7c9e71a7530400795f574bd55df17a2d496089cd70f8ae34bf267
uloveyou

### Part 2 (40 Pts)
The goal for part 2 was to create a script that would continuously answer the trivia questions until a flag was reached. After running nc 142.93.117.193 7331 a few times, I could see that the trivia questions were always in the format: "Find me the [hashing algorithm] hash of [string]". I wrote my script to create a socket connection with the given IP and port, and first read in the welcome script, then match the hashing algorithm requested. Next, I pulled out and trimmed the string that needed to be hashed, hashed it according to the given algorithm, and sent it back into the socket. Finally, I pulled out the following string that indicated the correctness of the user answer. I continued to loop through this until I reached the flag: CMSC389R-{H4sh-5l!ngInG-h@sH3r}
