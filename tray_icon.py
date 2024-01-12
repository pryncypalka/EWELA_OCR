import settings_window as win_icon
import EwelaOCR
from pystray import Icon, Menu, MenuItem
from PIL import Image
import sys
import os
from settings import settings_file as set_f
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

class TrayIcon:
    def __init__(self):
        image = Image.open(set_f.icon_png_path)  # Wstaw tutaj ścieżkę do twojej ikony (plik .png)
        menu = Menu(MenuItem('Settings', self.open_window), MenuItem('Exit', self.on_quit))
        self.icon = Icon("EwelaOCR", image, "EwelaOCR", menu)
        self.icon.run()
        self.window_icon = None

    def open_window(self, icon, item):
        self.window_icon = win_icon.SettingsWindow(self)


    def on_quit(self,icon, item):
        icon.stop()
        EwelaOCR.exit()
    def stop(self):
        self.icon.stop()

    def restart_main_app(self):
        self.window_icon.destroy()
        restart_program()










