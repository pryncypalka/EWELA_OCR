import keyboard
from window_tree import main_empty_app as empty
import tray_icon
import threading
import os
from settings import settings_file as set_f
import win32gui
import win32con

def exit():
    os._exit(1)

def message_handler(hwnd, msg, wparam, lparam):
    if msg == win32con.WM_POWERBROADCAST:
        if wparam == win32con.PBT_APMSUSPEND:
            pass
        elif wparam == win32con.PBT_APMRESUMEAUTOMATIC:
            tray_icon.restart_program()
            pass
    return True

def icon_processing():
    tray_icon.TrayIcon()


def main():


    set_f.init_ewelaocr_folder()
    settings = set_f.read_settings()

    empty_app = empty.App()


    tray_icon_thread = threading.Thread(target=icon_processing)
    tray_icon_thread.start()


    pumpMessages_thread = threading.Thread(target=win32gui.PumpMessages)
    pumpMessages_thread.start()


    if settings["second_key"] == "None":
        keyboard.add_hotkey(settings["first_key"], empty_app.open_windows)
    else:
        keyboard.add_hotkey(settings["first_key"] + "+" + settings["second_key"], empty_app.open_windows)

    empty_app.mainloop()
    # tray.stop()
    # keyboard.unhook_all()

if __name__ == "__main__":
    main()

