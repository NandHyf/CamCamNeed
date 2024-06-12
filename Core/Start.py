import Extract
import Plot

if __name__ == "__main__":
    fls_dict = Extract.GetFls(Extract.GetFolders())
    kl, vl = Plot.SortDict(fls_dict)
    Plot.Bar(kl, vl)