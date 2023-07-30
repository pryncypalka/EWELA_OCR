import tkinter as tk
import specs_check as spec
import main_window

class App(tk.Tk):
    main_apps = []
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.geometry('0x0')

    def open_windows(self):
        for monitor_index in range(spec.number_of_monitors):
            App.main_apps.append(main_window.MainApp(monitor_index, self))

    @classmethod
    def destroy_windows(cls):
        for app in cls.main_apps:
            app.destroy()




