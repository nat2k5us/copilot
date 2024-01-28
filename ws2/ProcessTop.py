import psutil
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import threading
import time

class ProcessViewer(toga.App):
    def startup(self):
        # Main window
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Data display box
        self.data_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Table to display process data
        self.process_table = toga.Table(
            headings=['PID', 'Name', 'CPU Usage'],
            style=Pack(flex=1)
        )
        self.data_box.add(self.process_table)

        # Set the main window content
        self.main_window.content = self.data_box
        self.main_window.show()

        # Start the thread to update the process list
        self.update_thread = threading.Thread(target=self.update_process_list, daemon=True)
        self.update_thread.start()

    def update_process_list(self):
        # Initiate CPU percent calculation
        psutil.cpu_percent(interval=None)

        while True:
            time.sleep(1)  # Ensuring there's a gap for CPU percent calculation

            # Get top 10 CPU consuming processes
            processes = []
            for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                try:
                    cpu_usage = p.cpu_percent(interval=None)
                    if cpu_usage is not None:
                        print(f"Process: {p.info['name']}, CPU Usage: {cpu_usage}")
                        processes.append((p.info['pid'], p.info['name'], cpu_usage))
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            processes.sort(key=lambda x: x[2], reverse=True)
            top_processes = processes[:10]

            # Directly update the table from the background thread
            self.main_window.app._impl.loop.call_soon_threadsafe(
                self.update_table_data, top_processes)

    def update_table_data(self, processes):
        # Clear the existing data
        self.process_table.data = []

        # Add new data
        for process in processes:
            self.process_table.data.append(process)

def main():
    # Set a formal name for the application
    return ProcessViewer('Process Viewer', 'org.example.processviewer')

if __name__ == '__main__':
    main().main_loop()
