import socket
import argparse

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is open")
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        exit()
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
    parser.add_argument("--host", required=True, help="Target host or IP")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    args = parser.parse_args()

    print(f"Scanning {args.host} from port {args.start} to {args.end}...\n")
    for port in range(args.start, args.end + 1):
        scan_port(args.host, port)

if __name__ == "__main__":
    main()
