import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn

data = pd.read_csv('data.csv')
x_value = data.iloc[:, 0]
y_value = data.iloc[:, 1]


def scatter_kde(style='ggplot', color='#d87c7c', Title='Title', Xlabel='Xlabel', Ylabel='Ylabel'):
    plt.style.use(style)
    matplotlib.rcParams['font.family'] = 'serif'

    fig = plt.figure(dpi=300)
    gs = fig.add_gridspec(2, 2, wspace=0.01, hspace=0.01, width_ratios=[0.8, 0.2], height_ratios=[0.2, 0.8])
    ax = fig.add_subplot(gs[1, 0])
    ax1 = fig.add_subplot(gs[0, 0], sharex=ax)
    ax2 = fig.add_subplot(gs[1, 1], sharey=ax)

    ax.scatter(x_value, y_value, c=color)
    seaborn.kdeplot(x=x_value, ax=ax1, color=color)
    seaborn.kdeplot(y=y_value, ax=ax2, color=color)

    ax.set_xlabel(Xlabel)
    ax.set_ylabel(Ylabel)
    ax1.set_title(Title, pad=16, fontdict={'fontsize': 24})

    ax1.get_xaxis().set_visible(False)
    ax1.get_yaxis().set_visible(False)
    ax2.get_xaxis().set_visible(False)
    ax2.get_yaxis().set_visible(False)

    plt.tight_layout()
    plt.savefig('scatter_kde.pdf')
    plt.show()


scatter_kde(style='ggplot', color='#d87c7c', Title='Title', Xlabel='Xlabel', Ylabel='Ylabel')
