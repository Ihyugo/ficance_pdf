import os
import glob
import re
from PIL import Image
import img2pdf
import os

pdf_file_name = "output.pdf"
path = "./"
ext = ".jpeg"

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts
files = sorted(glob.glob("./*.png"), key=numericalSort)
match = re.compile("(png)")

for file in files:
    im = Image.open(file)
    im = im.convert("RGB")
    new_file = match.sub("jpeg", file)
    os.remove(file)
    im.save(new_file, quality=100)
    print(file + "converted")

jpeg_file = sorted(glob.glob("./*.jpeg"), key=numericalSort)
with open(pdf_file_name, "wb") as f:
    f.write(img2pdf.convert([i for i in jpeg_file]))

for i in os.listdir(path):
    if i.endswith(ext):
        os.remove(str(i))
