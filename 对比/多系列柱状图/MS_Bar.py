import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


data = pd.read_csv('data.csv')
labels = data.columns

mul_series = data.iloc[:,:-1].to_numpy().T
series_num = mul_series.shape[0]
width = 0.4
space = width * (series_num + 1.5)
bar_width = (width * mul_series.shape[1]) / 2 - 0.5 * width
xindex = np.array([0 + i*space for i in range(mul_series.shape[1])]) - bar_width
xticks = data['X_tick'].to_list()

def Ms_Bar(style='ggplot', Title='Title', Xlabel='Xlabel', Ylabel='Ylabel', color=['#d87c7c', '#919e8b', '#d7ab82', '#6e7074', '#61a0a8']):
	matplotlib.rcParams['font.family'] = 'serif'
	plt.style.use(style)
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
	colors = color * 10
	
	for i in range(series_num):
		bar01 = ax.bar(xindex + i*width, mul_series[i], width-0.1, color=colors[i], label=labels[i])		#设置柱子颜色		
		
	ax.set_xlabel(Xlabel)
	ax.set_ylabel(Ylabel)
	ax.set_title(Title, pad=16, fontdict={'fontsize':24})
	
	ax.set_xticks(xindex + (mul_series.shape[0]-1)/2*width, xticks)
	ax.tick_params(axis='y', which='both', direction='in', right=False)
	ax.tick_params(axis='x', which='both', bottom=False, top=False)
	ax.set_ylim(0, int(1.2 * mul_series.max()))

	
	ax.legend()
	
	plt.savefig('Ms_Bra.pdf')
	plt.show()

Ms_Bar()
