import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn

data = pd.read_csv('data.csv')
x_value = data.iloc[:, 0]
y_value = data.iloc[:, 1]


def scatter(style='ggplot', color='#d87c7c', Title='Title', Xlabel='Xlabel', Ylabel='Ylabel'):
    plt.style.use(style)
    matplotlib.rcParams['font.family'] = 'serif'

    fig = plt.figure(dpi=300)
    ax = fig.subplots()

    ax.scatter(x_value, y_value, c=color)

    ax.set_xlabel(Xlabel)
    ax.set_ylabel(Ylabel)
    ax.set_title(Title, pad=16, fontdict={'fontsize': 24})

    plt.tight_layout()
    plt.savefig('scatter.pdf')
    plt.show()


scatter(style='ggplot', color='#d87c7c', Title='Title',
        Xlabel='Xlabel', Ylabel='Ylabel')
