import socket


my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_socket.sendto("Omer".encode(), ("127.0.0.1", 8200))

data, temp = my_socket.recvfrom(1024)
data = data.decode()
print(data)
my_socket.close()
