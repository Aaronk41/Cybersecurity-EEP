import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return port if result == 0 else None
    except:
        return None

def scan_ports(ip, ports):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda port: scan_port(ip, port), ports)
        for port in results:
            if port:
                open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP: ")
    port_range = input("Enter port range (e.g., 1-1000): ")
    start, end = map(int, port_range.split("-"))
    ports = range(start, end + 1)
    
    print(f"Scanning {target}...")
    open_ports = scan_ports(target, ports)
    
    if open_ports:
        print("Open ports:", sorted(open_ports))
    else:
        print("No open ports found.")
