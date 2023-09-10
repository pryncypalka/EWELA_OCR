import keyboard
import main_empty_app as empty
import tray_icon
import threading
import os
import time
import settings_file as set_f
import win32gui
import win32con

icon_need = True

def exit():

    os._exit(1)
def restart_60_min():
    start_time = time.time()
    restart_interval = 3600

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= restart_interval:
            start_time = current_time

            if len(empty.App.main_apps) == 0:
                tray_icon.restart_program()

        time.sleep(60)

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
    global icon_need

    set_f.init_ewelaocr_folder()
    settings = set_f.read_settings()

    empty_app = empty.App()

    if icon_need:
        tray_icon_thread = threading.Thread(target=icon_processing)
        tray_icon_thread.start()
        icon_need = False
    else:
        pass

    pumpMessages_thread = threading.Thread(target=win32gui.PumpMessages)
    pumpMessages_thread.start()
    restart_thread = threading.Thread(target=restart_60_min)
    restart_thread.start()

    if settings["second_key"] == "None":
        keyboard.add_hotkey(settings["first_key"], empty_app.open_windows)
    else:
        keyboard.add_hotkey(settings["first_key"] + "+" + settings["second_key"], empty_app.open_windows)

    empty_app.mainloop()
    # tray.stop()
    # keyboard.unhook_all()

if __name__ == "__main__":
    main()

