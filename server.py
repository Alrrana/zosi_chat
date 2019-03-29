from socket import *

BUFF_SIZE = 1024

host = ''
my_ip = gethostbyname(gethostname())

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('', 777))

client_ip, server_ip = udp_socket.recvfrom(BUFF_SIZE)
udp_socket.sendto(str.encode(my_ip), (client_ip.decode(), 778))
udp_socket.close()

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(('', 777))
tcp_socket.listen(200)
connection, addr = tcp_socket.accept()

file = open('C:\\Users\\alran\\PycharmProjects\\try2\\2 (2).txt', 'wb')

while True:
    data = connection.recv(1024)
    file.write(data)
    if not data:
        break

print(client_ip)

file.close()
# file = open('C:\\Users\\gfhfl\\Downloads', 'rb')
