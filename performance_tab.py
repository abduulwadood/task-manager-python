import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import psutil
import time


class PerformanceTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Performance")

        self.figure = Figure(figsize=(5, 3), dpi=100)
        self.cpu_ax = self.figure.add_subplot(111)
        self.cpu_ax.set_title("CPU Usage (%)")
        self.cpu_ax.set_xlabel("Time")
        self.cpu_ax.set_ylabel("Usage")
        self.cpu_usage_data = [0] * 50
        self.cpu_line, = self.cpu_ax.plot(self.cpu_usage_data, label="CPU Usage", color="blue")
        self.cpu_ax.legend()

        canvas = FigureCanvasTkAgg(self.figure, master=self.tab)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.performance_info = tk.Label(self.tab, text="", font=("Arial", 12), bg="white", fg="blue")
        self.performance_info.pack(pady=10)

    def update_performance(self):
        while True:
            self.cpu_usage_data = self.cpu_usage_data[1:] + [psutil.cpu_percent()]
            self.cpu_line.set_ydata(self.cpu_usage_data)
            self.cpu_ax.relim()
            self.cpu_ax.autoscale_view()

            memory = psutil.virtual_memory()
            total_memory = memory.total / 1024 / 1024 / 1024
            used_memory = memory.used / 1024 / 1024 / 1024
            cpu_freq = psutil.cpu_freq().current / 1000
            self.performance_info.config(
                text=f"Total Memory: {total_memory:.2f} GB | Used Memory: {used_memory:.2f} GB\nCPU Speed: {cpu_freq:.2f} GHz"
            )
            self.figure.canvas.draw()
            time.sleep(1)
