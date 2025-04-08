import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 8200))
data, client_addr = server_socket.recvfrom(1024)
print(data.decode())
server_socket.sendto(f"Hello, {data.decode()}".encode(), client_addr)
server_socket.close()
