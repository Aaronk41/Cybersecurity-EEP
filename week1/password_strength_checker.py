import re
from pathlib import Path

def load_common_passwords(filepath="rockyou.txt"):
    try:
        with open(filepath, "r", encoding="latin-1") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print("Warning: Common passwords file not found.")
        return set()

def check_password_strength(password, common_passwords):
    if password in common_passwords:
        return "Very Weak (Common Password)"
    
    length = len(password)
    score = 0

    # Length check
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    # Complexity checks
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength rating
    if score >= 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

if __name__ == "__main__":
    common_passwords = load_common_passwords()
    password = input("Enter password to check: ")
    strength = check_password_strength(password, common_passwords)
    print(f"Password Strength: {strength}")
