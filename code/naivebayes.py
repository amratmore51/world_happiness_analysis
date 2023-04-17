import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from tkinter import *
import comparison
from sklearn.metrics import mean_absolute_percentage_error
from tkinter import messagebox
import tkinter.font as font
from sklearn import metrics

def back(current, previous):
	current.withdraw()
	previous.deiconify()

def dropColumns(filepath):
    global data
    data = pd.read_csv(filepath)
    data = data.drop(['Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
                                  'Explained by: Log GDP per capita', 'Explained by: Social support',
                                  'Explained by: Healthy life expectancy',
                                  'Explained by: Freedom to make life choices',
                                  'Explained by: Generosity', 'Explained by: Perceptions of corruption'], axis=1)
    data.dropna(inplace=True)

def selectPredictors(data):
    # Split the Predictors and Prediction Attributes
    # Column No 4 to 9 are predictors, i.e. Logged GDP per capita, Social support, Healthy life expectancy, Freedom to make life choices, Generosity, Perceptions of corruption
    # Column No 3 is Prediction i.e. Ladder Score (happiness index)

    X = data.iloc[:, 4:11].values
    Y = data.iloc[:, 3].values
    X = X.astype('int')
    Y = Y.astype('int')
    print(X)
    print(Y)
    return X, Y

def calculateAccuracy():
    accuracy = 100 - np.mean(mean_absolute_percentage_error(y_test,y_pred))
    print('Accuracy:', round(accuracy, 2), '%.')
    s = 'Accuracy of Regression Model: ' + str(round(accuracy, 2)) + '%.'
    messagebox.showinfo('Percentage Accuracy', s)


def createModel(filepath):
    dropColumns(filepath)

    X, Y = selectPredictors(data)

    global X_train, X_test, y_train, y_test, y_pred
    # Split the dataset into train and test dataset
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state = 45)

    print(X_train.shape, y_train.shape)
    print(type(X_train), type(y_train))
    messagebox.showinfo('Create Model', 'Naive Bayes model is created')


def trainModel():
    # Train Model
    global model
    model = GaussianNB()
    model.fit(X_train, y_train)
    messagebox.showinfo('Train Model', 'Naive Bayes model is trained')

def calculateAccuracy():
    y_pred = model.predict(X_test)
    print(y_pred)
    accuracy = 100 * metrics.accuracy_score(y_test, y_pred)
    comparison.naivebayes_accuracy = accuracy

    print("Accuracy:", accuracy)
    s = 'Accuracy of Naive Bayes Model : ' + str(accuracy) + ' %'
    messagebox.showinfo('Accuracy', s)

def predictScore(predWin, filepath):
    a = float(logged_gdp_per_capita_entry.get())
    b = float(social_support_entry.get())
    c = float(healthy_life_expectancy_entry.get())
    d = float(freedom_to_make_life_choices_entry.get())
    e = float(generosity_entry.get())
    f = float(perceptions_of_corruption_entry.get())
    g = float(dystopia_residual_entry.get())

    # Prediction
    # Input: Logged GDP per capita, Social support, Healthy life expectancy, Freedom to make life choices, Generosity, Perceptions of corruption, Dystopia + residual

    #prediction = model.predict([[10.77, 0.95, 72, 0.94, -0.098, 0.186, 3.2]])

    prediction = model.predict([[a,b,c,d,e,f,g]]) 
    print(prediction)
    comparison.naive_bayes_prediction = prediction
    
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
    predWin.title("Prediction Using Naive Bayes")
    predWin.configure(bg='white')

    Label(predWin, text="Prediction of Happiness/Ladder Score using Naive Bayes Algorithm", bg='white', fg='green', font='Arial 18 bold').grid(row=0, column=0, columnspan=2, pady=20)

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

    Label(predWin, text="Logged GDP per Capita * ", bg='white', fg='green').grid(row=1, column=0, padx=20, pady=10)
    logged_gdp_per_capita_entry = Entry(predWin, textvariable=logged_gdp_per_capita)
    logged_gdp_per_capita_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(predWin, text="Social Support * ", bg='white', fg='green').grid(row=2, column=0, padx=20, pady=10)
    social_support_entry = Entry(predWin, textvariable=social_support)
    social_support_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(predWin, text="Healthy Life Expectancy * ", bg='white', fg='green').grid(row=3, column=0, padx=20, pady=10)
    healthy_life_expectancy_entry = Entry(predWin, textvariable=healthy_life_expectancy)
    healthy_life_expectancy_entry.grid(row=3, column=1, padx=10, pady=10)

    Label(predWin, text="Freedom to Make Life Choices * ", bg='white', fg='green').grid(row=4, column=0, padx=20, pady=10)
    freedom_to_make_life_choices_entry = Entry(predWin, textvariable=freedom_to_make_life_choices)
    freedom_to_make_life_choices_entry.grid(row=4, column=1, padx=10, pady=10)

    Label(predWin, text="Generosity * ", bg='white', fg='green').grid(row=5, column=0, padx=20, pady=10)
    generosity_entry = Entry(predWin, textvariable=generosity)
    generosity_entry.grid(row=5, column=1, padx=10, pady=10)

    Label(predWin, text="Perceptions of Corruption * ", bg='white', fg='green').grid(row=6, column=0, padx=20, pady=10)
    perceptions_of_corruption_entry = Entry(predWin, textvariable=perceptions_of_corruption)
    perceptions_of_corruption_entry.grid(row=6, column=1, padx=10, pady=10)

    Label(predWin, text="Dystopia / Residual * ", bg='white', fg='green').grid(row=7, column=0, padx=20, pady=10)
    dystopia_residual_entry = Entry(predWin, textvariable=dystopia_residual)
    dystopia_residual_entry.grid(row=7, column=1, padx=10, pady=10)

    Button(predWin, text="Predict", width=15, height=1, bg='green', fg='white',
           command=lambda: predictScore(predWin, filepath)).grid(row=9, column=0, padx=20, pady=10)

    Button(predWin, text="Clear All", width=15, height=1, bg='green', fg='white',
            command  = clearAll).grid(row=9, column=1, padx=10, pady=10)

    predWin.eval('tk::PlaceWindow %s center' % predWin.winfo_pathname(predWin.winfo_id()))	# used to disply the window at the center of screen	
    predWin.mainloop()

def naiveBayesOptions(root, filepath):
    root.withdraw()
    win =Tk()
    win.title('Naive Bayes Algorithm')
    helv36 = font.Font(family='Arial', size=12)

    b1 = Button(win, text='Create Naive Bayes Model', font=helv36, fg='white', bg='green', command=lambda:createModel(filepath))
    b1.pack(fill=X, padx=50, pady=10)

    b2 = Button(win, text='Train the Model', font=helv36, fg='white', bg='green', command=trainModel)
    b2.pack(fill=X, padx=50, pady=10)

    #b3 = Button(win, text='Plot Regression Line', font=helv36, fg='white', bg='green', command=plotRegressionLine)
    #b3.pack(fill=X, padx=50, pady=10)

    #b4 = Button(win, text='Display Coefficents', font=helv36, fg='white', bg='green', command=displayCoefficients)
    #b4.pack(fill=X, padx=50, pady=10)

    b5 = Button(win, text='Calculate Model Accuracy', font=helv36, fg='white', bg='green', command=calculateAccuracy)
    b5.pack(fill=X, padx=50, pady=10)

    b6 = Button(win, text='Prediction of Happiness Score using Naive Bayes', font=helv36, fg='white', bg='green', command=lambda:predictionWindow(root, filepath))
    b6.pack(fill=X, padx=50, pady=10)

    b7 = Button(win, text='<-- Back to Main Menu', fg='white', bg='green', command=lambda:back(win, root))
    b7.pack(side=LEFT, expand=1)

    win.eval('tk::PlaceWindow %s center' % win.winfo_pathname(win.winfo_id()))	# used to disply the window at the center of screen	
    win.mainloop()
