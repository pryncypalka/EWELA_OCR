from SSAction.SSActionDecorator import SSActionDecorator

class OCRSSDecorator(SSActionDecorator):
    def __init__(self, decorated_ss_action):
        super().__init__(decorated_ss_action)

    def action(self, args):
        super().action(args)
        # Dodatkowe działanie - przetwarzanie odczytu z obrazu (OCR)
        print("OCR processing performed on the screenshot.")
