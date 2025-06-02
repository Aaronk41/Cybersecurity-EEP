import hashlib

def crack_hash(hash_value, wordlist="rockyou.txt", algorithm="md5"):
    try:
        with open(wordlist, "r", encoding="latin-1") as file:
            for word in file:
                word = word.strip()
                if algorithm == "md5":
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif algorithm == "sha1":
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif algorithm == "sha256":
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    return "Unsupported algorithm."
                
                if hashed_word == hash_value:
                    return f"Found: {word}"
        return "Password not found in wordlist."
    except FileNotFoundError:
        return "Wordlist file not found."

if __name__ == "__main__":
    hash_input = input("Enter hash: ")
    algo = input("Algorithm (md5/sha1/sha256): ").lower()
    result = crack_hash(hash_input, algorithm=algo)
    print(result)
