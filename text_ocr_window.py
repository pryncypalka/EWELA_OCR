import tkinter as tk
import main_empty_app as empty
from PIL import Image, ImageTk
import settings_file as set_f
class TextOCR(tk.Toplevel):
    def __init__(self, parent, ocr_text):
        super().__init__(parent)
        self.parent = parent
        self.ocr_text = ocr_text

        # Utwórz główny kontener
        main_frame = tk.Frame(self)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Kontener dla obrazu
        image_frame = tk.Frame(main_frame)
        image_frame.pack(side=tk.LEFT)

        # Kontener dla tekstu
        text_frame = tk.Frame(main_frame)
        text_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        image = Image.open(set_f.ss_path)
        self.photo = ImageTk.PhotoImage(image)
        tk.Label(image_frame, image=self.photo).pack()

        tk.Label(text_frame, text="Pamiętaj zawsze sprawdzać poprawność!", fg="red", font=("Arial", 10)).pack()

        text_widget = tk.Text(text_frame, font=("Arial", 10))
        text_widget.insert(tk.END, self.ocr_text)
        text_widget.pack(fill=tk.BOTH, expand=True)
        # left_frame = tk.Frame(self)
        # left_frame.pack(side=tk.LEFT)
        #
        # right_frame = tk.Frame(self)
        # right_frame.pack(side=tk.RIGHT)
        #
        # image = Image.open(set_f.ss_path)
        # self.photo = ImageTk.PhotoImage(image)
        # tk.Label(left_frame, image=self.photo).pack()
        #
        #
        # tk.Label(right_frame, text="Pamietaj zawsze sprawdzić poprawność!", fg="red",
        #          font=("Arial", 10)).pack()
        #
        # text_widget = tk.Text(right_frame, font=("Arial", 10))
        # text_widget.insert(tk.END, self.ocr_text)
        # text_widget.pack(fill=tk.BOTH, expand=True)

        self.bind("<Escape>", self.close_window)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def close_window(self, event):
        empty.App.destroy_windows()
    def on_closing(self):
        empty.App.destroy_windows()
        self.destroy()
