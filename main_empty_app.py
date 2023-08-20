import tkinter as tk
import specs_check as spec
import main_window

class App(tk.Tk):
    main_apps = []
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.withdraw()
        self.iconbitmap("EwelaOCR.ico")
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






