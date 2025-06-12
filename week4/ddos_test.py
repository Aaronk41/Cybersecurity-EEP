import time
from collections import defaultdict

MAX_REQUESTS_PER_IP = 10
TIME_WINDOW = 5  
BLOCK_DURATION = 60  

request_log = defaultdict(list)
blocked_ips = {}

def handle_request(ip_address):
    current_time = time.time()

    if ip_address in blocked_ips:
        if current_time < blocked_ips[ip_address]:
            print(f"[BLOCKED] {ip_address} is currently blocked.")
            return
        else:
            del blocked_ips[ip_address]

    request_log[ip_address].append(current_time)
    
    request_log[ip_address] = [
        t for t in request_log[ip_address] if current_time - t <= TIME_WINDOW
    ]

    if len(request_log[ip_address]) > MAX_REQUESTS_PER_IP:
        print(f"[ALERT] {ip_address} is making too many requests! Blocking for {BLOCK_DURATION} seconds.")
        blocked_ips[ip_address] = current_time + BLOCK_DURATION
    else:
        print(f"[OK] {ip_address} request accepted.")

def simulate_requests():
    test_ips = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]
    rounds = 30  

    for i in range(rounds):
        print(f"\nRound {i+1}")
        for ip in test_ips:
            handle_request(ip)
        time.sleep(0.5)  

if __name__ == "__main__":
    simulate_requests()
