import socket
import threading

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            print(f"[{addr}] {msg.decode()}")
        except:
            break
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")
