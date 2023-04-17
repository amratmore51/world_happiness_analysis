import matplotlib.pyplot as plt
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog		
from tkinter import messagebox
import pandas as pd
#import preprocessing
from pandastable import Table
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # for displaying the graphs in tkinter window
#import dataset_metadata as meta
#from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#from sklearn.preprocessing import scale
from numpy import random, float, array
import numpy as np
import seaborn as sns
#from sklearn.preprocessing import StandardScaler


def back(current, previous):
	current.withdraw()
	previous.deiconify()

def clearWindow(win):
	for widget in win.winfo_children():
		widget.destroy()

def findCorrelationsBetweenFactors(df, frame2_1):
	cols = df[['Ladder score', 'Logged GDP per capita','Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']]
	new_df = cols.corr()
	t = Table(frame2_1, dataframe=new_df)
	t.show()
	plt.figure(figsize=(20, 8))
	sns.heatmap(cols.corr(), annot = True, cmap='RdYlGn_r', mask=np.triu(np.ones_like(cols.corr())))
	plt.title('Correlations between factors', fontsize=20, fontweight='bold', pad=20)
	plt.show()

def findCorrelationsLadderScoreGenorosity(data, frame2_1):
	cols = data[['Ladder score', 'Generosity']]
	plt.figure(figsize=(20, 8))
	sns.heatmap(cols.corr(), annot = True, cmap='RdYlGn_r', mask=np.triu(np.ones_like(cols.corr())));
	plt.title('Correlations between Ladder Score and Generocity', fontsize=20, fontweight='bold', pad=20);
	plt.show()

	plt.figure(figsize=(12, 6))
	sns.regplot(x='Ladder score', y='Generosity', data=data, ci=None)
	plt.title('Correlation between ladder score and generosity', fontsize=20, fontweight='bold', pad=20)
	plt.show()

def findCorrelationsLadderScoreCorruption(data, frame2_1):
	cols = data[['Ladder score', 'Perceptions of corruption']]
	plt.figure(figsize=(20, 8))
	sns.heatmap(cols.corr(), annot = True, cmap='RdYlGn_r', mask=np.triu(np.ones_like(cols.corr())));
	plt.title('Correlations between Ladder Score and Perceptions of Corruption', fontsize=20, fontweight='bold', pad=20);
	plt.show()
	
	plt.figure(figsize=(12, 6))
	sns.regplot(x='Ladder score', y='Perceptions of corruption', data=data, ci=None)
	plt.title('Correlation between ladder score and perceptions of corruption', fontsize=20, fontweight='bold', pad=20)
	plt.show()

def correlationWindow(root1, data):
	#root1.withdraw()
	anWin = Tk()
	anWin.title("CORRELATION")
	anWin.configure(bg='white')

	w=Label(anWin, text='Find Correlation', fg='green', bg='white', font='Arial 22 bold ')
	w.pack()

	frame1_1 = LabelFrame(anWin, width=1200, height=40, bg='white')
	frame1_1.pack(fill=X, expand=1)

	frame1_2 = LabelFrame(anWin, width=1200, height=40, bg='white')
	frame1_2.pack(fill=X, expand=1)

	frame2 = LabelFrame(anWin, text='Data in Tabular Format', width=1200, height=1000, borderwidth = 5, fg = 'blue', bg='white')
	frame2.pack(fill=X, expand=1)

	frame2_1 = LabelFrame(frame2, text="Correlations of Variables", width=500, height=500, borderwidth = 5, fg = 'blue', bg='white')
	frame2_1.pack(fill=BOTH, side=LEFT, expand=1)
	frame2_1.configure(height=frame2_1["height"],width=frame2_1["width"])
	frame2_1.pack_propagate(0)

	# Frame1_1 contents

	button1 = Button(frame1_1, text='Find Correlation between Factors',fg='white', bg='green', command=lambda:findCorrelationsBetweenFactors(data, frame2_1))
	button1.pack(side=LEFT, fill=X, expand=1)

	button2 = Button(frame1_1, text='Find Correlation between Ladder Score & Genorosity',fg='white', bg='green', command=lambda:findCorrelationsLadderScoreGenorosity(data, frame2_1))
	button2.pack(side=LEFT, fill=X, expand=1)

	button3 = Button(frame1_1, text='Find Correlation between Ladder Score & Perceptions of Corruption',fg='white', bg='green', command=lambda:findCorrelationsLadderScoreCorruption(data, frame2_1))
	button3.pack(side=LEFT, fill=X, expand=1)

	button2 = Button(frame1_1, text='<-- Back to Main Menu', fg='white', bg='green', command=lambda:back(anWin, root1))
	button2.pack(side=LEFT, fill=X, expand=1)

        #anWin.eval('tk::PlaceWindow %s center' % anWin.winfo_pathname(anWin.winfo_id()))	 
	anWin.mainloop()
