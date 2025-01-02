import tkinter as tk
from tkinter import ttk, messagebox
import psutil


class ProcessTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Processes")

        self.process_table = ttk.Treeview(
            self.tab, columns=("PID", "Name", "User", "Memory", "CPU"), show="headings"
        )
        self.process_table.heading("PID", text="PID")
        self.process_table.heading("Name", text="Name")
        self.process_table.heading("User", text="User")
        self.process_table.heading("Memory", text="Memory (MB)")
        self.process_table.heading("CPU", text="CPU (%)")
        self.process_table.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.tab, orient=tk.VERTICAL, command=self.process_table.yview)
        self.process_table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        button_frame = tk.Frame(self.tab, bg="white")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Refresh", command=self.refresh_processes, bg="blue", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Kill Process", command=self.kill_process, bg="blue", fg="white").pack(side=tk.LEFT, padx=10)

        self.refresh_processes()

    def refresh_processes(self):
        self.process_table.delete(*self.process_table.get_children())
        for proc in psutil.process_iter(['pid', 'name', 'username', 'memory_info', 'cpu_percent']):
            try:
                mem_usage = proc.info['memory_info'].rss / 1024 / 1024
                self.process_table.insert(
                    "", "end", values=(proc.info['pid'], proc.info['name'], proc.info['username'], f"{mem_usage:.2f}", proc.info['cpu_percent'])
                )
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

    def kill_process(self):
        selected_item = self.process_table.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a process to terminate.")
            return

        pid = int(self.process_table.item(selected_item, "values")[0])
        try:
            psutil.Process(pid).terminate()
            messagebox.showinfo("Success", f"Process {pid} terminated successfully.")
            self.refresh_processes()
        except psutil.AccessDenied:
            messagebox.showerror("Error", "Permission denied to terminate the process.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
