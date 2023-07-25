import tkinter as tk

class TextOCR(tk.Toplevel):
    def __init__(self, parent, ocr_text):
        super().__init__(parent)
        self.parent = parent
        self.ocr_text = ocr_text
        # self.overrideredirect(True)
        # app.attributes('-fullscreen', True)

        tk.Button(self, text="Anuluj", command=parent.destroy).pack()
        text_widget = tk.Text(self, font=("Arial", 10))
        text_widget.insert(tk.END, self.ocr_text)
        text_widget.pack(fill=tk.BOTH, expand=True)



