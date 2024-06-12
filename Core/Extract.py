import os
from exif import Image
import Model


def GetFolders() -> dict:
    dirs = {}

    while True:
        pd = str(input("Photo Directory or [E]nd: "))
        
        if pd != "e" and pd != "E":
            
            pd_frameSize = str(input("Frame Size in this folder: " + Model.PreConfig.fs_options + "\nFrame Size in this folder: "))

            if pd_frameSize in Model.PreConfig.frameSizes:
                dirs[pd] = Model.PreConfig.frameSizes[pd_frameSize]

            else:
                print("Unsupported Frame Size")

        elif pd == "e" or pd == "E":
            return dirs

        else:
            input("Unsupported Inputs")
            exit()


def GetFls(dirs:dict) -> dict:
    fls = {}

    for dk in dirs.keys():
        try:
            photos = os.listdir(dk)

            for p in photos:

                try:
                    with open(dk + "\\" + p,  'rb') as image_file:
                        my_image = Image(image_file)
                except:
                    print("Worng format:", p)
                    break

                if my_image.has_exif == True:
                    mp = Model.Photo()
                    mp.focal_length = my_image.focal_length

                    if mp.focal_length_in_35mm_film == 0:
                        mp.focal_length_in_35mm_film = round(mp.focal_length * float(dirs[dk]))
                    
                    if mp.focal_length_in_35mm_film not in fls.keys():
                        fls[mp.focal_length_in_35mm_film] = 1
                    
                    elif mp.focal_length_in_35mm_film in fls.keys():
                        fls[mp.focal_length_in_35mm_film] += 1
                
                # unnecessary print
                print(p, my_image.has_exif, mp.focal_length, mp.focal_length_in_35mm_film)

        except FileNotFoundError:
            print("Worng Path: ", dir)
    
    print(fls)
    return fls

if __name__ == "__main__":
    GetFls(GetFolders())