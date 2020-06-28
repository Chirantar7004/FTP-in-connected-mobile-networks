import socket
import socket
import sys
import hashlib
import pickle
import sys
import os
import math
import time
localIP     = "10.1.0.3"
localPort   = 20001
bufferSize  = 4096
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams
filename = 'trans_file'
f = open('newfile2.py', 'wb')
print("Ready to receive.....")
listt =[]
rec_dict = dict.fromkeys(listt,0 )
stor_dict = {}
transfer_done = False
check_no = 0
intelligent_loss_variable = 0
while not transfer_done:
    data, address = UDPServerSocket.recvfrom(bufferSize)
    load_data = pickle.loads(data)
    recq_seq_no = load_data[0]
    no_of_chunks = load_data[2]
    intelligent_loss_variable = load_data[3]
    stor_dict[recq_seq_no] = load_data[1]
    rec_dict[recq_seq_no] = 1
    check_no = check_no + 1
    print("recv")
    if(check_no == no_of_chunks):
    	transfer_done = True
    	UDPServerSocket.sendto(pickle.dumps(rec_dict),address)
    	break
    else:
        continue
var = no_of_chunks + 1
for i in range(1, var):
		f.write(stor_dict[i])
print("Transfer complete",intelligent_loss_variable)
for i in range(0,(2*intelligent_loss_variable)):
    UDPServerSocket.sendto(pickle.dumps(rec_dict),address)

f.close()
UDPServerSocket.close()
