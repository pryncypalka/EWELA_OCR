import keyboard
import main_empty_app as empty
import tray_icon
import threading
import os
import settings_file as set_f

icon_need = True


def icon_processing():
    tray_icon.TrayIcon()


def main():
    global icon_need
    settings = set_f.read_settings()
    empty_app = empty.App()

    if icon_need:
        tray_icon_thread = threading.Thread(target=icon_processing)
        tray_icon_thread.start()
        icon_need = False
    else:
        pass

    if settings["second_key"] == "None":
        keyboard.add_hotkey(settings["first_key"], empty_app.open_windows)
    else:
        keyboard.add_hotkey(settings["first_key"] + "+" + settings["second_key"], empty_app.open_windows)

    empty_app.mainloop()
    # tray.stop()
    # keyboard.unhook_all()


def exit():
    os._exit(1)


if __name__ == "__main__":
    main()

