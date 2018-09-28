Writeup 3 - Pentesting I
======

Name: Christina Benjamin
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Christina Benjamin

## Assignment 4 Writeup

### Part 1 (45 pts)

I found the flag: CMSC389R-{p1ng_as_a_$erv1c3} inside home/flag.txt, using the command ping 142.93.118.186; cat home/flag.txt. My initial approach to this problem was to attempt to test a few random commands to see what would happen. I saw pretty quickly that passing a normal IP as requested simply ended the program, and that the program consistently took one input and then ended. Random commands also resulted in the program ending. From the prompt, I knew that Fred is utilizing the ping command, so I tried sending the ping command with a semicolon and another command tagged directly after. With this method, the input would read the valid portion (the ping command and IP) and then continue running the following command. From here, I continued entering commands appended by the ping and fake IP to look at directories and navigate to the home folder. Once I'd found the path of flag.txt, I used cat to open the file. Using the same method, I discovered the script in the opt folder. As stated in the prompt, Fred's goal for this server was to test the uptime of Internet-connected devices in his company's network; since in general, an option for user input introduces a wide range of vulnerabilities, the security of eliminating the user input seems to outweigh the benefit of a more usable interface. If user input is absolutely necessary, Fred should implement input validation on his code to weed out any faulty or malicious commands. After finding the script, I could see that Fred is using "ping -w 5 -c 2 $input" as his input. If he had used input validation like regex on his command to ensure that the user was entering ping, a valid IP address, and nothing after, then his system would be more robust in addition to being more secure. 

### Part 2 (55 pts)

In stub.py, I implemented a shell with a few basic commands, including the option to drop into an interactive shell inside of Fred's server. The 'outer' shell implements four basic commands: 
1) shell: all commands entered after this command, and until 'exit' is entered, will be sent to Fred's server and any resulting output will be printed as if the user is in Fred's terminal. 
2) pull [remote_path] [local_path]: any data inside of the file at remote_path will be written or overwritten into the file at local_path. 
3) help: a help menu describing the four commands will be printed.
4) quit: the user will exit the shell. 

If the user's input is not one of these four commands, or if the pull command is not followed by two elements, an error message will be printed.

When the user first enters the interactive shell, their path begins at '\', or the parent directory. My program implements the illusion of navigating through Fred's directories by continuously updating this path whenever a cd command is implemented. If the cd command is isolated, the program resets the path to the parent directory. If there is another argument after, it concatenates this path to the current path, and otherwise, it prints an error message. The program sends the cd command regardless of what command the user sends in order to ensure that the program is always located in the user's last current directory; for the same reason, path updates always occur after the command has been written. The rest of the shell portion opens a socket and reads the cornerstone logo out, sends the command in, and then reads and prints any output before closing the socket. 

The pull command works very similarly; it delimits the user's input by spaces and sends a cat command to the remote path after opening a socket connection. Rather than printing the received data as in the shell, this function writes it into the local path file before closing both the file and the socket. 
