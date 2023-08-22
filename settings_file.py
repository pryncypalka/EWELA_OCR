import os
import sys

settings_path = ""
ss_path = ""
icon_png_path = ""
icon_ico_path = ""
tesseract_path = ""

default_settings = """lang=pol
first_key=print_screen
second_key=None
auto_run=0
"""

settings_dict = {
            "lang": "pol",
            "first_key": "print_screen",
            "second_key": "None",
            "auto_run": "0"
        }
def check_folder_exists(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return True
    else:
        return False

def create_settings_file():
    global settings_path
    global default_settings

    with open(settings_path, 'w') as settings_file:
        settings_file.write(default_settings)

def read_settings():
    global settings_path
    global settings_dict
    settings = {}
    try:
        with open(settings_path, "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                settings[key] = value
    except FileNotFoundError:
        create_settings_file()
        settings = settings_dict
    except:
        create_settings_file()
        settings = settings_dict
    return settings

def change_settings(key, value):
    global settings_path
    settings = read_settings()
    settings[key] = value
    with open(settings_path, "w") as file:
        for key, value in settings.items():
            file.write(f"{key}={value}\n")
def get_EwelaOCR_path():
    appdata_roaming_path = os.path.join(os.environ['APPDATA'])
    ewelaOCR_path = os.path.join(appdata_roaming_path, 'EwelaOCR')
    return ewelaOCR_path

def init_ewelaocr_folder():
    ewelaOCR_path = get_EwelaOCR_path()
    if not check_folder_exists(ewelaOCR_path):
        os.makedirs(ewelaOCR_path, exist_ok=True)
    global settings_path
    global ss_path
    global icon_png_path
    global icon_ico_path
    global tesseract_path

    settings_path = os.path.join(ewelaOCR_path, 'settings.txt')
    ss_path = os.path.join(ewelaOCR_path, 'screenshot.png')
    if getattr(sys, 'frozen', False):
        exe_dir = os.path.dirname(sys.executable)
        exe_path = os.path.join(exe_dir, 'EwelaOCR.exe')

        icon_png_path = os.path.join(exe_path, 'EwelaOCR.png')
        icon_ico_path = os.path.join(exe_path, 'EwelaOCR.ico')
        tesseract_path = os.path.join(exe_path, r'Tesseract-OCR\tesseract')


