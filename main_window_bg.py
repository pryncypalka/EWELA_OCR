import tkinter as tk
import specs_check as spec
import tkinter_main_window as main_window

class MainAppBG(tk.Toplevel):
    def __init__(self, monitor_index, parent):
        super().__init__(parent)
        self.old_x = None
        self.old_y = None
        self.ss_x = None
        self.ss_y = None
        self.monitor_index = monitor_index

        self.overrideredirect(True)
        self.attributes('-alpha', 0.2)


        self.geometry(f"{spec.monitors[monitor_index].width}x{spec.monitors[monitor_index].height}+"
                        f"{spec.monitors[monitor_index].x}+{spec.monitors[monitor_index].y}")

        self.canvas = tk.Canvas(self, width=spec.monitors[monitor_index].width,
                                height=spec.monitors[monitor_index].height, bg="black")
        self.canvas.place(x=0, y=0)

        tk_main_window = main_window.MainApp(monitor_index, self)
        tk_main_window.grab_set()
