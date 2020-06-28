import socket
import sys

UDP_IP_ADDR = '10.0.0.3'
UDP_PORT = 6789
buffer = 4096
address = (UDP_IP_ADDR, UDP_PORT)

# file - not used yet

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input('> ').strip().encode()

    if message == 'quit'.encode():
        break

    # send message and hostname
    socket_client.sendto(message, address)
    socket_client.sendto(socket.gethostname().encode(), address)
    response, addr = socket_client.recvfrom(buffer)
    print("=> {}".format(response.decode()))

socket_client.close()
