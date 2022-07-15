import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

data = pd.read_csv('data.csv')
groups = list(data.groupby('category'))
datas = [group[1].iloc[:, :2] for group in groups]
category = [group[0] for group in groups]

def Mul_scater(style='ggplot', colors=('#d87c7c', '#919e8b', '#d7ab82', '#6e7074', '#61a0a8'), Title='Title', Xlabel='Xlabel', Ylabel='Ylabel'):
    plt.style.use(style)
    matplotlib.rcParams['font.family'] = 'serif'

    fig = plt.figure(dpi=300)
    ax = fig.subplots()

    for i, data in enumerate(datas):
        ax.scatter(data.x_value, data.y_value, c=colors[i], label=category[i])

    ax.set_xlabel(Xlabel)
    ax.set_ylabel(Ylabel)
    ax.set_title(Title, pad=16, fontdict={'fontsize': 24})

    ax.legend()

    plt.tight_layout()
    plt.savefig('Mul_scatter.pdf')
    plt.show()

Mul_scater(style='ggplot', colors=('#d87c7c', '#919e8b', '#d7ab82', '#6e7074', '#61a0a8'), Title='Title', Xlabel='Xlabel', Ylabel='Ylabel')
