from SSAction.SSActionDecorator import SSActionDecorator

from io import BytesIO
import win32clipboard
from PIL import Image
from settings import settings_file as set_f


class CopySSDecorator(SSActionDecorator):
    def __init__(self, decorated_ss_action):
        super().__init__(decorated_ss_action)

    def action(self):
        image = Image.open(set_f.ss_path)

        output = BytesIO()
        image.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

