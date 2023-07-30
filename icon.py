import tkinter as tk
from pystray import Icon, Menu, MenuItem
from PIL import Image


class IconApp(tk.Tk):
    def __init__(self):
        super().__init__()

    def on_quit(cls,icon, item):
        icon.stop()
        self.destroy()

    def open_window(self, icon, item):
        window = tk.Toplevel(self)
        window.title("Nowe okno")

# napraw tooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
def setup_tray_icon():
    image = Image.open("../OCR_ewela_remake/EwelaOCR.png")  # Wstaw tutaj ścieżkę do twojej ikony (plik .png)
    menu = Menu(MenuItem('Otwórz', open_window), MenuItem('Wyjdź', on_quit))
    icon = Icon("Program", image, "Program", menu)
    icon.run()


