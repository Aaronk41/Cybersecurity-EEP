from scapy.all import *
from scapy.layers.http import HTTPRequest

def packet_callback(packet):
    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        print(f"HTTP Request: {url}")
        if packet.haslayer(Raw):
            print(f"Raw Data: {packet[Raw].load.decode('utf-8', errors='ignore')}")

if __name__ == "__main__":
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0, filter="tcp port 80")
