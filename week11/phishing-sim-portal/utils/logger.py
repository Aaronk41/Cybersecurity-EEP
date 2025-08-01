def log_credentials(username, password, ip, timestamp):
    with open("app/logs/credentials.csv", "a") as f:
        f.write(f"{timestamp},{ip},{username},{password}\n")
