import re
import pandas as pd

def parse_logs(log_file):
    pattern = re.compile(
        r"SRC=(?P<src_ip>\S+)\sDST=(?P<dst_ip>\S+)\sPROTO=(?P<proto>\S+)\sSPT=(?P<src_port>\d+)\sDPT=(?P<dst_port>\d+)"
    )
    data = []

    with open(log_file, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                entry = match.groupdict()
                action = "DROP" if "DROP" in line else "ACCEPT"
                entry['action'] = action
                data.append(entry)

    df = pd.DataFrame(data)
    return df
