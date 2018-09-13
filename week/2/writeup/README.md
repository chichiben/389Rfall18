Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Christina Benjamin
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Christina Benjamin

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2.
- Name / profile picture: Fred KruegerGoogled username in quotes & found his stwity website with a corresponding username.
- Location / Work / Twitter: Silver Spring, Cornerstone Airlines, @kruegster1990
Clicked his profile and was led to a personal biography page with a web client linked to his Twitter.
- Work website: www.cornerstoneairlines.co/
Found on twitter bio.
- Birth year: 1990
Searched his username on Twitter and found more information that the website didn't show.
- Interests: presumably in the UMD Cybersecurity Club, since they are following each other.
- Email: kruegster1990@tutanota.com
Listed in the 'About' section of the Cornerstone Airlines website.
Instagram: kruegster1990

3. I found  142.93.118.186 when looking at "whois" inside Centralops.

4. Found CMSC389R-{fly_th3_sk1es_w1th_u5} by navigating to /robots.txt, then navigating to /secret and inspecting the blank page.

5. IP address is 142.93.117.193; I clicked the 'Admin' tab, which led to a broken page. The IP address was listed in the address bar.

6. The associated server is located in New York; I searched the IP on ipinfo.io

7. Ubuntu-4ubuntu2.4; searched the IP address on Shodan

8.
Found CMSC389R-{h1dden_fl4g_in_s0urce} in source code of Cornerstone Airline's main page.
Found CMSC389R-{dns-txt-rec0rd-ftw} after searching host on DNS lookup.

### Part 2 (55 pts)

Since I already had the username @kruegster from the email on his website, I could use the given username and test it by iterating through all of the passwords in rockyou.txt until a password does not fail. Once I found the password pokemon and was in the server, I navigated to home and then flight_records. From the Instagram @kruegster1990 , I found the flight AAC27670 and opened the file to find the flag CMSC389R-{c0rn3rstone-air-27670}.
