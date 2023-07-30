import settings_window as win_icon
import main
from pystray import Icon, Menu, MenuItem
from PIL import Image


class TrayIcon:
    def __init__(self):
        image = Image.open("EwelaOCR.png")  # Wstaw tutaj ścieżkę do twojej ikony (plik .png)
        menu = Menu(MenuItem('Settings', self.open_window), MenuItem('Exit', self.on_quit))
        icon = Icon("EwelaOCR", image, "EwelaOCR", menu)
        icon.run()
        self.window_icon = None

    def open_window(self, icon, item):
        self.window_icon = win_icon.IconApp()

    def on_quit(self,icon, item):
        icon.stop()
        main.exit()










