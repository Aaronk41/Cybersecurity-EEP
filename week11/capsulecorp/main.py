from ui import CyberpunkLogin
from bounty_dashboard import BountyDashboard
from tkinter import messagebox

def main():
    login_app = CyberpunkLogin()

    def new_login():
        username = login_app.username_entry.get()
        password = login_app.password_entry.get()

        # Example simple credentials check
        if username == "goku" and password == "capsulecorp":
            login_app.speak("Access granted. Welcome back, Son Goku.")
            login_app.destroy()  # Close login window
            bounty_app = BountyDashboard()  # Open bounty dashboard
            bounty_app.mainloop()
        else:
            login_app.speak("Access denied. Unauthorized attempt logged.")
            messagebox.showerror("Access Denied", "Incorrect credentials.")

    login_app.login = new_login
    login_app.login_button.config(command=login_app.login)

    login_app.mainloop()

if __name__ == "__main__":
    main()
