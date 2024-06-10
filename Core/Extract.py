import os
from exif import Image
import Model


dirs = []

while True:
    pd = str(input("Photo Directory or [E]nd: "))
    
    if pd != "e" and pd != "E":
        
        try:
            pd_frameSize = int(input("Frame Size in this folder: " + Model.PreConfig.fs_options + "Frame Size in this folder: "))

        except:
            input("Unsupported Frame Size")
            exit()

        if pd_frameSize in Model.PreConfig.frameSizes:
            mf = Model.Folder()
            mf.path = pd
            mf.frameSize = pd_frameSize

            dirs.append(mf)

        else:
            print("Unsupported Frame Size")
            exit()

    elif pd == "e" or pd == "E":
        break

    else:
        input("Unsupported Inputs")
        exit()


for d in dirs:
    try:
        photos = os.listdir(d)

        for photo in photos:

            with open(d + "\\" + photo, 'rb') as image_file:
                my_image = Image(image_file)

    
    except FileNotFoundError:
        print("Worng Path: ", dir)

    