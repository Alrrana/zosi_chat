from socket import *
import time
import sys

host = '192.168.1.255'
my_ip = gethostbyname(gethostname())

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('', 778))
udp_socket.sendto(str.encode(my_ip), (host, 777))

server_ip, musor = udp_socket.recvfrom(1024)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect((server_ip, 777))
file = open('C:\\Users\\gfhfl\\Downloads\\YandexPackLoader.exe', 'rb')
data = file.read()
tcp_socket.send(data)
file.close()
