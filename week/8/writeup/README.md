Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Christina Benjamin
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Christina Benjamin

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. I looked through the ICMP protocol that was marked as "Destination Unreachable" and checked the IP addresses in a reverse DNS lookup until I found the domain: http://csec-vip.umiacs.umd.edu/

2. I found the names by following the TCP stream and looking through the streams until I found a chat room conversation between the two hackers: c0uchpot4doz and laz0rh4x

3. I used the same chat room to find their IP addresses. There was a server IP address between the two IP addresses, so I factored that out and found the hackers' addresses to be: 104.248.224.85 and 206.189.113.189

4. The port associated with the server IP address mentioned above was 2749

5. They mentioned their plans in the chatroom; since the date of the capture on Wireshark is October 24th, "tomorrow at 15:00" would be October 25th at 15:00.

6. In the chat room: https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

7. They mentioned seeing each other tomorrow; October 25th.

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. My data for the timestamp was ﻿1540428007. I put it into an Epoch time converter and the result was: Thursday, October 25, 2018 12:40:07 AM GMT

2. laz0rh4x

3. It says it has 9, but there are 11 sections.

4.
TYPE: SECTION_ASCII
['Call this number to get your flag: (422) 537 - 7946']
TYPE: SECTION_WORDS
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
TYPE: SECTION_COORD
[38.99161, -77.02754]
TYPE: SECTION_REFERENCE
[1]
TYPE: SECTION_ASCII
['The imfamous security pr0s at CMSC389R will never find this!']
TYPE: SECTION_ASCII
['The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}']
TYPE: SECTION_COORD
[38.9910941, -76.9328019]
TYPE: SECTION_PNG
[0]
TYPE: SECTION_ASCII
['AF(saSAdf1AD)Snz**asd1']
TYPE: SECTION_ASCII
['Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9\n']
TYPE: 0x2
[4, 8, 15, 16, 23, 42]

5. In order to open the PNG file, I packed the magic bytes of a PNG file back into the data that I had unpacked so far for the PNG file, and then read that into a new file in the directory. The flag inside the photo was: CMSC389R - {c0rnerst0ne_airlin3s_to_the_m00n}
