from tkinter import *
import tkinter.font as font
from turtle import color
import pandas as pd
from pandastable import Table
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import visualisation_result as vis_res

def quitWindow():
	if messagebox.askyesnocancel('Verify', 'Really quit?'):
		messagebox.showwarning('Yes', 'Your Program will Quit')
		exit(0)
	else:
		messagebox.showinfo('No', 'Quit has been cancelled')
		
def prepareData(happiness_report):
	happiness_report_older = pd.read_csv('C:\\Happiness\\dataset\\world-happiness-report.csv')
	india_1 = happiness_report_older[happiness_report_older['Country name'] == 'India'].reset_index(drop=True) 
	india_1 = india_1.drop(['Positive affect','Negative affect'], axis = 1)
	india_1 = india_1.fillna(0)
	happiness_report['year'] = 2021
	india_2 = happiness_report[happiness_report['Country name'] == 'India']
	india_2 = india_2.rename(columns = {'Ladder score':'Life Ladder',
		        'Logged GDP per capita':'Log GDP per capita',
		        'Healthy life expectancy':'Healthy life expectancy at birth'})
	india_2 = india_2.drop(['Dystopia + residual', 'Regional indicator'], axis = 1)
	global india
	india = pd.concat([india_1, india_2])
	india.reset_index(drop=True, inplace=True)
	india.rename(columns = {'year':'Year'}, inplace=True)
	india.to_csv('C:\\Happiness\\india.csv')
	return india

def ladderScore(india):
	plt.figure(figsize=(18, 6))
	sns.lineplot(x='Year', y='Life Ladder', data=india, marker='o', markersize=10);
	sns.set_style('whitegrid')
	sns.despine(left=True)
	plt.title("India's ladder score over the years", fontsize=18, fontweight='bold', pad=20)
	plt.xlabel('Year')
	str1, str2, str3, str4 = vis_res.visualisation_result_ladder_score(india)
	msg = '----------------- Auto Generated Conclusion -----------------\n' + str1 + '\n' + str2 + '\n--------------------------------------------------------------------------' + '\n' + str3 + '\n' + str4 + '\n--------------------------------------------------------------------------'
	plt.text(2012, 4.7, msg, fontsize=12, color='blue')
	plt.show()

def logGDPPerCapita(india):
	plt.figure(figsize=(18, 6))
	sns.lineplot(x='Year', y='Log GDP per capita', data=india, marker='o', markersize=10);
	sns.set_style('whitegrid')
	sns.despine(left=True)
	plt.title("India's Log GDP per capita over the years", fontsize=18, fontweight='bold', pad=20)
	plt.xlabel('Year')
	str1, str2, str3, str4 = vis_res.visualisation_result_log_GDP_per_capita(india)
	msg = '----------------- Auto Generated Conclusion -----------------\n' + str1 + '\n' + str2 + '\n--------------------------------------------------------------------------' + '\n' + str3 + '\n' + str4 + '\n--------------------------------------------------------------------------'
	plt.text(2006, 8.5, msg, fontsize=12, color='blue')
	plt.show()

def socialSupport(india):
	plt.figure(figsize=(18, 6))
	sns.lineplot(x='Year', y='Social support', data=india, marker='o', markersize=10);
	sns.set_style('whitegrid')
	sns.despine(left=True)
	plt.title("India's Social support over the years", fontsize=18, fontweight='bold', pad=20)
	plt.xlabel('Year')
	str1, str2, str3, str4 = vis_res.visualisation_result_social_support(india)
	msg = '----------------- Auto Generated Conclusion -----------------\n' + str1 + '\n' + str2 + '\n--------------------------------------------------------------------------' + '\n' + str3 + '\n' + str4 + '\n--------------------------------------------------------------------------'
	plt.text(2010, 0.63, msg, fontsize=12, color='blue')
	plt.show()

def lifeExpectancy(india):
	plt.figure(figsize=(18, 6))
	sns.lineplot(x='Year', y='Healthy life expectancy at birth', data=india, marker='o', markersize=10);
	sns.set_style('whitegrid')
	sns.despine(left=True)
	plt.title("India's life expectancy at birth over the years", fontsize=18, fontweight='bold', pad=20)
	plt.xlabel('Year')
	str1, str2, str3, str4 = vis_res.visualisation_result_healthy_life_expectancy(india)
	msg = '----------------- Auto Generated Conclusion -----------------\n' + str1 + '\n' + str2 + '\n--------------------------------------------------------------------------' + '\n' + str3 + '\n' + str4 + '\n--------------------------------------------------------------------------'
	plt.text(2006, 59, msg, fontsize=12, color='blue')
	plt.show()

def freedomToMakeLifeChoices(india):
	plt.figure(figsize=(18, 6))
	sns.lineplot(x='Year', y='Freedom to make life choices', data=india, marker='o', markersize=10);
	sns.set_style('whitegrid')
	sns.despine(left=True)
	plt.title("India's Freedom to make life choices over the years", fontsize=18, fontweight='bold', pad=20)
	plt.xlabel('Year')
	str1, str2, str3, str4 = vis_res.visualisation_result_freedom_to_make_life_choice(india)
	msg = '----------------- Auto Generated Conclusion -----------------\n' + str1 + '\n' + str2 + '\n--------------------------------------------------------------------------' + '\n' + str3 + '\n' + str4 + '\n--------------------------------------------------------------------------'
	plt.text(2013, 0.63, msg, fontsize=12, color='blue')
	plt.show()

def generosity(india):
	plt.figure(figsize=(18, 6)) 
	sns.lineplot(x='Year', y='Generosity', data=india, marker='o', markersize=10); sns.set_style('whitegrid') 
	sns.despine(left=True) 
	plt.title("India's Generosity over the years", fontsize=18, fontweight='bold', pad=20) 
	plt.xlabel('') 
	str1, str2, str3, str4 = vis_res.visualisation_result_generosity(india)
	msg = '----------------- Auto Generated Conclusion -----------------\n' + str1 + '\n' + str2 + '\n--------------------------------------------------------------------------' + '\n' + str3 + '\n' + str4 + '\n--------------------------------------------------------------------------'
	plt.text(2006, 0.05, msg, fontsize=12, color='blue')
	plt.show()

def perceptionsOfCorruptions(india):
	plt.figure(figsize=(18, 6))
	sns.lineplot(x='Year', y='Perceptions of corruption', data=india, marker='o', markersize=10);
	sns.set_style('whitegrid')
	sns.despine(left=True)
	plt.title("India's Perceptions of corruption over the years", fontsize=18, fontweight='bold', pad=20)
	plt.xlabel('Year')
	str1, str2, str3, str4 = vis_res.visualisation_perceptions_of_corruptions(india)
	msg = '----------------- Auto Generated Conclusion -----------------\n' + str1 + '\n' + str2 + '\n--------------------------------------------------------------------------' + '\n' + str3 + '\n' + str4 + '\n--------------------------------------------------------------------------'
	plt.text(2012, 0.84, msg, fontsize=12, color='blue')
	plt.show()


def visualiseMenu(root, data):
	helv36 = font.Font(family='Arial', size=12)
	win = Tk()
	win.title('Visualisation')
	prepareData(data)
	print(india)
	b1 = Button(win, text='India’s Ladder Score Over the Years', font=helv36, fg='white', bg='green', command=lambda:ladderScore(india))
	b1.pack(fill=X, padx=50, pady=10)

	b2 = Button(win, text='India’s Log GDP per capita Over the Years', font=helv36, fg='white', bg='green', command=lambda:logGDPPerCapita(india))
	b2.pack(fill=X, padx=50, pady=10)

	b3 = Button(win, text='India’s Social Support Over the years', font=helv36, fg='white', bg='green', command=lambda:socialSupport(india))
	b3.pack(fill=X, padx=50, pady=10)
	
	b4 = Button(win, text='India’s Life Expectancy At Birth Over the years', font=helv36, fg='white', bg='green', command=lambda:lifeExpectancy(india))
	b4.pack(fill=X, padx=50, pady=10)

	b5 = Button(win, text='India’s Freedom To Make Life Choices Over the years', font=helv36, fg='white', bg='green', command=lambda:freedomToMakeLifeChoices(india))
	b5.pack(fill=X, padx=50, pady=10)

	b6 = Button(win, text='India’s Generosity Over the years', font=helv36, fg='white', bg='green', command=lambda:generosity(india))
	b6.pack(fill=X, padx=50, pady=10)

	b7 = Button(win, text='India’s Perceptions Of Corruption Over the years', font=helv36, fg='white', bg='green', command=lambda:perceptionsOfCorruptions(india))
	b7.pack(fill=X, padx=50, pady=10)

