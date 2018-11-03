#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1


if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, timestamp, author, count = struct.unpack("<LLL8sL", data[0:24])
offset_x = 24

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % int(timestamp))
print("AUTHOR: %s" % author)
print("COUNT: %d" % int(count))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

x = 0
print("-------  BODY  -------")

while offset_x < len(data):
	x += 1
	offset_y = offset_x + 8
	stype, slen = struct.unpack("<LL", data[offset_x:offset_y])
	svalue = []
	print("TYPE: %s" % hex(stype))
	if slen > 0:
		#PNG
		if stype == 0x1 or stype == 0x3:
			offset_x = offset_y
			offset_y += slen
			
			if stype == 0x1:
				temp = struct.unpack("<%dB" % slen, data[offset_x:offset_y])
				temp = (0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A) + temp
				with open("picture.png", 'w') as f:
					f.write(struct.pack("<%dB" % len(temp), *temp))
					f.close()
				
			print(svalue)
		#DWORDS
		elif stype == 0x2 or stype == 0x4:
			num = slen / 8
			y = 0
			while y < num:
				y += 1
				offset_x = offset_y
				offset_y += 8
				svalue.append(struct.unpack("<Q", data[offset_x:offset_y])[0])	
			print(svalue)
		elif stype == 0x5 or stype == 0x7:
			num = slen / 4
			y = 0
			while y < num:
				y += 1
				offset_x = offset_y
				offset_y += 4
				svalue.append(struct.unpack("<L", data[offset_x:offset_y])[0])
			print(svalue)
		elif stype == 0x6:
			offset_x = offset_y
			offset_y += 8
			svalue.append(struct.unpack("<d", data[offset_x:offset_y])[0])
			offset_x = offset_y
			offset_y += 8
			svalue.append(struct.unpack("<d", data[offset_x:offset_y])[0])
			print(svalue)
		elif stype == 0x9:
			offset_x = offset_y
			offset_y += slen
			svalue.append(struct.unpack("<%ds" % slen, data[offset_x:offset_y])[0])
			print(svalue)
		else:
			print("Invalid type.")
		offset_x = offset_y
	else:
		print("svalue does not exist.")
