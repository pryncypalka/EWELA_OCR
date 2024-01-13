from SSAction.SSActionDecorator import SSActionDecorator
import pytesseract
from PIL import Image
from settings import settings_file as set_f


class OCRSSDecorator(SSActionDecorator):
    def __init__(self, decorated_ss_action):
        super().__init__(decorated_ss_action)
        self.text = ""

    def action(self):
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

