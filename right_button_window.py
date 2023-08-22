import tkinter as tk
import main_empty_app as empty
import settings_file as set_f
class RButton(tk.Toplevel):
    def __init__(self,  parent):
        super().__init__(parent)
        self.iconbitmap(set_f.icon_ico_path)
        self.title("EwelaOCR")
        self.overrideredirect(True)


        tk.Button(self, text="Anuluj", command=self.close_window).pack()

    def close_window(self):
        # Zamknięcie okna po wciśnięciu klawisza Esc
        # self.parent.destroy()
        empty.App.destroy_windows()
        self.destroy()

