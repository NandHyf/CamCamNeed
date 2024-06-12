import matplotlib.pyplot as plt
import numpy as np


def SortDict(fls:dict):
    kl = []
    vl = []
    kl = sorted(fls.keys())
    for k in kl:
        vl.append(fls[k])
    
    return kl, vl


def Bar(x:list, y:list):
   plt.style.use('_mpl-gallery')

   fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
   ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
   ax.set_xlabel('Focal Length')

   plt.show()


if __name__ == "__main__":
    pass