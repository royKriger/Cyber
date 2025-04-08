import socket
import time


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 8200))
data, client_addr = server_socket.recvfrom(1024)

name = data.decode()
time1 = time.perf_counter()

server_socket.sendto(f"Hello, {name}".encode(), client_addr)

delta_time = time.perf_counter() - time1
print(f"{delta_time:.5f}")

server_socket.close()
