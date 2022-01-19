import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


data = pd.read_csv('data.csv')

value = data['series_value'].to_numpy()
xindex = 0.5 + np.arange(data.shape[0])
xticks = data['X_tick'].to_list()

def plot_stem(style='ggplot', color='#72aa9d', Title='Title', Xlabel='Xlabel', Ylabel='Ylabel'):
	plt.style.use(style)	# 设置风格
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
	
	fig = plt.figure(dpi=300)
	ax = fig.subplots()
	mystem = ax.stem(xindex, value, linefmt=color, markerfmt=color)		#设置柱子颜色
	
	mystem[1].set_linewidths(1.5)
	
	mystem[0].set_marker('o')
	mystem[0].set_markeredgewidth(2)
	mystem[0].set_markeredgecolor(color)
	mystem[0].set_linestyle('none')
	ax.set_xlabel(Xlabel)
	ax.set_ylabel(Ylabel)
	ax.set_title(Title, pad=16, fontdict={'fontsize':24})
	
	ax.set_xticks(xindex, xticks)
	ax.tick_params(axis='y', which='both', direction='in', right=False)
	ax.tick_params(axis='x', which='both', bottom=False, top=False)
	
	plt.savefig('Stem.pdf')
	plt.show()

plot_stem()