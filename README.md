# Task Manager – Operating System Simulation Using Python
An operating system simulation with process management, resource visualization, and real-time data fetching using Python.

**Overview**  
This is a Task Manager built with Python that simulates core features of an operating system, such as process management, system resource monitoring, and real-time data visualization. It provides an interactive GUI to manage active processes, visualize CPU and memory usage, and more.

**Features:**
- Real-time process management with detailed process information.
- Visualize system performance (CPU, Memory, Disk Usage) with dynamic graphs.
- Process control to kill unresponsive tasks.
- Dynamic data fetching using the `psutil` library.

**File Structure:**
- `main.py`: Core logic and application entry point.
- `performance_tab.py`: Handles system performance visualization.
- `process_tab.py`: Manages the active processes.
- `users_tab.py`: Displays user-related system data.
- `task_manager_data.json`: Stores settings and user preferences.

**Video Demonstration:**  
Check out the video showing the working of the Task Manager project: [https://drive.google.com/file/d/1PRywpVqVbuCCju5oBuUYN4kaKfpFoQLi/view]

**Installation Instructions:**
1. **Clone the repository** or download the project files.
   
2. **Install the required libraries** by running the following command in your terminal or command prompt:
      - Ensure that you have Python 3.x installed on your system.
      - let's install the libraries needed to run the Task Manager:
        **sudo apt install python3-psutil python3-matplotlib python3-tk**
        
3. **After installing the required libraries** you can run the main.py file with:
       - **python3 main.py**
