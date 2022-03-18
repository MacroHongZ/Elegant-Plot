# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:11:20 2022

@author: Wang
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

data = pd.read_csv('data.csv')
x = data.iloc[:, 0].to_numpy()


def plotline(style='ggplot', color='#72aa9d', Title='Title', Xlabel='Xlabel', Ylabel='Ylabel'):

    matplotlib.rcParams['font.family'] = 'serif'
    plt.style.use(style)

    fig = plt.figure(dpi=300)
    ax = fig.subplots()
    line1 = ax.plot(x)

    plt.setp(line1, c=color)

    ax.set_xlabel(Xlabel)
    ax.set_ylabel(Ylabel)
    ax.set_title(Title, pad=16, fontdict={'fontsize': 24})

    # ax.set_ylim(10, 32)
    # ax.set_yticks(np.arange(10, 32, 4))

    ax.tick_params(axis='y', which='both', direction='in', right=False)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)

    plt.savefig('line.pdf')
    plt.show()


plotline()
