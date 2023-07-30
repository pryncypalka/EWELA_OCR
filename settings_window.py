import tkinter as tk
class IconApp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        tk.Button(self, text="Anuluj", command=self.close_window).pack()

    def close_window(self):
        super().destroy()




