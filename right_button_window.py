import tkinter as tk


class RButton(tk.Toplevel):
    def __init__(self,  parent):
        super().__init__(parent)

        self.overrideredirect(True)
        self.attributes('-transparentcolor', 'blue')
        # app.attributes('-fullscreen', True)

        tk.Button(self, text="Anuluj", command=parent.destroy).pack()
