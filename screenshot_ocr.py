import pytesseract
from PIL import ImageGrab

class ScreenShotOCR:
    def __init__(self, old_x, old_y, last_x, last_y):
        self.text = None
        self.old_x = old_x
        self.old_y = old_y
        self.last_x = last_x
        self.last_y = last_y
    def read_text_from_picture(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\teserrakcik\tesseract'  # Ścieżka do pliku wykonywalnego Tesseract OCR



        try:
            ss = ImageGrab.grab(bbox=(self.old_x, self.old_y, self.last_x, self.last_y))
            picture = ss.convert("RGB")
            text = pytesseract.image_to_string(picture)
            if not text.strip():
                print("Nie wykryto żadnego tekstu.")
            else:
                print("Wykryty tekst:")
                print(text)
        except pytesseract.TesseractError:
            print("Wystąpił błąd podczas przetwarzania obrazu Tesseract.")
        except:
            print("inny blad przetwarzania obrazu ")





