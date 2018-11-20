#!/usr/bin/env python2
# from the git repo
import md5py, socket, time
import struct

#####################################
### STEP 1: Calculate forged hash ###
#####################################
host = "142.93.118.186"
port = 1234
# original message here
message = 'Hello World'
# open a socket connection with the digital notary
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
# send in the message and receive the signed version
data = s.recv(1024)
print(data.strip())
s.send(' 1\n')
data = s.recv(1024)
s.send(message + '\n')
data = s.recv(1024)
data_list = data.split(' ')
idx = data_list.index('hash:')
hash = data_list[idx + 1]
# a legit hash of secret + message goes here, obtained from signing a message
legit =  hash.strip()

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'bad'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
secret_len = 6
while secret_len <= 15:
    msg_len = len(message) + secret_len
    padding_len = 56 - msg_len
    padding = '\x80'
    count = 1
    while count < padding_len:
        padding += '\x00'
        count += 1

    msg_len_bits = msg_len * 8
    padding += struct.pack('<q', msg_len_bits)

    # payload is the message that corresponds to the hash in `fake_hash`
    # server will calculate md5(secret + payload)
    #                     = md5(secret + message + padding + malicious)
    #                     = fake_hash
    payload = message + padding + malicious
    # send `fake_hash` and `payload` to server (manually or with sockets)
    s.send(' 2\n')
    data = s.recv(1024)
    print(data.strip())
    s.send(fake_hash + '\n')
    data = s.recv(1024)
    time.sleep(1)
    print(data.strip())
    s.send(payload + '\n')
    time.sleep(1)
    data = s.recv(1024)
    print(data.strip())
    secret_len += 1
# REMEMBER: every time you sign new data, you will regenerate a new secret!
s.close()
