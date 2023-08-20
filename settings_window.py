import tkinter as tk
import settings_file as set_f
import keyboard
import os
import winreg
import sys

def add_to_startup(program_name, executable_path):
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    full_executable_path = os.path.abspath(executable_path)

    try:
        key = winreg.HKEY_CURRENT_USER
        with winreg.OpenKey(key, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE) as registry_key:
            winreg.SetValueEx(registry_key, program_name, 0, winreg.REG_SZ, full_executable_path)

    except Exception as e:
        print("An error occurred:", e)


def remove_from_startup(program_name):
    try:
        key = winreg.HKEY_CURRENT_USER
        with winreg.OpenKey(key, r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
                            winreg.KEY_SET_VALUE) as registry_key:
            winreg.DeleteValue(registry_key, program_name)
    except Exception as e:
        print("An error occurred:", e)



class SettingsWindow(tk.Toplevel):
    def __init__(self, icon_object):
        super().__init__()
        self.icon_object = icon_object
        self.bind("<Escape>", self.close_window)
        self.protocol("WM_DELETE_WINDOW", self.close_window_cross)
        self.geometry("400x400+720+300")
        self.iconbitmap("EwelaOCR.ico")
        self.sett = set_f.read_settings()
        self.checkbox_var = tk.IntVar(value=int(self.sett["auto_run"]))

        # Etykieta u góry okna
        self.label = tk.Label(self, text="Ustaw skrót klawiszowy:", font=("Helvetica", 14))
        self.label.pack(pady=10)
        self.label = tk.Label(self, text="Aby nowy skrót zadziałał zrestartuj program:", font=("Helvetica", 10))
        self.label.pack(pady=10)

        # Utworzenie ramki, aby pola tekstowe były w jednej linii
        self.frame = tk.Frame(self)
        self.frame.pack(pady=10)

        # Dodaj pola tekstowe do wprowadzenia klawiszy
        self.shortcut_entry1 = tk.Entry(self.frame, font=("Helvetica", 16), width=10)
        self.shortcut_entry1.pack(side="left")
        self.plus_label = tk.Label(self.frame, text="+", font=("Helvetica", 16))
        self.plus_label.pack(side="left")
        self.shortcut_entry2 = tk.Entry(self.frame, font=("Helvetica", 16), width=10)
        self.shortcut_entry2.pack(side="left")

        self.shortcut_entry1.insert(0, self.sett["first_key"])
        self.shortcut_entry2.insert(0, self.sett["second_key"])

        # Przycisk do ustawiania skrótu
        self.set_shortcut_button = tk.Button(self, text="Wyczyść", command=self.clean_entry_field)
        self.set_shortcut_button.pack(pady=10)
        self.set_shortcut_button = tk.Button(self, text="Ustaw skrót", command=self.update_shortcut)
        self.set_shortcut_button.pack(padx=10)

        self.set_shortcut_button = tk.Button(self, text="Ustaw domyślnie", command=self.reset_shortcut)
        self.set_shortcut_button.pack(pady=30)
        self.checkbox = tk.Checkbutton(self, text="Dodaj do autostartu",  onvalue=1, offvalue=0,variable=self.checkbox_var)
        self.checkbox.pack()

        self.button = tk.Button(self, text="Zatwierdź", command=self.check_checkbox)
        self.button.pack()



        # Zmienne przechowujące ustawione klawisze
        self.shortcut_key1 = ""
        self.shortcut_key2 = ""

        # Przypisanie funkcji do zdarzeń naciśnięcia klawiszy
        self.shortcut_entry1.bind("<KeyPress>", self.on_key_press1)
        self.shortcut_entry2.bind("<KeyPress>", self.on_key_press2)
        keyboard.unhook_all()

    def check_checkbox(self):
        if self.checkbox_var.get() == 1:
            if getattr(sys, 'frozen', False):
                exe_dir = os.path.dirname(sys.executable)
                exe_path = os.path.join(exe_dir, 'EwelaOCR.exe')
                print(exe_path)
                add_to_startup("EwelaOCR", exe_path)
                set_f.change_settings("auto_run", "1")
        else:
            remove_from_startup("EwelaOCR")
            set_f.change_settings("auto_run", "0")

    def close_window(self, event):
        # Zamknięcie okna po wciśnięciu klawisza Esc
        self.icon_object.restart_main_app()

    def close_window_cross(self):
        # Zamknięcie okna po wciśnięciu klawisza Esc
        self.icon_object.restart_main_app()


    def update_shortcut(self):
        if self.shortcut_key1 == "":
            self.shortcut_key1 = "None"
        if self.shortcut_key2 == "":
            self.shortcut_key2 = "None"

        if self.shortcut_key1 == "None":
            return

        if self.shortcut_key1 == self.shortcut_key2:
            return
        elif self.shortcut_key1 != "None" and self.shortcut_key2 == "None":
            set_f.change_settings("first_key", self.shortcut_key1)
            set_f.change_settings("second_key", self.shortcut_key2)
            self.shortcut_entry2.delete(0, tk.END)
            self.shortcut_entry2.insert(0, "None")
            self.shortcut_entry1['state'] = 'readonly'
            self.shortcut_entry2['state'] = 'readonly'
        else:
            set_f.change_settings("first_key", self.shortcut_key1)
            set_f.change_settings("second_key", self.shortcut_key2)
            self.shortcut_entry1['state'] = 'readonly'
            self.shortcut_entry2['state'] = 'readonly'


    def on_key_press1(self, event):
        hotkey_event = keyboard.read_event(suppress=True)
        key = hotkey_event.name
        self.shortcut_entry1.delete(0, tk.END)
        self.shortcut_entry1.insert(0, key)
        self.shortcut_key1 = key
        self.shortcut_entry1['state'] = 'readonly'


    def on_key_press2(self, event):
        hotkey_event = keyboard.read_event(suppress=True)
        key = hotkey_event.name
        self.shortcut_entry2.delete(0, tk.END)
        self.shortcut_entry2.insert(0, key)
        self.shortcut_key2 = key
        self.shortcut_entry2['state'] = 'readonly'

    def clean_entry_field(self):
        self.shortcut_entry1['state'] = 'normal'
        self.shortcut_entry2['state'] = 'normal'
        self.shortcut_entry1.delete(0, tk.END)
        self.shortcut_entry2.delete(0, tk.END)
        self.shortcut_key1 = "None"
        self.shortcut_key2 = "None"

    def reset_shortcut(self):
        set_f.create_settings_file()
        self.shortcut_entry1['state'] = 'normal'
        self.shortcut_entry2['state'] = 'normal'
        self.shortcut_entry1.delete(0, tk.END)
        self.shortcut_entry2.delete(0, tk.END)
        self.shortcut_entry1.insert(0, "print_screen")
        self.shortcut_entry2.insert(0, "None")
        self.shortcut_key1 = "print_screen"
        self.shortcut_key2 = "None"
        self.shortcut_entry1['state'] = 'readonly'
        self.shortcut_entry2['state'] = 'readonly'



