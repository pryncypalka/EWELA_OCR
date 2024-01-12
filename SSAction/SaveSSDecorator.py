from SSAction.SSActionDecorator import SSActionDecorator

class SaveSSDecorator(SSActionDecorator):
    def __init__(self, decorated_ss_action, save_path):
        super().__init__(decorated_ss_action)
        self.save_path = save_path

    def action(self, args):
        super().action(args)
        # Dodatkowe działanie - zapisywanie screenshotu
        print(f"Screenshot saved to {self.save_path}.")
