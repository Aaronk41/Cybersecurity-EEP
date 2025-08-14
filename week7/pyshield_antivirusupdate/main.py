from scanner import scan_folder

if __name__ == "__main__":
    target = input("Enter folder path to scan: ").strip()
    if not target:
        target = "testfolder"   
    scan_folder(target)
