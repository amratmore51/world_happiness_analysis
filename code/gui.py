import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as font
import pandas as pd
from pandastable import Table
import numpy as np
import preprocessing as ppr
import find_correlations as corr
import history as hist
import visualise as vs
import neighbours as neb
import regression as regr
import naivebayes as nb
import comparison as cmp

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

def back(root, root1):
	root1.withdraw()
	root.deiconify()
	
def loadWindow(root):
	root.withdraw()
	root1 = Tk()
	root1.title("Load Dataset")	# Set the Window Title
	root1.geometry("1200x800")
	root1.configure(bg='white')
	w=Label(root1, text="Load the Dataset", fg='green', bg='white', font='Arial 20 bold')
	w.pack()

	frame1 = LabelFrame(root1, text='Options', width=1200, height=80, borderwidth = 5, fg = 'blue', bg='white')
	frame1.pack(side=TOP, fill=X)

	button2 = Button(frame1, text='<-- Back to Main Menu', fg='white', bg='green', command=lambda:back(root, root1))
	button2.pack(side=LEFT, expand=1)
	
	button1 = Button(frame1, text='Load Dataset',fg='white', bg='green', command=lambda:LoadDataset(root1, button1))
	button1.pack(side=LEFT, expand=1)

	#root1.eval('tk::PlaceWindow %s center' % root1.winfo_pathname(root1.winfo_id()))	# used to disply the window at the center of screen	
	root1.mainloop()

def quitWindow():
	if messagebox.askyesnocancel('Verify', 'Really quit?'):
		messagebox.showwarning('Yes', 'Your Program will Quit')
		exit(0)
	else:
		messagebox.showinfo('No', 'Quit has been cancelled')
#	exit(0)

def firstWindow(root, leftFrame):
	helv36 = font.Font(family='Arial', size=12)
	
	loadButton = Button(leftFrame, text='Load and Display the Dataset', font=helv36, fg='white', bg='green', command=lambda: loadWindow(root))
	loadButton.pack(fill=X, padx=50, pady=10)

	preButton = Button(leftFrame, text='Preprocessing', font=helv36, fg='white', bg='green', command=lambda:ppr.preprocessingWindow(root, data))
	preButton.pack(fill=X, padx=50, pady=10)

	corrButton = Button(leftFrame, text='Find Correlations', font=helv36, fg='white', bg='green', command=lambda:corr.correlationWindow(root, data))
	corrButton.pack(fill=X, padx=50, pady=10)
	
	histButton = Button(leftFrame, text='India from 2006 to 2021', font=helv36, fg='white', bg='green', command=lambda:hist.historyWindow(root, data))
	histButton.pack(fill=X, padx=50, pady=10)

	vizButton = Button(leftFrame, text='Visualization', font=helv36, fg='white', bg='green', command=lambda:vs.visualiseMenu(root, data))
	vizButton.pack(fill=X, padx=50, pady=10)

	compareButton = Button(leftFrame, text='Comparison of India with Neighbours', font=helv36, fg='white', bg='green', command=lambda:neb.comparisonMenu(root, data))
	compareButton.pack(fill=X, padx=50, pady=10)

	predButton = Button(leftFrame, text='Prediction using Multiple Linear Regression', font=helv36, fg='white', bg='green', command=lambda:regr.regressionOptions(root, filepath))
	predButton.pack(fill=X, padx=50, pady=10)

	NBpredButton = Button(leftFrame, text='Prediction using Naive Bayes', font=helv36, fg='white', bg='green', command=lambda:nb.naiveBayesOptions(root, filepath))
	NBpredButton.pack(fill=X, padx=50, pady=10)

	compareButton = Button(leftFrame, text='Comparison of Regression & Naive Bayes', font=helv36, fg='white', bg='green', command=cmp.compare)
	compareButton.pack(fill=X, padx=50, pady=10)

	quitButton = Button(leftFrame, text='Quit', font=helv36, fg='white', bg='green', command=quitWindow)
	quitButton.pack(padx=100, side=LEFT)
	
	button = Button(leftFrame, text='Help', font=helv36, fg='white', bg='green') # lambda is used to pass arguments to the function
	button.pack(padx=100, side=LEFT)

