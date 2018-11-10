#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hash_file = open("../hashes", 'r')
hashes = hash_file.readlines()
words = wordlist.readlines()

#hashes = hash_file.read().replace('\n', '')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase
for salt in salts:
    for word in words:
        word = word.strip()
        temp = salt + word;
        hash = hashlib.sha512(temp)
        new_hash = hash.hexdigest()
        new_hash = new_hash.strip()
        for hash in hashes:
            hash = hash.strip()
            if new_hash == hash:
                print(new_hash)
                print(temp)
wordlist.close()
hash_file.close()
