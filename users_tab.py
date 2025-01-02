import tkinter as tk
from tkinter import ttk
import psutil


class UsersTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Users")

        self.users_table = ttk.Treeview(
            self.tab, columns=("User", "Terminal", "Host", "Started"), show="headings"
        )
        self.users_table.heading("User", text="User")
        self.users_table.heading("Terminal", text="Terminal")
        self.users_table.heading("Host", text="Host")
        self.users_table.heading("Started", text="Started")
        self.users_table.pack(fill=tk.BOTH, expand=True)

        tk.Button(self.tab, text="Refresh Users", command=self.refresh_users, bg="blue", fg="white").pack(pady=10)
        self.refresh_users()

    def refresh_users(self):
        self.users_table.delete(*self.users_table.get_children())
        for user in psutil.users():
            self.users_table.insert("", "end", values=(user.name, user.terminal, user.host, user.started))
