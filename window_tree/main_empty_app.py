import tkinter as tk
from settings import specs_check as spec
from window_tree import main_window
from settings import settings_file as set_f
from window_tree.Window import Window
class App(tk.Tk, Window):
    main_apps = []
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.withdraw()
        self.iconbitmap(set_f.icon_ico_path)
        self.title("EwelaOCR")


    def open_windows(self):
        if len(App.main_apps) == 0:
            for monitor_index in range(spec.number_of_monitors):
                App.main_apps.append(main_window.MainApp(monitor_index, self))

    @classmethod
    def destroy_windows(cls):
        for app in cls.main_apps:
            app.destroy()
        App.main_apps.clear()


    def close_window(self, event = None):
        self.destroy()








