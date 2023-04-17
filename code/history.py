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
import matplotlib.pyplot as plt
from numpy import random, float, array
import numpy as np


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
	
def LoadDataset(root1, button):			# Opens a file browsing File Dialog
	ftypes = [('CSV Files', '*.csv'),('All files', '*')]
	global filepath
	filepath = filedialog.askopenfilename(initialdir = "C:\\Happiness\\dataset\\",title = "Select the Dataset File",filetypes = (("CSV files","*.csv"),("all files","*.*")))
	global data
	data = pd.read_csv(filepath)
	button.config(state="disabled")
	displayDataset(root1, data, "Original Dataset")
	messagebox.showinfo('Data Loaded', 'Dataset is loaded successfully.')
	root1.lift()
	return filepath
        

def generateHistoryReport(filepath, happiness_report, frame2_2):
	happiness_report_older = pd.read_csv(filepath)
	india_1 = happiness_report_older[happiness_report_older['Country name'] == 'India'].reset_index(drop=True) 
	india_1 = india_1.drop(['Positive affect','Negative affect'], axis = 1)
	india_1 = india_1.fillna(0)
	happiness_report['year'] = 2021
	india_2 = happiness_report[happiness_report['Country name'] == 'India']
	india_2 = india_2.rename(columns = {'Ladder score':'Life Ladder',
		        'Logged GDP per capita':'Log GDP per capita',
		        'Healthy life expectancy':'Healthy life expectancy at birth'})
	india_2 = india_2.drop(['Dystopia + residual', 'Regional indicator'], axis = 1)
	india = pd.concat([india_1, india_2])
	india.reset_index(drop=True, inplace=True)
	india.rename(columns = {'year':'Year'}, inplace=True)
	displayDataset(frame2_2, india, 'India from 2006 to 2021')



def historyWindow(root1, data):
	root1.withdraw()
	histWin = Tk()
	histWin.title("History")
	histWin.configure(bg='white')

	w=Label(histWin, text='History of India from 2006 to 2021', fg='green', bg='white', font='Arial 22 bold')
	w.pack()
	
	frame1_1 = LabelFrame(histWin, width=1200, height=40, bg='white')
	frame1_1.pack(fill=X, expand=1)

#	frame1_2 = LabelFrame(histWin, width=1200, height=40, bg='white')
#	frame1_2.pack(fill=X, expand=1)

	frame2 = LabelFrame(histWin, width=1200, height=1000, borderwidth = 5, fg = 'blue', bg='white')
	frame2.pack(fill=X, expand=1)

	frame2_1 = LabelFrame(frame2, text="Data in Tabular Format", width=500, height=500, borderwidth = 5, fg = 'blue', bg='white')
	frame2_1.pack(fill=BOTH, side=LEFT, expand=1)
	frame2_1.configure(height=frame2_1["height"],width=frame2_1["width"])
	frame2_1.pack_propagate(0)

	frame2_2 = LabelFrame(frame2, width=700, height=500, borderwidth = 5, fg = 'blue', bg='white')
	frame2_2.pack(fill=BOTH, side=LEFT, expand=1)
	frame2_2.configure(height=frame2_2["height"],width=frame2_2["width"])
	frame2_2.pack_propagate(0)

	# Frame1_1 contents
	button1 = Button(frame1_1, text='Load Dataset',fg='white', bg='green', command=lambda:LoadDataset(frame2_1, button1))
	button1.pack(side=LEFT, expand=1)

	button3 = Button(frame1_1, text='Generate History Report',fg='white', bg='green', command=lambda:generateHistoryReport(filepath, data, frame2_2))
	button3.pack(side=LEFT, expand=1)

	button2 = Button(frame1_1, text='<-- Back to Main Menu', fg='white', bg='green', command=lambda:back(histWin, root1))
	button2.pack(side=LEFT, expand=1)

	histWin.mainloop()
