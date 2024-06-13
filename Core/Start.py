import Extract
import Plot

if __name__ == "__main__":
    fls_dict = Extract.GetFls(Extract.GetFolders())
    Plot.Charts(fls_dict).Bar()