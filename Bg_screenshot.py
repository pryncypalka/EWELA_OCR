from PIL import Image
from io import BytesIO
import mss
import mss.tools


class Bg_screenshot:
    def __init__(self, monitor_index):
        self._monitor_index = monitor_index

    def making_ss(self):
        with mss.mss() as sct:
            monitor = sct.monitors[self._monitor_index + 1]

            screenshot = sct.grab(monitor)
            image_data = mss.tools.to_png(screenshot.rgb, screenshot.size)
            image = Image.open(BytesIO(image_data))

        return image

