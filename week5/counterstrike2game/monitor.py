from scapy.all import sniff, IP, UDP
from datetime import datetime

#  CS2 ports (Source 2 engine / Steam)
WATCH_PORTS = list(range(27015, 27051)) + [7777, 4380]

def is_game_traffic(packet):
    if IP in packet and UDP in packet:
        return packet.sport in WATCH_PORTS or packet.dport in WATCH_PORTS
    return False

def log_packet(packet):
    timestamp = datetime.now().strftime("%H:%M:%S")
    src = packet[IP].src
    dst = packet[IP].dst
    sport = packet[UDP].sport
    dport = packet[UDP].dport
    size = len(packet)
    print(f"[{timestamp}] {src}:{sport} → {dst}:{dport} | {size} bytes")

def start_monitor():
    print("Monitoring session traffic... Press Ctrl+C to stop.\n")
    sniff(filter="udp", prn=lambda pkt: log_packet(pkt) if is_game_traffic(pkt) else None, store=False)

if __name__ == "__main__":
    start_monitor()
