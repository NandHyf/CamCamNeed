import Extract
import Plot
from Model import PreConfig

if __name__ == "__main__":
    fls_dict = Extract.GetFls(Extract.GetFolders())
    Plot.Charts(fls_dict).Bar(PreConfig.famousFLs)