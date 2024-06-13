import Extract
import Plot
from Model import PreConfig

if __name__ == "__main__":
    fls_dict = Extract.GetFls(Extract.GetFolders())
    i = input("[S]pecific Focal Length or [C]lassic Focal Length: ")

    while True:
        if i == "s" or i == "S":
            Plot.Charts(fls_dict).Bar()
            break

        elif i == "c" or i == "C":
            Plot.Charts(fls_dict).Bar(PreConfig.classicFLs)
            break

        else:
            print("Unsupported Label")
    