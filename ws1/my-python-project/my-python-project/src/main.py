import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from dashboard import Dashboard

class MyApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.dashboard = Dashboard()
        main_box.add(self.dashboard)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

if __name__ == '__main__':
    app = MyApp('My Application', 'com.example.myapp')
    app.main_loop()