import matplotlib.pyplot as plt
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog		
from tkinter import messagebox
import pandas as pd
from pandastable import Table
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # for displaying the graphs in tkinter window
#import dataset_metadata as meta
#from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#from sklearn.preprocessing import scale
from numpy import random, float, array
import numpy as np
#import seaborn as sns
#from sklearn.preprocessing import StandardScaler


def back(current, previous):
	current.withdraw()
	previous.deiconify()

def clearWindow(win):
	for widget in win.winfo_children():
		widget.destroy()

def displayDataset(root1, data, title):
	f = LabelFrame(root1, text=title, borderwidth = 5, fg = 'blue')	# Create a frame
	f.pack(fill=BOTH,expand=1)
	t = Table(f, dataframe=data)
	t.show()
	return
def dropColumns(anWin, data, title):
	data_report = data.drop(['Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
	       'Explained by: Log GDP per capita', 'Explained by: Social support',
	       'Explained by: Healthy life expectancy',
	       'Explained by: Freedom to make life choices',
	       'Explained by: Generosity', 'Explained by: Perceptions of corruption', 'Ladder score in Dystopia'], axis = 1)
	displayDataset(anWin, data_report, title)
	messagebox.showinfo('Drop Columns', 'Unnecessary Columns are Dropped')


def handleNA(data):
	data.dropna(inplace=True)
	messagebox.showinfo('handle NA', 'NA values are dropped Successfully')

def dropDownMenu(data, frame1_2, anWin):
	button1 = tk.Button(frame1_2, text="Handle NAs", fg='white', bg='green', command=lambda:handleNA(data))
	button1.pack(side=LEFT, fill=X, expand=1)

	button2 = tk.Button(frame1_2, text="Drop Columns", fg='white', bg='green', command=lambda:dropColumns(anWin, data, 'Dataframe After Dropping Columns'))
	button2.pack(side=LEFT, fill=X, expand=1)

def preprocessingWindow(root1, data):
	root1.withdraw()
	anWin = Tk()
	anWin.title("Analysis")
	anWin.configure(bg='white')

	w=Label(anWin, text='Drop Columns from Dataset', fg='blue', bg='white', font='Arial 18 bold ')
	w.pack()

	#frame1_1 = LabelFrame(anWin, width=1200, height=40, bg='white')
	#frame1_1.pack(fill=X, expand=1)

	frame1_2 = LabelFrame(anWin, width=1200, height=40, bg='white')
	frame1_2.pack(fill=X, expand=1)

	# Frame1_1 contents

	#button1 = Button(frame1_1, text='Start Column Drop',fg='white', bg='green', command=lambda:dropDownMenu(data, frame1_2, anWin))
	#button1.pack(side=LEFT, fill=X, expand=1)

	# Frame1_2 contents

	button1 = Button(frame1_2, text="Handle NAs", fg='white', bg='green', command=lambda:handleNA(data))
	button1.pack(side=LEFT, padx=10, pady=10)

	button2 = Button(frame1_2, text="Drop Columns", fg='white', bg='green', command=lambda:dropColumns(anWin, data, 'Dataframe After Dropping Columns'))
	button2.pack(side=LEFT, padx=10, pady=10)

	button3 = Button(frame1_2, text='<-- Back to Main Menu', fg='white', bg='green', command=lambda:back(anWin, root1))
	button3.pack(side=LEFT, padx=10, pady=10)

	anWin.eval('tk::PlaceWindow %s center' % anWin.winfo_pathname(anWin.winfo_id()))	# used to disply the window at the center of screen	
	anWin.mainloop()
