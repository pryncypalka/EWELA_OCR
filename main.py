import keyboard
import main_empty_app as empty
import tray_icon
import threading
import os
def main():
    empty_app = empty.App()
    keyboard.add_hotkey('print_screen', empty_app.open_windows)

    tray_thread = threading.Thread(target=tray_icon.TrayIcon)
    tray_thread.start()

    empty_app.mainloop()
    keyboard.unhook_all()

def exit():
    os._exit(1)


if __name__ == "__main__":
    main()

