import socket
import sys
import hashlib
import pickle
import sys
import os
import math
import time
#how to send only relevant chunks?
intelligent_loss_variable = 0
client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
host     = sys.argv[2]
port   = 20001

server_address = (host,port)

file_name=sys.argv[1]

sequence= 1;
file_size = os.path.getsize(file_name)

num = int(file_size/500) + 1
print("File size is",file_size)
print(file_size)

num = int(file_size/3500) + 1
print("No of chunks is",num)

check_dict = False
listt = []
for i in range(1,(num+1)):
	listt.append(i)
server_dict = dict.fromkeys(listt,0 )
client_socket.settimeout(10)
def heartbeat(time_before_send):
	current_time = int(round(time.time()))
	if(current_time-time_before_send > 10):
		return False
	else:
		return True

def resend():
	global intelligent_loss_variable
	global file_ob
	global sequence
	intelligent_loss_variable = intelligent_loss_variable + 1
	file_ob.close()
	sequence = 1
	file_ob = open(file_name,'rb')
	transfer_complete = False
	time_before_send = int(round(time.time()))
	for i in range(1,(num+1)):
		main_data = file_ob.read(3500)
		if(server_dict.get(i)!=1):
			uns_data = []
			uns_data.append(sequence)
			uns_data.append(main_data)
			uns_data.append(num)
			uns_data.append(intelligent_loss_variable)
			final_data = pickle.dumps(uns_data)
			client_socket.sendto(final_data,server_address)
			sequence = sequence + 1
	print("Sent")		
	if(sequence == 1):
		print("Sending of File is Completed.",intelligent_loss_variable)
		sys.exit()
		
complete = False
time_before_send = int(round(time.time()))
file_ob = open(file_name,'rb')
resend()
while not complete:
	try:
		data, (address,port) = client_socket.recvfrom(100000)
	except socket.timeout:
			print("Sending again as previous packets were lost")
			resend()
			continue
	server_dict = pickle.loads(data)
	print("Recieved reply..")
	resend()	



print("Sending of file complete")
file_ob.close()
client_socket.close()



		
		

