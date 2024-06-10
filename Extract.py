import os
from exif import Image
import Model

dirs = []

while True:
    key = str(input("Photo Directory or [E]nd: "))

    if key != "e" and key != "E":
        dirs.append(key)

    elif key == "e" or key == "E":
        break


for d in dirs:
    try:
        photos = os.listdir(d)

        for photo in photos:

            with open(d + "\\" + photo, 'rb') as image_file:
                my_image = Image(image_file)

    
    except FileNotFoundError:
        print("Worng Path: ", dir)

    