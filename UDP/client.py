import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.sendto(f"Omer".encode(), ("127.0.0.1", 8200))
data, temp = my_socket.recvfrom(1024)
print(data.decode())
