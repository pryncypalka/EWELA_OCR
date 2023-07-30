import tkinter as tk
import specs_check as spec
import main_window
import settings_window as win_icon
class App(tk.Tk):
    main_apps = []
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.withdraw()


    def open_windows(self):
        for monitor_index in range(spec.number_of_monitors):
            App.main_apps.append(main_window.MainApp(monitor_index, self))

    @classmethod
    def destroy_windows(cls):
        for app in cls.main_apps:
            app.destroy()
    def open_icon_settings(self):
        window_icon = win_icon.IconApp(self)




