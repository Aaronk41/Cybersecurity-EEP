import socket
import threading
import json

clients = {}  # username -> socket
public_keys = {}  # username -> public key string

def broadcast(sender, message):
    for username, conn in clients.items():
        if username != sender:
            try:
                conn.send(f"{sender}: {message}".encode())
            except:
                pass

def send_public_keys():
    key_data = json.dumps(public_keys).encode()
    for conn in clients.values():
        try:
            conn.send(b"__KEY_UPDATE__" + key_data)
        except:
            pass

def handle_client(conn, addr):
    try:
        conn.send(b"Enter your username: ")
        username = conn.recv(1024).decode().strip()

        if username in clients:
            conn.send(b"Username already taken. Disconnecting.\n")
            conn.close()
            return

        conn.send(b"Send your public key: ")
        pubkey = conn.recv(4096).decode()
        public_keys[username] = pubkey
        clients[username] = conn

        print(f"[NEW CONNECTION] {username} ({addr}) connected.")
        broadcast(username, "joined the chat.")
        send_public_keys()

        while True:
            msg = conn.recv(4096)
            if not msg:
                break
            broadcast(username, msg.decode())
    except:
        pass
    finally:
        conn.close()
        if username in clients:
            del clients[username]
        if username in public_keys:
            del public_keys[username]
        broadcast(username, "left the chat.")
        send_public_keys()
        print(f"[DISCONNECTED] {username} ({addr}) disconnected.")

def start_server(host='127.0.0.1', port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
