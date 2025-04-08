import socket
import os
import base64
from datetime import date

current_time = date.today()


def content_prefix_fix(status, length):
    prefix = f"""HTTP/1.1 {status}
User-Agent: curl/7.16.3 libcurl/7.16.3 OpenSSL/0.9.7l zlib/1.2.3
Host: localhost:8200
Accept-Language: he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
ETag: &quot;34aa387-d-1568eb00&quot;
Accept-Ranges: bytes
Content-Length: {length}
Vary: Accept-Encoding
Content-Type: text/html 

<html>
<body>  
"""
    return prefix


server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 8200))
server_socket.listen()
(client_socket, client_address) = server_socket.accept()
data = client_socket.recv(1024).decode()
forbidden = False
file_not_found = False
server_response = ""

if "/upload" in data:
    image = data.split('server')[-1]
    with open(r'C:\Users\Pc2\Desktop\image.png', 'wb') as file:
        file.write(base64.b64decode(image))

path = data.split(" ")[1]
if "/calculate-next" in path:
    if '?' not in path:
        server_response += """
<h1>The Next Number Is: 5</h1>
"""
        with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
            file.write(str(current_time) + ' The server executed calculate-next \n')
    else:
        num = int(path.split("=")[-1])
        server_response += f"""
<h1>The Next Number Is: {num + 1}</h1>
"""
        with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
            file.write(str(current_time) + ' The server executed calculate-next with the number: ' + str(num) + '\n')
elif "/triangle-area" in path:
    path = path.split("?")
    width = int(path[1].split('=')[-1])
    height = int(path[2].split('=')[-1])
    server_response += f"""
<h1>The Next Number Is: {width * height * 0.5}</h1>
"""
    with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
        file.write(
            str(current_time) + f' The server executed Triangle-area with the height: {height} and the width: {width} \n')
elif "/file-name" in path:
    file_path = path.split('=')[-1]
    file_path = file_path.replace("%22", "")
    condition = os.path.isfile(file_path)
    if file_path == r"C:\Users\roykr\Desktop\Google":
        forbidden = True
        with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
            file.write(str(current_time) + ' The server found a forbidden file who cannot be accessed \n')
    if not forbidden:
        if condition:
            file_content = open(file_path)
            text = file_content.read()
            new_text = ""
            for i in range(len(text)):
                new_text += text[i]
                if i % 25 == 0:
                    new_text += "\n"
            server_response += f"""
<h1>The Content of the file is: {new_text}</h1>
"""
            with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
                file.write(str(current_time) + ' The server executed the printing of the files content \n')
        else:
            file_not_found = True
            server_response += r"<h1>File Not Found</h1>"
            with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
                file.write(str(current_time) + ' The server didnt find any requested file \n')
elif "/image" in path:
    image_path = path.split('=')[-1]
    with open(image_path, "rb") as image:
        file = base64.b64encode(image.read()).decode()
    server_response += f"""
<img src="data:image/png;base64,{file}">
"""
    with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
        file.write(str(current_time) + ' The server executed an image print \n')
elif '/user-agent' in data:
    if 'Edge' in data:
        server_response += """
<h1> Youre using Microsoft Edge as your browser
"""
    elif 'Firefox' in data:
        server_response += """
<h1> Youre using Firefox as your browser
"""
    elif 'Explorer' in data:
        server_response += """
<h1> Youre using Internet Explorer as your browser
"""
    elif 'Chrome' in data:
        server_response += """
<h1> Youre using Google Chrome as your browser
"""
    with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
        file.write(str(current_time) + ' The server executed a browser identification act \n')
else:
    server_response += """
    <h1> Hello World! </h1>
    """

server_response += """
</body>
</html>
"""
server_response_length = len(server_response)
if forbidden:
    with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
        file.write(str(current_time) + ' The server found an Forbidden error \n')
    server_response = content_prefix_fix("403, Forbidden", server_response_length) + server_response
elif file_not_found:
    with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
        file.write(str(current_time) + ' The server found an Not Found Error \n')
    server_response = content_prefix_fix("404, Not Found", server_response_length) + server_response
# check if there is any error thrown
elif False:
    with open(r"C:\Users\Pc2\PycharmProjects\pythonProject\log.txt", 'a') as file:
        file.write(str(current_time) + ' The server Found an Internal Server Error \n')
    server_response = content_prefix_fix("500, Internal Server Error", server_response_length) + server_response
else:
    server_response = content_prefix_fix("200, OK", server_response_length) + server_response
client_socket.send(server_response.encode())
