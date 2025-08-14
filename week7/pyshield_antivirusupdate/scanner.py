import os
from quarantine import quarantine_file


def scan_folder(folder):
    print(f"🔍 Scanning: {folder}")
    for root, _, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            try:
             
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                
                if "MALWARE_TEST" in content:
                    print(f"⚠️ Threat Detected: {full_path}")
                    quarantine_file(full_path)
                else:
                    print(f"✔️ Clean: {full_path}")

            except Exception as e:
                print(f"⚠️ Could not read {full_path}: {e}")

