import pytesseract
import mss
import mss.tools
from io import BytesIO
import win32clipboard
from PIL import Image
from settings import settings_file as set_f

class ScreenShotOCR:
    def __init__(self, old_x, old_y, last_x, last_y, monitor_index):
        self.monitor_index = monitor_index
        self.text = None
        self.old_x = old_x
        self.old_y = old_y
        self.last_x = last_x
        self.last_y = last_y
        self.ss_done = self.making_ss()




    def making_ss(self):
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


    def read_text_from_picture(self):
        if self.ss_done:
            pytesseract.pytesseract.tesseract_cmd = set_f.tesseract_path
            lang = "pol"
            try:
                image = Image.open(set_f.ss_path)

                # Wywołanie tesseract do rozpoznawania tekstu z zrzutu ekranu
                self.text = pytesseract.image_to_string(image, lang=lang)
                # self.text = pytesseract.image_to_pdf_or_hocr(Image.open(set_f.ss_path), extension='hocr')
            except pytesseract.TesseractError:
                print("Wystąpił błąd podczas przetwarzania obrazu Tesseract.")
            else:
                return True


    def copy_ss(self):
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

    def get_size(self):
        image = Image.open(set_f.ss_path)
        width, height = image.size
        return width, height












