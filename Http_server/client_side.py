import base64
import socket

client_side = socket.socket()
client_side.connect(('127.0.0.1', 8200))
length = 100000000
with open(r'C:\Users\Pc2\Desktop\Images\image.png', 'rb') as file:
    image = file.read()

image = base64.b64encode(image).decode()
response = fr"""
POST /upload

Host: google.com

Accept: text/html,application/xhtml+xml,application/xml
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.110
Accept-Encoding: gzip,deflate,sdch

Cookie: ASP.NET_SessionId=qrth0wbrqvc2mwonnp5luc5p;

Content-Type: Application/x-www-form-urlencoded

Content-Length: {len(image)}
query=send image to server{image}"""
print(image)
client_side.send(response.encode())
