import socket
import os

#I'm Bored
users_num = 1
users_dict = {}
while True:
    path = rf"C:\Users\roykr\Documents\RoyKriger\Clients"
    my_server = socket.socket()
    my_server.bind(("0.0.0.0", 1234))
    my_server.listen()
    (client_socket, client_address) = my_server.accept()
    client_socket.send("Enter Password In Order To Sign up --> ".encode())
    password = client_socket.recv(1024).decode()
    user_assigned = False
    request = ""
    user = ""
    path1 = ""
    for key, value in users_dict.items():
        if password == value:
            user_assigned = True            
            user = key
            path1 = path + rf"\{user}"
            client_socket.send("You're Signed in! \nWhats Your First Request --> ".encode())
    if not user_assigned:
        for i in range(3):
            client_socket.send("Confirm Your Password --> ".encode())
            password_again = client_socket.recv(1024).decode()
            if password_again == password:
                break
        if password_again != password:
            client_socket.send("Confirmation Of Password Not Good: GoodBye".encode())
            client_socket.close()
        user_assigned = True
        user = f"User{users_num}"
        users_dict[user] = password
        client_socket.send(f"You're Signed in! {user} \nWhat Would You Like Your First Command To Be? --> ".encode())
        path1 = path + rf"\{user}"
        os.mkdir(path1)
        users_num += 1
    while request != "QUIT" and user_assigned:
        request = client_socket.recv(1024).decode()
        if request.startswith('SAVE'):
            request = request.split(' ', 2)
            request[1] = request[1].replace('"', '')
            name_of_file = request[1].split("\\")[-1]
            path = path + '\\' + user + '\\' + name_of_file
            with open(path, 'w') as file:
                file.write(request[-1])
                client_socket.send("File Saved Successfully".encode())
                path = rf"C:\Users\roykr\Documents\RoyKriger\Clients"
        elif request.startswith("DIR"):
            files_list = os.listdir(path1)
            files_list = ','.join(files_list)
            print(files_list)
            client_socket.send(files_list.encode())
        else:
            client_socket.send("Alright! ".encode())

    client_socket.send("GoodBye! ".encode())
    client_socket.close()
