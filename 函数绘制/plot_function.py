import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math


def function(x):
    return math.cos(x)


def plot_function(function, xrange=(-10, 10)):
    x = np.arange(xrange[0], xrange[1], 0.1)
    y = list(map(function, x))

    plt.style.use('seaborn-ticks')
    matplotlib.rcParams['font.family'] = 'serif'
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot()

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_position(("data", 0))
    ax.spines['bottom'].set_position(("data", 0))

    xticks_lable = list(map(str, np.linspace(xrange[0], xrange[1], 11)))
    ax.set_xticks(np.linspace(xrange[0], xrange[1], 11), xticks_lable)

    ax.plot(x, y, color='#d87c7c')
    plt.show()


plot_function(function)
