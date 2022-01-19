import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


data = pd.read_csv('data.csv')

value = data['series_value'].to_numpy()
xindex = np.arange(data.shape[0])
xticks = data['X_tick'].to_list()


def plotbar(style='ggplot', color='#72aa9d', Title='Title', Xlabel='Xlabel', Ylabel='Ylabel'):
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
	bar = ax.bar(xindex, value, width=0.6, color=color)		#设置柱子颜色

	ax.set_xlabel(Xlabel)
	ax.set_ylabel(Ylabel)
	ax.set_title(Title, pad=16, fontdict={'fontsize':24})
	
	ax.set_xticks(xindex, xticks)
	ax.tick_params(axis='y', which='both', direction='in', right=False)
	ax.tick_params(axis='x', which='both', bottom=False, top=False)
	
	ax.bar_label(bar, padding=3)
	
	plt.savefig('bar.pdf')
	plt.show()

def plot_texture_bar(hatch='//', Title='Title', Xlabel='Xlabel', Ylabel='Ylabel'):
	plt.style.use('seaborn-ticks')	# 设置风格
	matplotlib.rcParams['font.family'] = 'serif'
	
	fig = plt.figure(dpi=300)
	ax = fig.subplots()
	
	bar = ax.bar(xindex, value, width=0.6, color='w', edgecolor='black', hatch="//")
	'''
	/   - diagonal hatching
	\   - back diagonal
	|   - vertical
	-   - horizontal
	+   - crossed
	x   - crossed diagonal
	o   - small circle
	O   - large circle
	.   - dots
	*   - stars
	'''
	
	ax.set_xlabel(Xlabel)
	ax.set_ylabel(Ylabel)
	ax.set_title(Title, pad=16, fontdict={'fontsize':24})
	
	ax.set_xticks(xindex, xticks)
	# ax.minorticks_on()
	ax.tick_params(axis='y', which='both', direction='in', right=False)
	ax.tick_params(axis='x', which='both', bottom=False, top=False)
	bwith = 2
	ax.spines['bottom'].set_linewidth(bwith)
	ax.spines['left'].set_linewidth(bwith)
	ax.spines['top'].set_linewidth(bwith)
	ax.spines['right'].set_linewidth(bwith)
	
	ax.bar_label(bar, padding=3)
	
	plt.savefig('texture_bar.pdf')
	plt.show()
	
plotbar()
# plot_texture_bar()
