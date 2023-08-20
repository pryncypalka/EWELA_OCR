import tkinter as tk
import main_empty_app as empty
from tkinter import filedialog
import settings_file as set_f
import shutil

class Menu(tk.Toplevel):
    def __init__(self, parent, event, screenshot_rectangle):
        super().__init__(parent)
        self.parent = parent
        self.iconbitmap("EwelaOCR.ico")
        self.title("EwelaOCR")
        self.event = event
        self.screenshot_rectangle = screenshot_rectangle
        self.overrideredirect(True)
        # app.attributes('-fullscreen', True)
        tk.Button(self, text="OCR", command=self.run_ocr).pack()
        tk.Button(self, text="Kopiuj", command=self.copy).pack()
        tk.Button(self, text="Zapisz", command=self.save).pack()
        tk.Button(self, text="Anuluj", command=self.close_window).pack()

    def close_window(self):
        empty.App.destroy_windows()
        self.destroy()
    def run_ocr(self):
        self.parent.open_ocr_window(self.event, self.screenshot_rectangle)
        self.destroy()
        self.close_window()

    def copy(self):
        self.screenshot_rectangle.copy_ss()
        self.destroy()
        self.close_window()


    def save(self):
        new_name = filedialog.asksaveasfilename(defaultextension=".png", title="Zapisz jako...")
        if new_name:
            shutil.copy(set_f.ss_path, new_name)
        self.destroy()
        self.close_window()




