import tkinter as tk
from tkinter import ttk
import threading
from process_tab import ProcessTab
from performance_tab import PerformanceTab
from users_tab import UsersTab


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("900x600")
        self.root.configure(bg="white")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=880, height=560)

        # Tabs
        self.process_tab = ProcessTab(self.notebook)
        self.performance_tab = PerformanceTab(self.notebook)
        self.users_tab = UsersTab(self.notebook)

        # Start performance updates in a separate thread
        threading.Thread(target=self.performance_tab.update_performance, daemon=True).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
