import comparison
from tkinter import *

regression_prediction = 0
naive_bayes_prediction = 0

regression_accuracy = 0
naivebayes_accuracy = 0

def compare():
    compareWin = Tk()
    compareWin.title("Comparisons of Predictions")
    compareWin.configure(bg='white')

    l = Label(compareWin, text="Comparison of the results of Regression & Naive Bayes", bg='white', fg='black', font='Arial 16 bold')
    l.pack(padx=20, pady=20)

    text1 = 'Happiness Score predicted by Regression  :   ' + str(regression_prediction) 
    text2 = 'Happiness Score predicted by Naive Bayes :   ' + str(naive_bayes_prediction)

    text3 = 'Accuracy of Regression  :   ' + str(regression_accuracy) + ' %'
    text4 = 'Accuracy of Naive Bayes :   ' + str(naivebayes_accuracy) + ' %'
    
    l1 = Label(compareWin, text=text1, bg='white', fg='green', font='Arial 12')
    l1.pack(pady=10)

    l2 = Label(compareWin, text=text2, bg='white', fg='green', font='Arial 12')
    l2.pack(pady=10)

    l3 = Label(compareWin, text=text3, bg='white', fg='blue', font='Arial 12')
    l3.pack(pady=10)

    l4 = Label(compareWin, text=text4, bg='white', fg='blue', font='Arial 12')
    l4.pack(pady=10)

    if(regression_accuracy > naivebayes_accuracy):
        text5 = 'Regression Algorithm gives more accurate results.'
    else:
        text5 = 'Naive Bayes Algorithm gives more accurate results.'

    l5 = Label(compareWin, text=text5, bg='white', fg='red', font='Arial 14')
    l5.pack(pady=10)
        
    compareWin.eval('tk::PlaceWindow %s center' % compareWin.winfo_pathname(compareWin.winfo_id()))	# used to disply the window at the center of screen	
    compareWin.mainloop()



