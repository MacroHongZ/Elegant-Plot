import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

data = pd.read_csv('data.csv')
xticklabels = list(data.columns)
data = data.to_numpy()

x_value = (np.arange(1, data.shape[1] + 1)).repeat(data.shape[0]) + np.random.randn(300) * 0.02
y_value = data.T.flatten()
dot_color = '#757576'


def mybox(style='ggplot', facecolors=('#d87c7c', '#919e8b', '#d7ab82', '#6e7074', '#61a0a8'), Title='Title',
          Xlabel='Xlabel', Ylabel='Ylabel'):
    plt.style.use(style)
    matplotlib.rcParams['font.family'] = 'serif'

    fig = plt.figure(dpi=300)
    ax = fig.subplots()

    box = ax.boxplot(data, widths=0.2, patch_artist=True, zorder=1)

    lines = box['medians'] + box['whiskers'] + box['caps'] + box['boxes']
    for line in lines:
        line.set(color='#757576', linewidth=1.5)

    for i, line in enumerate(box['boxes']):
        line.set(facecolor=facecolors[i])

    ax.scatter(x_value, y_value, s=8, c=dot_color, alpha=0.8, zorder=2)

    ax.set_xticks(np.arange(1, data.shape[1] + 1), xticklabels)
    ax.set_xlabel(Xlabel, labelpad=10)
    ax.set_ylabel(Ylabel)
    ax.set_title(Title, pad=16, fontdict={'fontsize': 24})

    plt.tight_layout()
    plt.savefig('boxplot.pdf')
    plt.show()


mybox()
