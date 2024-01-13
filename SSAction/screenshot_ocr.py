import pytesseract
import mss
import mss.tools

from PIL import Image
from settings import settings_file as set_f
from SSAction.SSAction import SSAction


class ScreenShotOCR(SSAction):
    def __init__(self, old_x, old_y, last_x, last_y, monitor_index):
        self.monitor_index = monitor_index
        self.text = None
        self.old_x = old_x
        self.old_y = old_y
        self.last_x = last_x
        self.last_y = last_y
        self.action()

    def action(self):
        try:
            with mss.mss() as sct:
                x1, y1, x2, y2 = self.old_x, self.old_y, self.last_x, self.last_y
                monitor = sct.monitors[self.monitor_index+1]
                monitor_bbox = (monitor["left"] + x1 + 2, monitor["top"] + y1 + 2,
                                monitor["left"] + x2 - 2, monitor["top"] + y2 - 2)
                screenshot = sct.grab(monitor_bbox)

                mss.tools.to_png(screenshot.rgb, screenshot.size, output=set_f.ss_path)
        except:
            return False
        else:
            return True

    def get_size(self):
        image = Image.open(set_f.ss_path)
        width, height = image.size
        return width, height












