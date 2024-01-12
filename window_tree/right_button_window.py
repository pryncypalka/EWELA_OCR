import tkinter as tk
from window_tree import main_empty_app as empty
from settings import settings_file as set_f
from window_tree.Window import Window
class RButton(tk.Toplevel, Window):
    def __init__(self,  parent):
        super().__init__(parent)
        self.iconbitmap(set_f.icon_ico_path)
        self.title("EwelaOCR")
        self.overrideredirect(True)


        tk.Button(self, text="Anuluj", command=self.close_window).pack()

    def close_window(self, event=None):
        # Zamknięcie okna po wciśnięciu klawisza Esc
        # self.parent.destroy()
        empty.App.destroy_windows()
        self.destroy()

