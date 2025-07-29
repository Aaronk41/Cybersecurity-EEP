import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime

class BountyDashboard(tk.Tk):
    def __init__(self, data_file='bounty_data.json'):
        super().__init__()
        self.title("Red Ribbon Galactic Bounty Database")
        self.geometry("900x600")
        self.configure(bg="#0f0f0f")

        self.data_file = data_file
        self.load_data()

        self.create_widgets()

    def load_data(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.bounties = json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load bounty data:\n{e}")
            self.bounties = []

    def create_widgets(self):
        title = tk.Label(self, text="RED RIBBON GALACTIC BOUNTY DATABASE",
                         font=("Orbitron", 20, "bold"), fg="#00ffcc", bg="#0f0f0f")
        title.pack(pady=15)

        # Filters Frame
        filter_frame = tk.Frame(self, bg="#0f0f0f")
        filter_frame.pack(pady=5)

        # Planet filter
        tk.Label(filter_frame, text="Planet:", fg="#ff007f", bg="#0f0f0f",
                 font=("Consolas", 12, "bold")).grid(row=0, column=0, padx=10)
        planets = sorted(set(b.get('planet', 'Unknown') for b in self.bounties))
        self.planet_var = tk.StringVar(value="All")
        planet_options = ["All"] + planets
        self.planet_menu = ttk.Combobox(filter_frame, values=planet_options, textvariable=self.planet_var, width=15)
        self.planet_menu.grid(row=0, column=1)
        self.planet_menu.bind("<<ComboboxSelected>>", lambda e: self.update_table())

        # Status filter
        tk.Label(filter_frame, text="Status:", fg="#ff007f", bg="#0f0f0f",
                 font=("Consolas", 12, "bold")).grid(row=0, column=2, padx=10)
        statuses = sorted(set(b.get('status', 'Unknown') for b in self.bounties))
        self.status_var = tk.StringVar(value="All")
        status_options = ["All"] + statuses
        self.status_menu = ttk.Combobox(filter_frame, values=status_options, textvariable=self.status_var, width=15)
        self.status_menu.grid(row=0, column=3)
        self.status_menu.bind("<<ComboboxSelected>>", lambda e: self.update_table())

        # Sort by dropdown
        tk.Label(filter_frame, text="Sort By:", fg="#ff007f", bg="#0f0f0f",
                 font=("Consolas", 12, "bold")).grid(row=0, column=4, padx=10)
        self.sort_var = tk.StringVar(value="Bounty")
        sort_options = ["Bounty", "Threat Level", "Last Sighting"]
        self.sort_menu = ttk.Combobox(filter_frame, values=sort_options, textvariable=self.sort_var, width=15)
        self.sort_menu.grid(row=0, column=5)
        self.sort_menu.bind("<<ComboboxSelected>>", lambda e: self.update_table())

        # Treeview table for bounty display
        columns = ("Name", "Bounty", "Status", "Planet", "Threat Level", "Last Sighting")
        self.tree = ttk.Treeview(self, columns=columns, show='headings', height=20)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center', width=130)
        self.tree.pack(padx=20, pady=15, fill=tk.BOTH, expand=True)

        # Style adjustments for cyberpunk look
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("Treeview",
                        background="#111111",
                        foreground="#00ff00",
                        fieldbackground="#111111",
                        font=("Consolas", 11))
        style.map('Treeview', background=[('selected', '#ff007f')])

        self.update_table()

    def update_table(self):
        # Clear current rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Filter data
        filtered = self.bounties
        planet_filter = self.planet_var.get()
        status_filter = self.status_var.get()

        if planet_filter != "All":
            filtered = [b for b in filtered if b['planet'] == planet_filter]
        if status_filter != "All":
            filtered = [b for b in filtered if b['status'] == status_filter]

        # Sort data
        sort_key = self.sort_var.get()
        if sort_key == "Bounty":
            # Extract number from bounty string, sort descending
            def bounty_value(b):
                val = b['bounty'].replace("¥", "").replace(" Zeni", "").replace(",", "")
                try:
                    return int(val)
                except:
                    return 0
            filtered.sort(key=bounty_value, reverse=True)
        elif sort_key == "Threat Level":
            threat_order = {"Critical": 3, "Moderate": 2, "Low": 1, "Unknown": 0}
            filtered.sort(key=lambda b: threat_order.get(b['threat_level'], 0), reverse=True)
        elif sort_key == "Last Sighting":
            def sighting_date(b):
                try:
                    return datetime.strptime(b['last_sighting'], "%Y-%m-%d %H:%M")
                except:
                    return datetime.min
            filtered.sort(key=sighting_date, reverse=True)

        # Insert rows
        for b in filtered:
            self.tree.insert("", tk.END, values=(
                b['name'], b['bounty'], b['status'], b['planet'], b['threat_level'], b['last_sighting']
            ))


if __name__ == "__main__":
    app = BountyDashboard()
    app.mainloop()
