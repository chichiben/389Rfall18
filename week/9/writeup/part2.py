#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket, time
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331    # port
# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
# receive some data
data = s.recv(1024)
print(data.strip())
while (1):
    data_list = data.split(' ')
    if 'of' in data_list:
        idx = data_list.index('of')
        to_hash = data_list[idx + 1]
        to_hash = to_hash.strip('>')
        to_hash = to_hash.strip()
        hash = ""
        if "sha512" in data_list:
            hash = hashlib.sha512(to_hash)
        elif "md5" in data_list:
            hash = hashlib.md5(to_hash)
        elif "sha1" in data_list:
            hash = hashlib.sha1(to_hash)
        elif "sha224" in data_list:
            hash = hashlib.sha224(to_hash)
        elif "sha256" in data_list:
            hash = hashlib.sha256(to_hash)
        elif "sha384" in data_list:
            hash = hashlib.sha384(to_hash)
        else:
            print("Didn't recognize command.")
        hex = hash.hexdigest() + "\n"
        s.send(hex)
        time.sleep(1)
        data = s.recv(1024)
        print(data.strip())
    else:
        break
# close the connection
s.close()
