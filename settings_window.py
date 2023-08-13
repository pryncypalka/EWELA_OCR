import tkinter as tk
import settings_file as settings
import keyboard
class SettingsWindow(tk.Toplevel):
    def __init__(self, icon_object):
        super().__init__()
        self.icon_object = icon_object
        self.bind("<Escape>", self.close_window)
        self.protocol("WM_DELETE_WINDOW", self.close_window_cross)
        self.geometry("400x400+720+300")
        self.iconbitmap("EwelaOCR.ico")

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
        self.sett = settings.read_settings()
        self.shortcut_entry1.insert(0, self.sett["first_key"])
        self.shortcut_entry2.insert(0, self.sett["second_key"])

        # Przycisk do ustawiania skrótu
        self.set_shortcut_button = tk.Button(self, text="Wyczyść", command=self.clean_entry_field)
        self.set_shortcut_button.pack(pady=10)
        self.set_shortcut_button = tk.Button(self, text="Ustaw skrót", command=self.update_shortcut)
        self.set_shortcut_button.pack(padx=10)

        self.set_shortcut_button = tk.Button(self, text="Ustaw domyślnie", command=self.reset_shortcut)
        self.set_shortcut_button.pack(pady=30)

        # Zmienne przechowujące ustawione klawisze
        self.shortcut_key1 = ""
        self.shortcut_key2 = ""

        # Przypisanie funkcji do zdarzeń naciśnięcia klawiszy
        self.shortcut_entry1.bind("<KeyPress>", self.on_key_press1)
        self.shortcut_entry2.bind("<KeyPress>", self.on_key_press2)




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
            pass
        elif self.shortcut_key1 == self.shortcut_key1:
            pass
        else:
            settings.change_settings("first_key", self.shortcut_key1)
            settings.change_settings("second_key", self.shortcut_key2)


    def on_key_press1(self, event):
        hotkey_event = keyboard.read_event(suppress=True)
        key = hotkey_event.name
        print(key)
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
        settings.create_settings_file()
        self.shortcut_entry1['state'] = 'normal'
        self.shortcut_entry2['state'] = 'normal'
        self.shortcut_entry1.delete(0, tk.END)
        self.shortcut_entry2.delete(0, tk.END)
        self.shortcut_entry1.insert(0, "print_screen")
        self.shortcut_key1 = "print_screen"
        self.shortcut_key2 = "None"

