import matplotlib.pyplot as plt


class Charts():
    def __init__(self, fls) -> None:
        self.fls = fls
        self.x = []
        self.y = []


    def SortDict(self):
        kl = []
        vl = []
        kl = sorted(self.fls.keys())
        for k in kl:
            vl.append(self.fls[k])

        self.x = kl
        self.y = vl
        
        return kl, vl


    def Bar(self):
        Charts.SortDict(self)

        plt.style.use('_mpl-gallery')

        fig, ax = plt.subplots(figsize=(11, 4), layout='constrained')
        rects = ax.bar(self.x, self.y, width=1, edgecolor="white", linewidth=1, tick_label=self.x)
        ax.bar_label(rects, padding=0.2)
        ax.set_xlabel('35 mm Equivalent Focal Length')
        ax.set_ylabel('Number of Photos')
        
        plt.grid(False)
        plt.show()

    def Scatter(self):
        pass
