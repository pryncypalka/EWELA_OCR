import tkinter as tk
import specs_check as spec
import main_window
import main_window_bg as bg_win
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.geometry('0x0')
    def open_windows(self):
        for monitor_index in range(spec.number_of_monitors):
            main_app = main_window.MainApp(monitor_index, self)


