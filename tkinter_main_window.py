import tkinter as tk
from tkinter import ttk
import specs_check as spec


class MainApp(tk.Toplevel):
    def __init__(self, monitor_index, parent):
        super().__init__(parent)
        self.old_x = None
        self.old_y = None
        self.ss_x = None
        self.ss_y = None
        self.monitor_index = monitor_index

        # self.overrideredirect(True)
        self.attributes('-alpha', 0.2)
        # app.attributes('-fullscreen', True)
        self.title(f"Okno {monitor_index + 1}")
        self.geometry(f"{spec.monitors[monitor_index].width}x{spec.monitors[monitor_index].height}+"
                     f"{spec.monitors[monitor_index].x}+{spec.monitors[monitor_index].y}")



        self.canvas = tk.Canvas(self, width=spec.monitors[monitor_index].width,
                                height=spec.monitors[monitor_index].height, bg="black")
        self.canvas.place(x=0, y=0)

        tk.Label(self.canvas, text="OCT: Zaznacz obszar ekranu do wyszukania tekstu", bg="black", fg="red",
                 font=("Arial", 25)).place(x=5, y=5)

        tk.Button(self.canvas, width=10, height=5, bg="gray", text="ANULUJ", fg="black", command=parent.destroy,
                  font=("Arial", 15)).place(x=int(spec.monitors[monitor_index].width) - (int(spec.monitors[monitor_index].width)*0.1),
                                            y=20)


        # self.canvas.bind('<B1-Motion>', self.paint)  # drwaing the line
        # self.canvas.bind('<ButtonRelease-1>', self.rele)
        # self.canvas.bind('<ButtonPress-1>', self.press)
        # # Przypisanie obsługi zdarzeń dla prawego i lewego przycisku myszy
        # self.bind("<Button-3>", self.show_options)  # Prawy przycisk myszy
        # self.bind("<Button-1>", self.close_options)  # Lewy przycisk mys
        # tk.Button(self.canvas, width=10, height=5, bg="white", text="ANULUJ", fg="black", command='anuluj',
        #        font=("Arial", 15)).place(x=int(self.winfo_width()) - 125, y=5)
