import socket
import os

while True:
    my_socket = socket.socket()
    my_socket.connect(("127.0.0.1", 1234))
    print(my_socket.recv(1024).decode())
    password = input()
    my_socket.send(password.encode())
    response = my_socket.recv(1024).decode()
    print(response)
    request = ""
    while not response.startswith("You're Signed"):
        password = input()
        my_socket.send(password.encode())
        response = my_socket.recv(1024).decode()
        print(response)

    if not response.startswith("You're Signed"):
        request = "QUIT"
    while request != "QUIT":
        request = input()
        if request.startswith("SAVE"):
            path = request.split()[-1]
            path = path.replace('"', '')
            if os.path.exists(path):
                with open(path, 'r') as file:
                    file_content = file.read()
                    request += ' ' + file_content
                    my_socket.send(file_content.encode())
                    response = my_socket.recv(1024).decode()
            else:
                my_socket.send("An Error Occurred".encode())
        my_socket.send(request.encode())
        response = my_socket.recv(1024).decode()
        print(response)

    my_socket.close()
