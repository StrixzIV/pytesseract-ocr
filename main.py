import pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image = Image.open('testocr.png')
text = tess.image_to_string(image, lang = 'eng')

print(text)