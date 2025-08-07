import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print(f"\n{msg}")
        except:
            break

def start_client(host='127.0.0.1', port=5555):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print(client.recv(1024).decode(), end="")
    username = input()
    client.send(username.encode())

    thread = threading.Thread(target=receive_messages, args=(client,), daemon=True)
    thread.start()

    try:
        while True:
            msg = input()
            client.send(msg.encode())
    except KeyboardInterrupt:
        print("\nDisconnected.")
        client.close()

if __name__ == "__main__":
    start_client()
