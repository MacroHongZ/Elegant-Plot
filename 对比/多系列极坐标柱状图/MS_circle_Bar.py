import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


data = pd.read_csv('data.csv')
labels = list(data.columns)
labels = [labels[i] for i in range(0, len(labels), 2)]
series_num = int(data.shape[1] / 2)

all_series = []
for i in range(series_num):
    series = data.iloc[:, 0+2*i].to_numpy()
    series = series[~np.isnan(series)]
    all_series.append(series)


all_value = np.concatenate(all_series)

maxvalue = all_value.max()
bottom = 0.1*maxvalue
all_series = [series - bottom for series in all_series]

all_ticks = []
for i in range(series_num):
    ticks = data.iloc[:, 1+2*i]
    ticks = ticks[ticks.notna()].to_list()
    all_ticks.extend(ticks)

series_count = np.array([i.size for i in all_series])
series_cumsum = np.cumsum(series_count).tolist()
series_cumsum = [0] + series_cumsum
width = 2*np.pi / all_value.size
angles = np.arange(all_value.size) * width

def MS_circle_Bar(style='ggplot', Title='Title', colors=['#d87c7c', '#919e8b', '#d7ab82', '#6e7074', '#61a0a8']):
    plt.style.use(style)  # 设置风格
    matplotlib.rcParams['font.family'] = 'serif'
    '''
	Solarize_Light2
	_classic_test_patch
	_mpl-gallery
	_mpl-gallery-nogrid
	bmh
	classic
	dark_background
	fast
	fivethirtyeight
	ggplot
	grayscale
	seaborn
	seaborn-bright
	seaborn-colorblind
	seaborn-dark
	seaborn-dark-palette
	seaborn-darkgrid
	seaborn-deep
	seaborn-muted
	seaborn-notebook
	seaborn-paper
	seaborn-pastel
	seaborn-poster
	seaborn-talk
	seaborn-ticks
	seaborn-white
	seaborn-whitegrid
	tableau-colorblind10
	'''
    colors = colors*10
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(projection='polar')

    for i in range(series_num):
        bar = ax.bar(angles[series_cumsum[i]:series_cumsum[i+1]],
                     all_series[i],
                     width=0.8*width,
                     bottom=bottom,
                     color=colors[i],
                     label=labels[i])

    ax.set_title(Title, pad=35, fontdict={'fontsize': 24})
    ax.set_xticks(angles, all_ticks)
    ax.tick_params(axis='x', which='both', pad=0)

    ax.legend(loc='upper left', bbox_to_anchor=(0.1,-0.1), ncol=series_num)

    # plt.savefig('MS_circle_Bar.pdf')
    plt.show()


MS_circle_Bar()
