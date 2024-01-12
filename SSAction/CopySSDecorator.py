from SSAction.SSActionDecorator import SSActionDecorator

class CopySSDecorator(SSActionDecorator):
    def __init__(self, decorated_ss_action):
        super().__init__(decorated_ss_action)

    def get_ss(self, ss_object):
        super().get_ss(ss_object)
        # Dodatkowe działanie - kopiowanie screenshotu
        print("Screenshot copied.")




    def action(self):
        image_path = set_f.ss_path
        image = Image.open(image_path)

        output = BytesIO()
        image.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

