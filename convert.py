#!/usr/bin/python3
import os
from PIL import Image
directory = 'images'

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    if os.path.isfile(file):
        #print(file)
        im = Image.open(file).convert("RGB")
        new_im = im.rotate(90).resize((128,128)).save("/opt/icons/" + filename, "JPEG")
