import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from process_monitor import ProcessMonitor

class Dashboard(toga.App):
    def startup(self):
        self.process_monitor = ProcessMonitor()

        self.main_window = toga.MainWindow(title=self.formal_name)

        self.table = toga.Table(headings=["PID", "Name", "CPU%"],
                                style=Pack(flex=1),
                                on_select=self.select_element)

        box = toga.Box(children=[self.table],
                       style=Pack(direction=COLUMN, padding=5))

        self.main_window.content = box
        self.main_window.show()

        self.refresh_data()

    def refresh_data(self):
        self.table.data = self.process_monitor.get_top_processes()
        self.main_window.refresh()
        self.main_window.set_timeout(1, self.refresh_data)

    def select_element(self, widget, row):
        pass

def main():
    return Dashboard()