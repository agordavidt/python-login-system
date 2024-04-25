import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 999))

message = client.recv(1024).decode()
client.send(input(message).encoded())
print(client.recv(1024).decode())