import socket
import threading
import logging
from datetime import datetime


logging.basicConfig(
    filename='honeypot.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def handle_ssh_connection(client_socket, ip):
    try:
        client_socket.send(b"SSH-2.0-OpenSSH_7.9p1 Ubuntu-10\r\n")
        data = client_socket.recv(1024)
        logging.info(f"SSH Attempt - IP: {ip} - Data: {data.decode(errors='ignore')}")
        client_socket.send(b"Permission denied (publickey).\r\n")
    except Exception as e:
        logging.error(f"SSH Error: {e}")
    finally:
        client_socket.close()

def handle_http_connection(client_socket, ip):
    try:
        request = client_socket.recv(1024)
        logging.info(f"HTTP Request - IP: {ip} - Data: {request.decode(errors='ignore')}")
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n\r\n"
            "<html><body><h1>Welcome to Fake Server!</h1></body></html>"
        )
        client_socket.send(response.encode())
    except Exception as e:
        logging.error(f"HTTP Error: {e}")
    finally:
        client_socket.close()

def honeypot(port, handler):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"[*] Honeypot running on port {port}")

    while True:
        client_socket, addr = server.accept()
        ip = addr[0]
        print(f"[+] Connection from {ip}:{addr[1]}")
        threading.Thread(target=handler, args=(client_socket, ip)).start()

if __name__ == "__main__":
    ssh_thread = threading.Thread(target=honeypot, args=(22, handle_ssh_connection))
    ssh_thread.daemon = True
    ssh_thread.start()

    http_thread = threading.Thread(target=honeypot, args=(80, handle_http_connection))
    http_thread.daemon = True
    http_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[*] Shutting down honeypot")
