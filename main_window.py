import tkinter as tk
import specs_check as spec
import right_button_window as options
import screenshot_ocr as ss_ocr
import text_ocr_window as ocr_txt
import main_empty_app as empty
class MainApp(tk.Toplevel):
    def __init__(self, monitor_index, parent):
        super().__init__(parent)
        self.iconbitmap("EwelaOCR.ico")
        self.title("EwelaOCR")
        self.old_x = None
        self.old_y = None
        self.last_x = None
        self.last_y = None
        self.options_window = None
        self.parent = parent
        self.monitor_index = monitor_index
        self.attributes('-alpha', 0.4)
        self.overrideredirect(True)
        self.attributes('-transparentcolor', 'blue')

        self.geometry(f"{spec.monitors[monitor_index].width}x{spec.monitors[monitor_index].height}+"
                        f"{spec.monitors[monitor_index].x}+{spec.monitors[monitor_index].y}")



        self.canvas = tk.Canvas(self, width=spec.monitors[monitor_index].width,
                                height=spec.monitors[monitor_index].height, bg="black")
        self.canvas.place(x=0, y=0)

        tk.Label(self.canvas, text="OCR: Zaznacz obszar ekranu do wyszukania tekstu", bg="black", fg="red",
                 font=("Arial", 20)).place(x=5, y=5)

        tk.Button(self.canvas, width=10, height=1, bg="gray", text="ANULUJ", fg="black", command=empty.App.destroy_windows,
                  font=("Arial", 10)).place(x=int(spec.monitors[monitor_index].width) - 125,
                                            y=20)

        self.canvas.bind('<B1-Motion>', self.paint)  # drwaing the line
        self.canvas.bind('<ButtonRelease-1>', self.release_mouse)
        self.canvas.bind('<ButtonPress-1>', self.press)
        # Przypisanie obsługi zdarzeń dla prawego i lewego przycisku myszy
        self.bind("<Button-3>", self.show_options)  # Prawy przycisk myszy
        self.bind("<Button-1>", self.close_options)  # Lewy przycisk mys

        self.bind("<Escape>", self.close_window)

    def close_window(self, event):
        # Zamknięcie okna po wciśnięciu klawisza Esc
        # self.parent.destroy()
        empty.App.destroy_windows()

    def paint(self, e):
        if self.old_x and self.old_y:
            self.canvas.delete("all")
            self.canvas.create_rectangle(self.old_x, self.old_y, e.x, e.y,  fill="blue", outline="white", width=2)

    def press(self, e):
        self.old_x = e.x
        self.old_y = e.y
        self.last_x = e.x
        self.last_y = e.y


    def release_mouse(self, e):
        self.last_x = e.x
        self.last_y = e.y
        self.old_x, self.old_y = min(self.old_x, self.last_x), min(self.old_y, self.last_y)
        self.last_x, self.last_y = max(self.old_x, self.last_x), max(self.old_y, self.last_y)

        if self.calculate_rectangle_area():
            screenshot_rectangle = ss_ocr.ScreenShotOCR(self.old_x, self.old_y, e.x, e.y, self.monitor_index)
            ocr_done = screenshot_rectangle.read_text_from_picture()
            if ocr_done:
                ocr_win = ocr_txt.TextOCR(self.parent, screenshot_rectangle.text)

                y_diff = self.last_y - self.old_y
                y_old_root = e.y_root - y_diff

                if spec.monitors[self.monitor_index].width - e.x_root > (int(spec.monitors[self.monitor_index].width / 5)):
                    ocr_win.geometry(f"{int(spec.monitors[self.monitor_index].width/5)}x"
                                     f"{int(spec.monitors[self.monitor_index].height/3)}"
                                     f"+{e.x_root}+{y_old_root}")
                else:
                    x_diff = self.last_x - self.old_x
                    x_old_root = e.x_root - x_diff
                    ocr_win.geometry(f"{int(spec.monitors[self.monitor_index].width / 5)}x"
                                     f"{int(spec.monitors[self.monitor_index].height / 3)}"
                                     f"+{x_old_root -int(spec.monitors[self.monitor_index].width / 5) }+{y_old_root}")
                empty.App.destroy_windows()



        # self.canvas.delete("all")
        # self.canvas.create_rectangle(self.old_x, self.old_y, e.x, e.y, fill="white",
        #                              outline="white", width=2)

    def show_options(self, event):
        if self.options_window is not None:
            self.options_window.destroy()

        # Tworzenie nowego okna z opcjami
        self.options_window = options.RButton(self.parent)
        self.options_window.geometry(f"+{event.x_root}+{event.y_root}")

        # Usuwanie domyślnych ikon
        self.options_window.iconbitmap(default='')  # Usuwanie ikony z paska tytułowego

    def close_options(self, event):
        if self.options_window is not None:
            self.options_window.destroy()

    def calculate_rectangle_area(self):
        x1, y1 = min(self.old_x, self.last_x), min(self.old_y, self.last_y)
        x2, y2 = max(self.old_x, self.last_x), max(self.old_y, self.last_y)

        width = abs(x2 - x1)
        height = abs(y2 - y1)

        area = width * height
        if area > 100:
            return True

