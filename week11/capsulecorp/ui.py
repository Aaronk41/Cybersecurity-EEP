import tkinter as tk
from tkinter import messagebox
import pyttsx3

class CyberpunkLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Red Ribbon Access Terminal")
        self.geometry("700x500")
        self.configure(bg="#0f0f0f")

        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Use female/system voice if available
        self.engine.setProperty('rate', 120)
        self.engine.setProperty('volume', 0.9)

        self.create_widgets()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="RED RIBBON AI CORE", fg="#00ffcc", bg="#0f0f0f",
                                     font=("Orbitron", 24, "bold"))
        self.title_label.pack(pady=30)

        self.username_label = tk.Label(self, text="USERNAME", fg="#ff007f", bg="#0f0f0f",
                                       font=("Consolas", 12, "bold"))
        self.username_label.pack()
        self.username_entry = tk.Entry(self, font=("Consolas", 14), fg="#0f0f0f", bg="#ccff00",
                                       insertbackground="#ff007f", justify='center')
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(self, text="ACCESS CODE", fg="#ff007f", bg="#0f0f0f",
                                       font=("Consolas", 12, "bold"))
        self.password_label.pack()
        self.password_entry = tk.Entry(self, font=("Consolas", 14), show="*", fg="#0f0f0f", bg="#ccff00",
                                       insertbackground="#ff007f", justify='center')
        self.password_entry.pack(pady=10)

        self.login_button = tk.Button(self, text="ENGAGE", command=self.login,
                                      font=("Consolas", 14, "bold"), fg="#0f0f0f", bg="#ff007f",
                                      activebackground="#ff007f", activeforeground="#ccff00",
                                      relief="flat")
        self.login_button.pack(pady=30)

        self.footer = tk.Label(self, text="Red Ribbon Surveillance Division", fg="#444444", bg="#0f0f0f",
                               font=("Consolas", 10, "italic"))
        self.footer.pack(side="bottom", pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "goku" and password == "capsulecorp":
            self.speak("Access granted. Welcome back, Son Goku.")
            messagebox.showinfo("Access Granted", "Welcome back, Son Goku.")
        else:
            self.speak("Access denied. Unauthorized attempt logged.")
            messagebox.showerror("Access Denied", "Incorrect credentials.")