import pytesseract
from PIL import Image

image_path = "./images/circular_text.jpg" 
text = pytesseract.image_to_string(Image.open(image_path),lang = "eng")
print(text)