Writeup 5 - Binaries I
======

Name: Christina Benjamin
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Christina Benjamin

## Assignment 5 Writeup

*Put your writeup words here in accordance to the Part 3 requirements*
I approached the my_memset function by looking at the C code and breaking down the problem into smaller steps. I could see that I was going to need to know which registers the parameters would be located in, how to loop, and how to access and store strings in array elements. I followed the assignment suggestion of using the loop modifier and googled usage cases to better understand the syntax. Initially, my code for this portion ran into an error "invalid size for operand 1" because I used the ecx register as was done in the documentation; I realized that since we were using 64-bit assembly, I would need to use the rcx register in order to resolve this error message. Since the loop modifier sets the upper limit of the counter, I knew that I would need a separate index to traverse the array from element 0. Since the rcx "counter" register was already in use, I used the rax register to act as an index. The slides specified that the three parameter variables would be read into rdi, rsi, and rdx, so I would need to read the value inside of rsi (corresponding to char val) into each element of rdi (corresponding to char *str). Since each char is equal to one byte, I used "mov byte" to move the rsi register into "rdi+rax", or the register corresponding to "char *str" plus the offset needed to fill each element of the array. I realized after another "invalid size" error that this command was attempting to move the entire 64-bit register rsi into the single byte allotted for the array element. To fix this error, I changed "rsi" to "sil" in order to access only the lowest 8 bits of the register.

The strncpy function was very similar, so I copied over the main structure of the loop and indexing from the memset function. The main difference between these two functions was that I would need to set the str array to another array, rather than a single char variable. Initially, I tried to use the same command as the memset function: mov byte [rdi+rax], [rsi+rax]. However, I received the error "invalid combination of opcode and operands." I decided to try pulling the data out of the rsi register and into the 8-bit register bl, and then moving the data in bl to the appropriate index in the rdi register. Since bl is the lowest 8 bits of the rbx register, which is callee saved, I pushed the register before changing the data and popped it after the loop to restore its original state. Moving the data in two steps succeeded in resolving the invalid combination error. 
