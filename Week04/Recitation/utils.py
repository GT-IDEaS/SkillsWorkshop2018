import numpy as np
import matplotlib.pyplot as plt


def PlotPC1PC2(PCs, y):

    fig = plt.figure(num = 1)
    ax1 = fig.add_subplot(111)

    for l, c, m in zip(range(0, 3), ('blue', 'red', 'green'), ('^', 's', 'o')):
        ax1.scatter(PCs[y == l, 0], PCs[y == l, 1],
                color=c,
                label='class %s' % l,
                alpha=0.5,
                marker=m)
    ax1.set_xlabel('PC1')
    ax1.set_ylabel('PC2')
    ax1.set_title('Score Plot')
    plt.legend(loc = 'best')
    plt.show()
