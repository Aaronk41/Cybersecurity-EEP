import os
from utils import get_file_hash
from signatures import malware_hashes
from quarantine import quarantine_file

def scan_folder(folder):
    print(f"Scanning: {folder}")
    for root, _, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = get_file_hash(full_path)
            if file_hash in malware_hashes:
                print(f"⚠️ Threat Detected: {full_path}")
                quarantine_file(full_path)
            else:
                print(f"✔️ Clean: {full_path}")
