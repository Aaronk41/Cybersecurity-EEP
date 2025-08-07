import socket

def start_client(host='127.0.0.1', port=5555):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Connected to the server. Type your messages.")

    try:
        while True:
            msg = input("You: ")
            client.send(msg.encode())
    except KeyboardInterrupt:
        print("\nDisconnected.")
        client.close()

if __name__ == "__main__":
    start_client()
