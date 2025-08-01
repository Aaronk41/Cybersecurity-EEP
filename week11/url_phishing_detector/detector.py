import re
import sys
from urllib.parse import urlparse

suspicious_keywords = [
    "login", "verify", "bank", "secure", "account", "update", "password", "signin", "confirm"
]

def is_ip_address(domain):
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", domain)

def check_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path.lower()
    full_url = url.lower()

    flags = {
        "uses_ip": is_ip_address(domain),
        "has_at_symbol": "@" in url,
        "has_https": url.startswith("https"),
        "has_long_url": len(url) > 75,
        "has_suspicious_words": any(word in full_url for word in suspicious_keywords),
        "has_multiple_subdomains": domain.count(".") > 2,
    }

    score = sum(flags.values())

    print(f"\nURL: {url}")
    for k, v in flags.items():
        print(f" - {k}: {'Yes' if v else 'No'}")

    if score >= 3:
        print("🔴 Result: Likely PHISHING")
    elif score == 2:
        print("🟠 Result: Suspicious")
    else:
        print("🟢 Result: Likely Safe")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python detector.py <url>")
    else:
        check_url(sys.argv[1])


