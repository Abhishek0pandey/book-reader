import pytesseract
from PIL import Image

img=Image.open("275.jpg")
text=pytesseract.image_to_string(img)
print(text)