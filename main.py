import keyboard
import screenshot_ocr as ss_maker
import settings_file as s_file
import settings_window as s_w
import main_window as main_window
import specs_check as spec
import main_empty_app as empty
import icon
def start_program():
    empty_app = empty.App()
    empty_app.open_windows()
    empty_app.mainloop()
def main():
    keyboard.add_hotkey('print_screen', start_program)
    keyboard.wait()







    


if __name__ == "__main__":
    main()

