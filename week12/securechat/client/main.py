import socket
import threading
import json
from crypto import generate_key_pair, encrypt_message, decrypt_message
from shared.protocol import wrap_message, unwrap_message

private_key, public_key_pem = generate_key_pair()
user_keys = {}  # username -> public key PEM
username = ""

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(4096)
            if not data:
                break

            if data.startswith(b"__KEY_UPDATE__"):
                key_data = json.loads(data[len(b"__KEY_UPDATE__"):].decode())
                user_keys.update(key_data)
                print("[KEYS UPDATED]")
                continue

            msg_type, sender, content = unwrap_message(data)
            if msg_type == "encrypted":
                try:
                    decrypted = decrypt_message(content, private_key)
                    print(f"\n{sender} (encrypted): {decrypted}")
                except:
                    print(f"\n{sender} (encrypted): [Could not decrypt]")
            else:
                print(f"\n{sender}: {content.decode()}")
        except Exception as e:
            print(f"[ERROR] Receiving: {e}")
            break

def start_client(host='127.0.0.1', port=5555):
    global username
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print(client.recv(1024).decode(), end="")
    username = input()
    client.send(username.encode())

    print(client.recv(1024).decode(), end="")
    client.send(public_key_pem.encode())

    thread = threading.Thread(target=receive_messages, args=(client,), daemon=True)
    thread.start()

    try:
        while True:
            msg = input("You (encrypted): ")
            for user, pubkey in user_keys.items():
                if user == username:
                    continue
                encrypted = encrypt_message(msg, pubkey)
                wrapped = wrap_message("encrypted", username, encrypted)
                client.send(wrapped)
    except KeyboardInterrupt:
        print("\nDisconnected.")
        client.close()

if __name__ == "__main__":
    start_client()

