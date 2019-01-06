from pytesseract import image_to_string
from PIL import Image

im = Image.open('/home/ab.gupta1/tannu.jpg')
s = image_to_string(im, lang='eng')

f = open('/home/ab.gupta1/tannu.txt', mode='w')
f.write(s)
f.close()
print(s)
