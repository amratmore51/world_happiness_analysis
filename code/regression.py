from sklearn.linear_model import LinearRegression
import pandas as pd
from tkinter import *
import comparison
import tkinter.font as font
from pandastable import Table
from tkinter import messagebox
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
from sklearn import metrics
import numpy as np

def back(current, previous):
	current.withdraw()
	previous.deiconify()

def dropColumns(filepath):
    data = pd.read_csv(filepath)
    global happiness_report
    happiness_report = data.drop(['Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
                                  'Explained by: Log GDP per capita', 'Explained by: Social support',
                                  'Explained by: Healthy life expectancy',
                                  'Explained by: Freedom to make life choices',
                                  'Explained by: Generosity', 'Explained by: Perceptions of corruption', 'Ladder score in Dystopia'], axis=1)


def predictScore(predWin, filepath):
    a = float(logged_gdp_per_capita_entry.get())
    b = float(social_support_entry.get())
    c = float(healthy_life_expectancy_entry.get())
    d = float(freedom_to_make_life_choices_entry.get())
    e = float(generosity_entry.get())
    f = float(perceptions_of_corruption_entry.get())
    g = float(dystopia_residual_entry.get())

    # Input: Logged GDP per capita, Social support, Healthy life expectancy, Freedom to make life choices, Generosity, Perceptions of corruption, Dystopia + residual

    prediction = lm.predict([[a,b,c,d,e,f,g]]) 

    comparison.regression_prediction = prediction

    print('The Predicted Happiness Score is : ', prediction)
    print(type(prediction))
    msg = 'The Predicted Happiness Score is : ' + str(prediction)
    Label(predWin, text=msg, bg='white', fg='blue', font='Times 24 bold').grid(row=10, column=0, columnspan=2, pady=20)

def clearAll():
    logged_gdp_per_capita_entry.delete(0, END)
    social_support_entry.delete(0, END)
    healthy_life_expectancy_entry.delete(0, END)
    freedom_to_make_life_choices_entry.delete(0, END)
    generosity_entry.delete(0, END)
    perceptions_of_corruption_entry.delete(0, END)
    dystopia_residual_entry.delete(0, END)

def predictionWindow(root, filepath):
    predWin = Tk()
    predWin.title("Prediction")
    predWin.configure(bg='white')

    l1 = Label(predWin, text="Prediction of Happiness/Ladder Score using Multiple Linear Regression", bg='white', fg='green', font='Arial 18 bold')
    l1.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    global logged_gdp_per_capita
    global social_support
    global healthy_life_expectancy
    global freedom_to_make_life_choices
    global generosity
    global perceptions_of_corruption
    global dystopia_residual

    logged_gdp_per_capita = StringVar()
    social_support = StringVar()
    healthy_life_expectancy = StringVar()
    freedom_to_make_life_choices = StringVar()
    generosity = StringVar()
    perceptions_of_corruption = StringVar()
    dystopia_residual = StringVar()

    global logged_gdp_per_capita_entry
    global social_support_entry
    global healthy_life_expectancy_entry
    global freedom_to_make_life_choices_entry
    global generosity_entry
    global perceptions_of_corruption_entry
    global dystopia_residual_entry

    Label(predWin, text="Logged GDP per Capita * ", bg='white', fg='blue').grid(row=1, column=0, padx=20, pady=10)
    logged_gdp_per_capita_entry = Entry(predWin, textvariable=logged_gdp_per_capita)
    logged_gdp_per_capita_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(predWin, text="Social Support * ", bg='white', fg='blue').grid(row=2, column=0, padx=20, pady=10)
    social_support_entry = Entry(predWin, textvariable=social_support)
    social_support_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(predWin, text="Healthy Life Expectancy * ", bg='white', fg='blue').grid(row=3, column=0, padx=20, pady=10)
    healthy_life_expectancy_entry = Entry(predWin, textvariable=healthy_life_expectancy)
    healthy_life_expectancy_entry.grid(row=3, column=1, padx=10, pady=10)

    Label(predWin, text="Freedom to Make Life Choices * ", bg='white', fg='blue').grid(row=4, column=0, padx=20, pady=10)
    freedom_to_make_life_choices_entry = Entry(predWin, textvariable=freedom_to_make_life_choices)
    freedom_to_make_life_choices_entry.grid(row=4, column=1, padx=10, pady=10)

    Label(predWin, text="Generosity * ", bg='white', fg='blue').grid(row=5, column=0, padx=20, pady=10)
    generosity_entry = Entry(predWin, textvariable=generosity)
    generosity_entry.grid(row=5, column=1, padx=10, pady=10)

    Label(predWin, text="Perceptions of Corruption * ", bg='white', fg='blue').grid(row=6, column=0, padx=20, pady=10)
    perceptions_of_corruption_entry = Entry(predWin, textvariable=perceptions_of_corruption)
    perceptions_of_corruption_entry.grid(row=6, column=1, padx=10, pady=10)

    Label(predWin, text="Dystopia / Residual * ", bg='white', fg='blue').grid(row=7, column=0, padx=20, pady=10)
    dystopia_residual_entry = Entry(predWin, textvariable=dystopia_residual)
    dystopia_residual_entry.grid(row=7, column=1, padx=10, pady=10)

    Button(predWin, text="Predict", width=15, height=1, bg='green', fg='white',
           command=lambda: predictScore(predWin, filepath)).grid(row=9, column=0, padx=20, pady=10)

    Button(predWin, text="Clear All", width=15, height=1, bg='green', fg='white',
            command  = clearAll).grid(row=9, column=1, padx=10, pady=10)

    predWin.eval('tk::PlaceWindow %s center' % predWin.winfo_pathname(predWin.winfo_id()))	 
    predWin.mainloop()


def displayCoefficients():
    coefWin = Tk()
    coefWin.title('Display Coefficients')
    
    print('Estimated Intercept is: ', lm.intercept_)
    print('No of coefficients in this model are: ', lm.coef_)

    coef = zip(X.columns, lm.coef_)
    coef_df = pd.DataFrame(list(coef), columns=['features', 'coefficients'])
    print(coef_df)

    f = LabelFrame(coefWin, text='Features & their Coefficients', borderwidth = 5, fg = 'blue')	# Create a frame
    f.pack(fill=BOTH,expand=1)
    t = Table(f, dataframe=coef_df)
    t.show()
    coefWin.eval('tk::PlaceWindow %s center' % coefWin.winfo_pathname(coefWin.winfo_id()))	 
    coefWin.mainloop()


def createModel(filepath):
    dropColumns(filepath)
    # print(happiness_report)

    dropped_happiness_report = happiness_report.drop(['Country name', 'Regional indicator'], axis=1)
    #print(dropped_happiness_report)
    global X, Y
    X = dropped_happiness_report.drop('Ladder score', axis=1) # All columns except Ladder Score
    Y = dropped_happiness_report['Ladder score'] # Ladder Score Column

    global lm
    lm = LinearRegression()
    messagebox.showinfo('Model Created', 'Regression Model Successfully Trained')

def trainModel():
    lm.fit(X, Y)
    messagebox.showinfo('Model Trained', 'Regression Model Training Successful')

def plotRegressionLine():
    Y_pred = lm.predict(X)
    plt.title('Regression Line')
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.show()

def calculateAccuracy():
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state = 45)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    '''
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    s = 'Accuracy of Regression Model : ' + str(metrics.accuracy_score(y_test, y_pred))
    messagebox.showinfo('Accuracy', s)

    '''
    accuracy1 = 100.0 - np.mean(mean_absolute_percentage_error(y_test,y_pred))
    comparison.regression_accuracy = accuracy1

    #print('Accuracy:', round(accuracy, 2), '%.')
    #s = 'Accuracy of Regression Model: ' + str(round(accuracy, 2)) + '%.'
    s1 = 'Accuracy of Regression Model: ' + str(accuracy1) + ' %'
    messagebox.showinfo('Percentage Accuracy', s1)

    '''
    accuracy2 = model.score(X_train, y_train)
    s2 = 'Accuracy Score: ' + str(accuracy2) + '%.'
    messagebox.showinfo('Percentage Accuracy', s2)
    '''

def regressionOptions(root, filepath):
    root.withdraw()
    win =Tk()
    win.title('Multiple Regression Algorithm')
    helv36 = font.Font(family='Arial', size=12)

    b1 = Button(win, text='Create Regression Model', font=helv36, fg='white', bg='green', command=lambda:createModel(filepath))
    b1.pack(fill=X, padx=50, pady=10)

    b2 = Button(win, text='Train the Model', font=helv36, fg='white', bg='green', command=trainModel)
    b2.pack(fill=X, padx=50, pady=10)

    #b3 = Button(win, text='Plot Regression Line', font=helv36, fg='white', bg='green', command=plotRegressionLine)
    #b3.pack(fill=X, padx=50, pady=10)

    b4 = Button(win, text='Display Coefficents', font=helv36, fg='white', bg='green', command=displayCoefficients)
    b4.pack(fill=X, padx=50, pady=10)

    b5 = Button(win, text='Calculate Model Accuracy', font=helv36, fg='white', bg='green', command=calculateAccuracy)
    b5.pack(fill=X, padx=50, pady=10)

    b6 = Button(win, text='Prediction of Happiness Score', font=helv36, fg='white', bg='green', command=lambda:predictionWindow(root, filepath))
    b6.pack(fill=X, padx=50, pady=10)

    b7 = Button(win, text='<-- Back to Main Menu', fg='white', bg='green', command=lambda:back(win, root))
    b7.pack(side=LEFT, expand=1)

    win.eval('tk::PlaceWindow %s center' % win.winfo_pathname(win.winfo_id()))	# used to disply the window at the center of screen	
    win.mainloop()

