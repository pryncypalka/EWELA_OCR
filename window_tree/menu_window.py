import tkinter as tk
from window_tree import main_empty_app as empty
from tkinter import filedialog
from settings import settings_file as set_f
import shutil
from window_tree.Window import Window
from SSAction.CopySSDecorator import CopySSDecorator
from SSAction.SaveSSDecorator import SaveSSDecorator
class Menu(tk.Toplevel, Window):
    def __init__(self, parent, event, screenshot_rectangle):
        super().__init__(parent)
        self.parent = parent
        self.iconbitmap(set_f.icon_ico_path)
        self.title("EwelaOCR")
        self.event = event
        self.screenshot_rectangle = screenshot_rectangle
        self.overrideredirect(True)
        # app.attributes('-fullscreen', True)
        tk.Button(self, text="OCR", command=self.run_ocr).pack()
        tk.Button(self, text="Kopiuj", command=self.copy).pack()
        tk.Button(self, text="Zapisz", command=self.save).pack()
        tk.Button(self, text="Anuluj", command=self.close_window).pack()

    def close_window(self, event=None):
        empty.App.destroy_windows()
        self.destroy()
    def run_ocr(self):
        self.parent.open_ocr_window(self.event, self.screenshot_rectangle)
        self.destroy()
        self.close_window()

    def copy(self):
        copy_action = CopySSDecorator(self.screenshot_rectangle)
        copy_action.action()
        # self.screenshot_rectangle.copy_ss()
        self.destroy()
        self.close_window()


    def save(self):
        save_action = SaveSSDecorator(self.screenshot_rectangle)
        new_name = save_action.action()
        if new_name:
            self.destroy()
            self.close_window()
            shutil.copy(set_f.ss_path, new_name)





