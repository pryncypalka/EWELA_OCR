import tkinter as tk
import settings_file as settings
import keyboard
import main
class IconApp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # self.overrideredirect(True)
        self.bind("<Escape>", self.close_window)
        self.geometry("400x400+720+300")

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

        # Przycisk do ustawiania skrótu
        self.set_shortcut_button = tk.Button(self, text="Ustaw skrót", command=self.update_shortcut)
        self.set_shortcut_button.pack(pady=20)

        # Zmienne przechowujące ustawione klawisze
        self.shortcut_key1 = ""
        self.shortcut_key2 = ""

        # Przypisanie funkcji do zdarzeń naciśnięcia klawiszy
        self.shortcut_entry1.bind("<KeyPress>", self.on_key_press1)
        self.shortcut_entry2.bind("<KeyPress>", self.on_key_press2)
        keyboard.unhook_all()

    def close_window(self, event):
        # Zamknięcie okna po wciśnięciu klawisza Esc
        self.destroy()

    def update_shortcut(self):
        if self.shortcut_key1 == "":
            self.shortcut_key1 = "None"
        if self.shortcut_key2 == "":
            self.shortcut_key2 = "None"

        if self.shortcut_key2 == "None" and self.shortcut_key2 == "None":
            pass
        else:
            settings.change_settings("first_key", self.shortcut_key1)
            settings.change_settings("second_key", self.shortcut_key2)


    def on_key_press1(self, event):
        # Automatyczne wpisanie naciśniętego klawisza do pierwszego pola tekstowego
        key = event.keysym
        self.shortcut_entry1.delete(0, tk.END)
        self.shortcut_entry1.insert(0, key)
        self.shortcut_key1 = key

    def on_key_press2(self, event):
        # Automatyczne wpisanie naciśniętego klawisza do drugiego pola tekstowego
        key = event.keysym
        self.shortcut_entry2.delete(0, tk.END)
        self.shortcut_entry2.insert(0, key)
        self.shortcut_key2 = key

