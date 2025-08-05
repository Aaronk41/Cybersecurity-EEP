import pandas as pd
import re

def parse_firewall_log(filepath):
    pattern = re.compile(r'(?P<timestamp>\w{3}\s+\d+\s[\d:]+)\s(?P<host>\S+)\s(?P<process>\S+):\s(?P<action>ALLOW|DENY)\s(?P<protocol>\S+)\s(?P<src_ip>\d+\.\d+\.\d+\.\d+):(\d+)\s->\s(?P<dst_ip>\d+\.\d+\.\d+\.\d+):(\d+)')
    
    entries = []
    with open(filepath, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                entries.append(match.groupdict())

    return pd.DataFrame(entries)
