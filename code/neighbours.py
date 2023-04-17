from tkinter import *
import tkinter.font as font
import pandas as pd
from pandastable import Table
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def quitWindow():
	if messagebox.askyesnocancel('Verify', 'Really quit?'):
		messagebox.showwarning('Yes', 'Your Program will Quit')
		exit(0)
	else:
		messagebox.showinfo('No', 'Quit has been cancelled')
		
def happiness(happiness_report):
	top = happiness_report[happiness_report['Country name'] == 'Finland']
	south_asia = happiness_report[happiness_report['Regional indicator'] == 'South Asia']

	top_bottom_neighbors = pd.concat([top, south_asia], axis=0)
	top_bottom_neighbors['Rank'] = top_bottom_neighbors.index + 1
	top_bottom_neighbors.reset_index(drop=True, inplace=True)
	top_bottom_neighbors.drop(['Regional indicator', 'Dystopia + residual', 'year'], axis=1, inplace=True)
	
	df_glob = happiness_report.sort_values('Ladder score', ascending=False)[['Country name', 'Ladder score', 'Regional indicator']].reset_index(drop=True)
	
	top = df_glob[df_glob['Ladder score'] == df_glob['Ladder score'].max()]
	neighbors = df_glob[df_glob['Regional indicator'] == 'South Asia']
	
	top_bottom_neighbors = pd.concat([top, neighbors], axis=0)
	top_bottom_neighbors['Rank'] = list(top_bottom_neighbors.index + 1)
	top_bottom_neighbors.reset_index(drop=True, inplace=True)
	top_bottom_neighbors.drop('Regional indicator', axis=1, inplace=True)

	mean_score = happiness_report['Ladder score'].mean()
	rank = list(top_bottom_neighbors['Rank'])

	fig, ax = plt.subplots(figsize=(12, 6))
	bar = sns.barplot(x='Country name', y='Ladder score', data=top_bottom_neighbors, palette='summer_r')
	sns.set_style('whitegrid')
	sns.despine(left=True)
	for i in range(1, len(top_bottom_neighbors)):
		bar.text(x=i, y=(top_bottom_neighbors['Ladder score'][i])/2, s=str(rank[i])+'th', fontdict=dict(color='white', fontsize=12, fontweight='bold', horizontalalignment='center'))

	bar.text(x=0, y=(top_bottom_neighbors['Ladder score'][0])/2, s=str(rank[0])+'st', fontdict=dict(color='white', fontsize=12, fontweight='bold', horizontalalignment='center'))
	bar.axhline(mean_score, color='grey', linestyle='--')
	bar.text(x=len(top_bottom_neighbors)-0.4, y = mean_score, s = 'Global Average: {:.2f}'.format(mean_score),
		fontdict = dict(color='white', backgroundcolor='grey', fontsize=10, fontweight='bold'))
	
	plt.title('How Happy is India Among its Neighbors?', fontsize=18, fontweight='bold', pad=20)
	plt.xlabel('Countries')
	plt.show()

def logGDP(happiness_report):
	df_glob = happiness_report.sort_values('Logged GDP per capita', ascending=False)[['Country name', 'Logged GDP per capita', 'Regional indicator']].reset_index(drop=True)
	top = df_glob[df_glob['Logged GDP per capita'] == df_glob['Logged GDP per capita'].max()]
	neighbors = df_glob[df_glob['Regional indicator'] == 'South Asia']
	top_bottom_neighbors = pd.concat([top, neighbors], axis=0)
	top_bottom_neighbors['Rank'] = list(top_bottom_neighbors.index + 1)
	top_bottom_neighbors.reset_index(drop=True, inplace=True)
	top_bottom_neighbors.drop('Regional indicator', axis=1, inplace=True)
	mean_score = happiness_report['Logged GDP per capita'].mean()
	rank = list(top_bottom_neighbors['Rank'])
	plt.figure(figsize=(12, 6))
	bar = sns.barplot(x='Country name', y='Logged GDP per capita', data=top_bottom_neighbors, palette='summer_r');
	sns.set_style('whitegrid')
	sns.despine(left=True)
	for i in range(1, len(top_bottom_neighbors)):
		bar.text(x=i, y=(top_bottom_neighbors['Logged GDP per capita'][i])/2, s=str(rank[i])+'th', fontdict=dict(color='white', fontsize=12, fontweight='bold', horizontalalignment='center'))
	bar.text(x=0, y=(top_bottom_neighbors['Logged GDP per capita'][0])/2, s=str(rank[0])+'st', fontdict=dict(color='white', fontsize=12, fontweight='bold', horizontalalignment='center'))
	bar.axhline(mean_score, color='grey', linestyle='--')
	bar.text(x=len(top_bottom_neighbors)-0.4, y = mean_score, s = 'Global Average: {:.2f}'.format(mean_score), fontdict = dict(color='white', backgroundcolor='grey', fontsize=10, fontweight='bold'))
	plt.title("Where does India's Log GDP Ranks?", fontsize=18, fontweight='bold', pad=20)
	plt.xlabel('')
	plt.show()

def healthyLifeExpectancy(happiness_report):
	df_glob = happiness_report.sort_values('Healthy life expectancy', ascending=False)[['Country name', 'Healthy life expectancy', 'Regional indicator']].reset_index(drop=True)
	top = df_glob[df_glob['Healthy life expectancy'] == df_glob['Healthy life expectancy'].max()]
	neighbors = df_glob[df_glob['Regional indicator'] == 'South Asia']
	top_bottom_neighbors = pd.concat([top, neighbors], axis=0)
	top_bottom_neighbors['Rank'] = list(top_bottom_neighbors.index + 1)
	top_bottom_neighbors.reset_index(drop=True, inplace=True)
	top_bottom_neighbors.drop('Regional indicator', axis=1, inplace=True)
	mean_score = happiness_report['Healthy life expectancy'].mean()
	rank = list(top_bottom_neighbors['Rank'])
	plt.figure(figsize=(12, 6))
	bar = sns.barplot(x='Country name', y='Healthy life expectancy', data=top_bottom_neighbors, palette='summer_r');
	sns.set_style('whitegrid')
	sns.despine(left=True)
	for i in range(1, len(top_bottom_neighbors)):
		bar.text(x=i, y=(top_bottom_neighbors['Healthy life expectancy'][i])/2, s=str(rank[i])+'th', fontdict=dict(color='white', fontsize=12, fontweight='bold', horizontalalignment='center'))
	bar.text(x=0, y=(top_bottom_neighbors['Healthy life expectancy'][0])/2, s=str(rank[0])+'st', fontdict=dict(color='white', fontsize=12, fontweight='bold', horizontalalignment='center'))
	bar.axhline(mean_score, color='grey', linestyle='--')
	bar.text(x=len(top_bottom_neighbors)-0.4, y = mean_score, s = 'Global Average: {:.2f}'.format(mean_score), fontdict = dict(color='white', backgroundcolor='grey', fontsize=10, fontweight='bold'))
	plt.title("Where does India's Healthy life expectancy Ranks?", fontsize=18, fontweight='bold', pad=20)
	plt.xlabel('')
	plt.show()

def perceptionOfCorruption(happiness_report):
	df_glob = happiness_report.sort_values('Perceptions of corruption', ascending=False)[['Country name', 'Perceptions of corruption', 'Regional indicator']].reset_index(drop=True)
	top = df_glob[df_glob['Perceptions of corruption'] == df_glob['Perceptions of corruption'].max()]
	neighbors = df_glob[df_glob['Regional indicator'] == 'South Asia']
	top_bottom_neighbors = pd.concat([top, neighbors], axis=0)
	top_bottom_neighbors['Rank'] = list(top_bottom_neighbors.index + 1)
	top_bottom_neighbors.reset_index(drop=True, inplace=True)
	top_bottom_neighbors.drop('Regional indicator', axis=1, inplace=True)
	mean_score = happiness_report['Perceptions of corruption'].mean()
	rank = list(top_bottom_neighbors['Rank'])
	plt.figure(figsize=(12, 6))
	bar = sns.barplot(x='Country name', y='Perceptions of corruption', data=top_bottom_neighbors, palette='summer_r');
	sns.set_style('whitegrid')
	sns.despine(left=True)
	for i in range(1, len(top_bottom_neighbors)):
		bar.text(x=i, y=(top_bottom_neighbors['Perceptions of corruption'][i])/2, s=str(rank[i])+'th', fontdict=dict(color='white', fontsize=12, fontweight='bold', horizontalalignment='center'))
	bar.text(x=0, y=(top_bottom_neighbors['Perceptions of corruption'][0])/2, s=str(rank[0])+'st', fontdict=dict(color='white', fontsize=12, fontweight='bold', horizontalalignment='center'))
	bar.axhline(mean_score, color='grey', linestyle='--')
	bar.text(x=len(top_bottom_neighbors)-0.4, y = mean_score, s = 'Global Average: {:.2f}'.format(mean_score), fontdict = dict(color='white', backgroundcolor='grey', fontsize=10, fontweight='bold'))
	plt.title("Where does India's Perceptions of corruption Ranks?", fontsize=18, fontweight='bold', pad=20)
	plt.xlabel('')
	plt.show()


def comparisonMenu(root, data):
	helv36 = font.Font(family='Arial', size=12)
	win = Tk()
	win.title('Comparison of India with Neighbors')

	happiness_report = data.drop(['Standard error of ladder score', 'upperwhisker', 'lowerwhisker', 'Explained by: Log GDP per capita', 'Explained by: Social support', 'Explained by: Healthy life expectancy', 'Explained by: Freedom to make life choices', 'Explained by: Generosity', 'Explained by: Perceptions of corruption', 'Ladder score in Dystopia'], axis = 1)

	b1 = Button(win, text='How Happy is India Among Its Neighbors?', font=helv36, fg='white', bg='green', command=lambda:happiness(happiness_report))
	b1.pack(fill=X, padx=50, pady=10)

	b2 = Button(win, text='Where does India’s Log GDP Rank?', font=helv36, fg='white', bg='green', command=lambda:logGDP(happiness_report))
	b2.pack(fill=X, padx=50, pady=10)

	b3 = Button(win, text='Where Does India’s Healthy Life Expectancy Ranks?', font=helv36, fg='white', bg='green', command=lambda:healthyLifeExpectancy(happiness_report))
	b3.pack(fill=X, padx=50, pady=10)
	
	b4 = Button(win, text='Where Does India’s Perceptions of corruption Ranks?', font=helv36, fg='white', bg='green', command=lambda:perceptionOfCorruption(happiness_report))
	b4.pack(fill=X, padx=50, pady=10)

	win.eval('tk::PlaceWindow %s center' % win.winfo_pathname(win.winfo_id()))	# used to disply the window at the center of screen	
	win.mainloop()


