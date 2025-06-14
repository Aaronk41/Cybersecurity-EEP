import zipfile

def crack_zip(zip_path, wordlist_path):
    try:
        zip_file = zipfile.ZipFile(zip_path)
    except FileNotFoundError:
        print(f"[!] ZIP file '{zip_path}' not found.")
        return
    except zipfile.BadZipFile:
        print(f"[!] File '{zip_path}' is not a valid zip file.")
        return

    with open(wordlist_path, 'r', errors='ignore') as f:
        passwords = f.read().splitlines()

    print(f"[+] Trying {len(passwords)} passwords...\n")

    for pwd in passwords:
        try:
            zip_file.extractall(pwd=bytes(pwd, 'utf-8'))
            print(f"[✅] Password found: '{pwd}'")
            return
        except RuntimeError:
            print(f"[-] Wrong password: '{pwd}'")
        except Exception as e:
            print(f"[!] Error: {e}")
    
    print("[❌] Password not found in the wordlist.")

if __name__ == '__main__':
    zip_path = input("Enter path to ZIP file: ").strip()
    wordlist_path = input("Enter path to wordlist: ").strip()
    crack_zip(zip_path, wordlist_path)