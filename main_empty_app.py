import tkinter as tk
from tkinter import ttk
import specs_check as spec
import tkinter_main_window as main_window

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.geometry('0x0')
    def open_windows(self):
        for monitor_index in range(spec.number_of_monitors):
            main_app = main_window.MainApp(monitor_index, self)

