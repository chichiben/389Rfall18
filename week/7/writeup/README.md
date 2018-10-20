Writeup 7 - Forensics I
======

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG file; found in "Show Location Info" on my Mac Image Previews
2. Chicago, Illinois; John Hancock Center; under "GPS" in the location information.
3. Date Time: Aug 22, 2018 at 11:33:24 AM; found in TIFF
   Time Stamp: 16:33:24 UTC; found in "GPS"
4. Apple's iPhone 8 back camera 3.99mm f/1.8; found in "Exif"
5. Altitude: 539.54 m; found in "GPS"
6. Found by grepping the strings command:
   CMSC389R-{look_I_f0und_a_str1ng}
   Found by using binwalk to extract a .png file:
   CMSC389R-{abr@cadabra}

### Part 2 (55 pts)

*SUBMIT YOUR WRITEUP DETAILING YOUR APPROACH AND SOLUTION TO THIS PROBLEM HERE (>250 words). Dont forget to include the flag!*

The first thing I tried was using the 'file' command to find out more about the file type, but that didn't yield any interesting results. Then I tried using the 'readelf -h' command to find the entry point of the executable, and found that the entry point address was ﻿0x610. Using the entry point, I set a breakpoint at that address in gdb. When that didn't work, I tried disassembling it at the address and setting the length to 50 using: disas 0x610,+50. This showed that the function was calling ﻿__libc_csu_fini", ''﻿__libc_csu_init', and main, and that the address for main was﻿ ﻿0x62d. Since this method wasn't really yielding results, I switched over to radare2 to try reading the binary. This showed that the code was writing to a file with the path /tmp/.stego. In the terminal, I navigated to the tmp folder and ran the command 'ls -al' to view all files, including any hidden ones. Then I ran the exiftool command on the .stego file, which yielded the message: "﻿Processing JPEG-like data after unknown 1-byte header." Next, I ran strings on .stego to see if it would yield any results about the type of file. The first line showed that it was a JFIF file; based on the other information, I could guess that it was a JFIF file with an faulty 1-byte header. Upon opening the hex code in bless, I could see that the magic bytes were "00 FF D8 FF E0 00..." From Google, I knew that the magic bytes of a JFIF file are "FF D8 FF E0 00..." Therefore, I deleted the leading zeroes from the magic bytes and saved the file. This proceeded to run the code, and a message popped up saying that something was saved to 'file'. The file was a picture of a stegosaurus. I ran the 'steghide extract -sf' command on the image that I had deleted the leading magic bytes off of, and used stegosaurus as the password. The flag is: ﻿CMSC389R-{dropping_files_is_fun}.
