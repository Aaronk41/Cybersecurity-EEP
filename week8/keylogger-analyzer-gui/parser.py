def parse_log(path):
    entries = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(" - User typed: ")
            if len(parts) != 2:
                continue
            timestamp, key = parts
            flag = "SUSPICIOUS" if filter_suspicious(key) else "OK"
            entries.append((timestamp, key, flag))
    return entries

def filter_suspicious(key):
    suspicious = ["rm", "sudo", "netstat", "whoami", "passwd"]
    return any(x in key.lower() for x in suspicious)
