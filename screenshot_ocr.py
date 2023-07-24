import pytesseract
import mss
import mss.tools
from PIL import Image
class ScreenShotOCR:
    def __init__(self, old_x, old_y, last_x, last_y, monitor_index):
        self.monitor_index = monitor_index
        self.text = None
        self.old_x = old_x
        self.old_y = old_y
        self.last_x = last_x
        self.last_y = last_y
    def read_text_from_picture(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\teserrakcik\tesseract'  # Ścieżka do pliku wykonywalnego Tesseract OCR



        try:
            with mss.mss() as sct:
                x1, y1 = min(self.old_x, self.last_x), min(self.old_y, self.last_y)
                x2, y2 = max(self.old_x, self.last_x), max(self.old_y, self.last_y)

                # Wykonanie zrzutu ekranu na wybranym obszarze i monitorze
                monitor = sct.monitors[self.monitor_index+1]
                monitor_bbox = (monitor["left"] + x1, monitor["top"] + y1, monitor["left"] + x2, monitor["top"] + y2)
                screenshot = sct.grab(monitor_bbox)
                output = "screenshot.png"
                mss.tools.to_png(screenshot.rgb, screenshot.size, output=output)

                # Wywołanie tesseract do rozpoznawania tekstu z zrzutu ekranu
                text = pytesseract.image_to_string(Image.open("screenshot.png"))
                if not text.strip():
                        print("Nie wykryto żadnego tekstu.")
                else:
                    print("Wykryty tekst:")
                    print(text)
        except pytesseract.TesseractError:
            print("Wystąpił błąd podczas przetwarzania obrazu Tesseract.")






