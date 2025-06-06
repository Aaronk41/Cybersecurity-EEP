from scapy.all import *
from scapy.layers.http import HTTPRequest
import argparse
from datetime import datetime
import json

def packet_callback(packet):
    """Process each packet and extract HTTP information"""
    if packet.haslayer(HTTPRequest):
    
        timestamp = datetime.fromtimestamp(packet.time).strftime('%Y-%m-%d %H:%M:%S')
        
 
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
     
        http_layer = packet[HTTPRequest]
        host = http_layer.Host.decode('utf-8', errors='replace')
        path = http_layer.Path.decode('utf-8', errors='replace')
        method = http_layer.Method.decode('utf-8', errors='replace')
        
  
        url = f"http://{host}{path}" if not host.startswith('http') else f"{host}{path}"
        
   
        print(f"\n[+] {timestamp} - {src_ip} -> {dst_ip}")
        print(f"    HTTP {method} Request: {url}")
        
       
        if hasattr(http_layer, 'fields'):
            print("    Headers:")
            for field in http_layer.fields:
                if field not in ['Method', 'Path', 'Http-Version']:
                    try:
                        value = http_layer.fields[field].decode('utf-8', errors='replace')
                        print(f"        {field}: {value}")
                    except:
                        continue
        
      
        if packet.haslayer(Raw):
            try:
                raw_load = packet[Raw].load.decode('utf-8', errors='replace')
                if raw_load.strip():
                    print("    Request Body:")
                    try:
                       
                        json_data = json.loads(raw_load)
                        print(f"        {json.dumps(json_data, indent=8)}")
                    except ValueError:
                      
                        for line in raw_load.split('&'):
                            print(f"        {line}")
            except Exception as e:
                print(f"    Error decoding body: {str(e)}")

def start_sniffing(interface=None, filter_exp="tcp port 80", count=0):
    """Start the packet sniffing process"""
    print(f"\n[!] Starting HTTP sniffer on interface {interface or 'default'}")
    print(f"[!] Filter: {filter_exp}")
    print("[!] Press Ctrl+C to stop\n")
    
    try:
        sniff(
            prn=packet_callback,
            store=False,
            filter=filter_exp,
            iface=interface,
            count=count
        )
    except KeyboardInterrupt:
        print("\n[!] Stopping sniffer...")
    except Exception as e:
        print(f"[!] Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enhanced HTTP Packet Sniffer")
    parser.add_argument("-i", "--interface", help="Network interface to sniff on")
    parser.add_argument("-f", "--filter", default="tcp port 80", 
                       help="BPF filter expression (default: tcp port 80)")
    parser.add_argument("-c", "--count", type=int, default=0,
                       help="Number of packets to capture (0 for unlimited)")
    
    args = parser.parse_args()
    
  
    if os.geteuid() != 0:
        print("[!] Warning: Sniffing may require root privileges")
    
    start_sniffing(
        interface=args.interface,
        filter_exp=args.filter,
        count=args.count
    )
