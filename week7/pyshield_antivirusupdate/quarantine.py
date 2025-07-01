import os
import shutil

QUARANTINE_FOLDER = "quarantine"

def quarantine_file(file_path):
    try:
        if not os.path.exists(QUARANTINE_FOLDER):
            os.makedirs(QUARANTINE_FOLDER)

        file_name = os.path.basename(file_path)
        quarantined_name = file_name + ".quarantined"
        destination = os.path.join(QUARANTINE_FOLDER, quarantined_name)

        shutil.move(file_path, destination)
        print(f"🚫 Quarantined: {file_path} → {destination}")

    except Exception as e:
        print(f"⚠️ Failed to quarantine {file_path}: {e}")
