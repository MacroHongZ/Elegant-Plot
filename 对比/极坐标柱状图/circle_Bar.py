import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


data = pd.read_csv('data.csv')

value = data['series_value'].to_numpy()
maxvalue = value.max()
bottom = 0.1*maxvalue
value = value - bottom

xticks = data['X_tick'].to_list()
width = 2*np.pi / value.size
angles = np.arange(value.size) * width

def circle_bar(style='ggplot', Title='Title', color='#72aa9d'):
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
	ax = fig.add_subplot(projection='polar')
	bar = ax.bar(angles, value, width=0.8*width, bottom=bottom, color=color)		
	
	ax.set_title(Title, pad=35, fontdict={'fontsize':24})
	ax.set_xticks(angles, xticks)
	ax.tick_params(axis='x', which='both', pad=0)
	
	plt.savefig('circle_Bar.pdf')
	plt.show()
	
circle_bar()