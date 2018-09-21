Writeup 3 - OSINT II, OpSec and RE
======

Name:
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Christina Benjamin

## Assignment 3 Writeup

### Part 1 (100 pts)

1) Fred used a weak server password.

Fred's password 'pokemon' was one of the passwords in rockyou.txt and was very easy to guess. Since hackers can use word lists or letter combinations to guess passwords, the more complex a password is, the less likely it is for this method to work. The strongest passwords will alternate upper and lowercase letters, symbols, and numbers; using this range of character types will raise the number of possible combinations to ~722 trillion and take approximately 83 days to crack using brute force verification, as opposed to a mere 35 minutes for passwords containing only lowercase letters (1 and 1). Chris Hoffman of How to Geek suggests using a password manager to randomly select a complex password and encrypt and store the data so that the user doesn't have to rely on their memory. According to a study done by Lyastani et al on the effectiveness of password managers, the tool is extremely effective because it eliminates the very common issues of overly simple passwords and password reuse. Various password managers offer different strengths; to name a few, Hoffman recommends Dashlane (versatile across platforms but keeps information local), LastPass (cloud-based and works across browsers and OS), and KeePass (good option for those who don't feel comfortable storing their passwords in a cloud.) 

2) Fred had an exposed port.

It was easy to find that port 1337 was open by searching Fred's IP address using Nmap. After that, using the given instructions, I was able to create socket connection using his IP address and the port number. Since 1337 is an uncommon port that's not typically used, this vulnerability could have been avoided by keeping the port closed so that a hacker cannot establish a connection. Tech Radar suggests keeping only "the bare minimum exposed," or keeping ports closed unless absolutely necessary, and using a firewall to close ports and prevent them from being opened by malicious software. A user can use a tool like Nmap to check the efficiency of their firewall and ensure that no unwanted ports are open.

3) Fred had no way of detecting or stopping the hacker once a connection was established.

Because Fred had no preventative measures in place, I was able to automate a continuous password attempt until the correct password was guessed. If the user had utilized intrusion detection software (IDS), the software could have easily picked up that the hack attempt was an anomaly from multiple incorrect password attempts, and used an intrusion prevention system to shut down the server after a certain number of incorrect attempts. One detection tool is called Brute Force Detection (BFD) and works by watching log files for multiple failed login attempts in a short amount of time, and blocking the IP address behind these attempts (Liquid Web). Although this measure would probably not be necessary if a strong password is being used, it's a good failsafe that should not have any impact on day-to-day usage.


Citations:
https://www.howtogeek.com/141500/why-you-should-use-a-password-manager-and-how-to-get-started/

https://arxiv.org/pdf/1712.08940.pdf

https://www.techradar.com/news/networking/how-to-secure-your-tcp-ip-ports-633089

https://www.1and1.com/digitalguide/server/security/brute-force-attack-definition-and-protective-measures/

https://www.liquidweb.com/kb/what-is-brute-force-detection-bfd/
