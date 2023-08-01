import keyboard
import main_empty_app as empty
import tray_icon
import threading
import os
import settings_file as set_f
def main():
    settings = set_f.read_settings()
    empty_app = empty.App()
    keyboard.add_hotkey(settings["first_key"], empty_app.open_windows)

    tray_thread = threading.Thread(target=tray_icon.TrayIcon)
    tray_thread.start()

    empty_app.mainloop()
    keyboard.unhook_all()

def exit():
    os._exit(1)


if __name__ == "__main__":
    main()

