from SSAction.SSActionDecorator import SSActionDecorator
from tkinter import filedialog

class SaveSSDecorator(SSActionDecorator):
    def __init__(self, decorated_ss_action):
        super().__init__(decorated_ss_action)


    def action(self):
        new_name = filedialog.asksaveasfilename(defaultextension=".png", title="Zapisz jako...")
        return new_name
