import tkinter as tk
from settings import specs_check as spec
from window_tree import right_button_window as options
from SSAction import screenshot_ocr as ss_ocr
from window_tree import text_ocr_window as ocr_txt
from window_tree import main_empty_app as empty
from window_tree  import menu_window as menu
from settings import settings_file as set_f
from PIL import ImageTk
import Bg_screenshot as bg_ss
from window_tree.Window import Window
from SSAction.OCRSSDecorator import OCRSSDecorator
class MainApp(tk.Toplevel, Window):
    def __init__(self, monitor_index, parent):
        self.bg_canvas = bg_ss.Bg_screenshot(monitor_index)
        self.background_image = ImageTk.PhotoImage(self.bg_canvas.making_ss())
        super().__init__(parent)
        self.lift()
        self.iconbitmap(set_f.icon_ico_path)
        self.title("EwelaOCR")
        self.old_x = None
        self.old_y = None
        self.last_x = None
        self.last_y = None
        self.options_window = None
        self.menu_window = None
        self.parent = parent
        self.monitor_index = monitor_index
        #self.attributes('-alpha', 0.4)
        self.overrideredirect(True)




        self.geometry(f"{spec.monitors[monitor_index].width}x{spec.monitors[monitor_index].height}+"
                        f"{spec.monitors[monitor_index].x}+{spec.monitors[monitor_index].y}")




        self.canvas = tk.Canvas(self, width=self.background_image.width(), height=self.background_image.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        self.canvas.place(x=0, y=0)

        tk.Button(self.canvas, width=10, height=1, bg="gray", text="ANULUJ", fg="black", command=empty.App.destroy_windows,
                  font=("Arial", 10)).place(x=int(spec.monitors[monitor_index].width) - 125,
                                            y=20)

        self.canvas.bind('<B1-Motion>', self.paint)  # drwaing the line
        self.canvas.bind('<ButtonRelease-1>', self.release_mouse)
        self.canvas.bind('<ButtonPress-1>', self.press)

        self.bind("<Button-3>", self.show_options)  # Prawy przycisk myszy
        self.bind("<Button-1>", self.close_options)  # Lewy przycisk mys
        self.bind("<Button-1>", self.close_menu)
        self.bind("<Escape>", self.close_window)

    def close_window(self, event):
        empty.App.destroy_windows()

    def paint(self, e):
        if self.old_x and self.old_y:

            self.canvas.delete("rectangle")
            self.canvas.create_rectangle(
                self.old_x, self.old_y, e.x, e.y, fill="", outline="red", width=2, tags="rectangle")

    def press(self, e):
        self.old_x = e.x
        self.old_y = e.y
        self.last_x = e.x
        self.last_y = e.y
    def open_ocr_window(self,e,screenshot_rectangle):
        ocr_action = OCRSSDecorator(screenshot_rectangle)
        ocr_done = ocr_action.action()
        width, height = screenshot_rectangle.get_size()
        if ocr_done:
            ocr_win = ocr_txt.TextOCR(self.parent, ocr_action.text)

            y_diff = self.last_y - self.old_y
            y_old_root = e.y_root - y_diff

            x_diff = self.last_x - self.old_x
            x_old_root = e.x_root - x_diff

            ocr_win.geometry(f"{2 * width + 50}x"f"{int( 50+  height)}"
                             f"+{x_old_root}+{y_old_root}")



    def open_menu(self, event, screenshot_rectangle):
        if self.menu_window is not None:
            self.menu_window.destroy()
        y_pos = 0
        x_pos = 0
        y_diff = self.last_y - self.old_y
        y_old_root = event.y_root - y_diff

        x_diff = self.last_x - self.old_x
        x_old_root = event.x_root - x_diff

        # Tworzenie nowego okna z opcjami
        self.menu_window = menu.Menu(self, event, screenshot_rectangle)
        if event.x_root > (spec.monitors[self.monitor_index].width - 60):
            x_pos = x_old_root - 60
        else:
            x_pos = event.x_root

        if event.y_root > (spec.monitors[self.monitor_index].height - 150):
            y_pos = event.y_root - 150
        else:
            y_pos = event.y_root

        self.menu_window.geometry(f"+{x_pos}+{y_pos}")
        # Usuwanie domyślnych ikon
        self.menu_window.iconbitmap(default='')  # Usuwanie ikony z paska tytułowego

    def close_menu(self, event):
        if self.menu_window is not None:
            self.menu_window.destroy()
    
    def release_mouse(self, e):
        self.last_x = e.x
        self.last_y = e.y
        self.old_x, self.old_y = min(self.old_x, self.last_x), min(self.old_y, self.last_y)
        self.last_x, self.last_y = max(self.old_x, self.last_x), max(self.old_y, self.last_y)
        self.canvas.delete("rectangle")
        self.canvas.create_rectangle(
            self.old_x, self.old_y, e.x, e.y, fill="", outline="red", width=2, tags="rectangle")
        if self.calculate_rectangle_area():
            screenshot_rectangle = ss_ocr.ScreenShotOCR(self.old_x, self.old_y, e.x, e.y, self.monitor_index)
            self.open_menu(e, screenshot_rectangle)



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

