import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

data = pd.read_csv('data.csv')
labels = data.columns

mul_series = data.iloc[:, :-1].to_numpy().T
circle = mul_series[:, 0]
mul_series = np.hstack((mul_series, circle[:, np.newaxis]))
xticks = data.iloc[:, -1].to_list()

category_num = mul_series.shape[1]
series_num = mul_series.shape[0]
max_value = mul_series.max()
ylim_max = (max_value // 5 + 1) * 5


def spider(style='ggplot', title='Title', color=['#d87c7c', '#919e8b', '#d7ab82', '#6e7074', '#61a0a8'], fill=True):
    plt.style.use(style)
    matplotlib.rcParams['font.family'] = 'serif'

    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(projection='polar')

    width = 2 * np.pi / (category_num - 1)
    angles = (np.arange(category_num - 1) * width).tolist()
    angles += angles[:1]
    color = color * 10
    for i in range(series_num):
        ax.plot(angles, mul_series[i], color=color[i], linewidth=1, linestyle='solid', label="group A")
        if fill:
            ax.fill(angles, mul_series[i], color=color[i], alpha=0.1)

    ax.set_title(title, pad=35, fontdict={'fontsize': 24})
    ax.set_xticks(angles[:-1], xticks)

    ax.set_ylim(0, ylim_max)
    ax.set_rlabel_position(0)
    yticks = range(0, ylim_max, 5)
    ax.set_yticks(yticks, [str(i) for i in yticks])

    plt.tight_layout()
    plt.savefig('spyder.pdf')
    plt.show()


spider(style='ggplot', title='Title', color=['#d87c7c', '#919e8b', '#d7ab82', '#6e7074', '#61a0a8'], fill=True)
