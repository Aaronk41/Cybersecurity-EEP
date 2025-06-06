def caesar_cipher(text, shift, mode="encrypt"):
result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shifted = (ord(char) - offset + shift) % 26 + offset if mode == "encrypt" else (ord(char) - offset - shift) % 26 + offset
            result += chr(shifted)
        else:
            result += char
    return result

def brute_force_decrypt(ciphertext):
    for shift in range(26):
        print(f"Shift {shift}: {caesar_cipher(ciphertext, shift, 'decrypt')}")

if __name__ == "__main__":
    action = input("Encrypt (E) or Decrypt (D)? ").lower()
    text = input("Enter text: ")
    
    if action == "e":
        shift = int(input("Enter shift key: "))
        print("Encrypted:", caesar_cipher(text, shift))
    elif action == "d":
        if input("Known shift? (Y/N): ").lower() == "y":
            shift = int(input("Enter shift key: "))
            print("Decrypted:", caesar_cipher(text, shift, "decrypt"))
        else:
            brute_force_decrypt(text)
