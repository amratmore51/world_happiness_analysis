#import modules
from tkinter import *
import os
from tkinter import messagebox
import gui 

# deletes all the widgets from a frame or window
def clearWindow(win):
	for widget in win.winfo_children():
		widget.destroy()

# Implementing event on register button
def register_user(login_frame):
	username_info = username.get()
	password_info = password.get()

	if(len(username_info)==0 and len(password_info)==0):
		messagebox.showinfo('Input Error', 'Please provide a valid Username & Password')
	elif(len(username_info)==0):
		messagebox.showinfo('Input Error', 'Please provide a valid Username')
	elif(len(password_info)==0):
		messagebox.showinfo('Input Error', 'Please provide a valid Password')
	else:
		file = open('C:\\Happiness\\login' + '\\'+str(username_info), "w")
		file.write(username_info + "\n")
		file.write(password_info)
		file.close()

		username_entry.delete(0, END)
		password_entry.delete(0, END)

		messagebox.showinfo('Success', 'Registration Successful\nPlease Go Back to Login')

# Implementing event on login button 

def login_verify(login_frame):
	username1 = username_verify.get()
	password1 = password_verify.get()

	username_login_entry.delete(0, END)
	password_login_entry.delete(0, END)

	list_of_files = os.listdir('C:\\Happiness\\login\\')
	if username1 in list_of_files:
		file1 = open('C:\\Happiness\\login\\' + username1, "r")
		verify = file1.read().splitlines()
		if password1 in verify:
			messagebox.showinfo('Success', 'Login Successful')
			clearWindow(login_frame)

			#Label(login_frame, text='Login Successful', bg='white', fg='green', font='Helvetica 20 bold').pack()

			gui.firstWindow(root, login_frame)

		else:
			messagebox.showinfo('Not Recognised', 'Password Not Recognised')
	else:
		messagebox.showinfo('Not Found', 'User Not Found')

def register(login_frame):
	clearWindow(login_frame)

	global username
	global password
	global username_entry
	global password_entry

	username = StringVar()
	password = StringVar()

	Label(login_frame, text="Register", bg="white", fg='green', font='Arial 18 bold').grid(row=0, column=0, columnspan=2, padx=20, pady=20)

	username_lable = Label(login_frame, text="Username * ", bg='white', fg='green')
	username_lable.grid(row=1, column=0, padx=20, pady=10)

	username_entry = Entry(login_frame, textvariable=username)
	username_entry.grid(row=1, column=1, padx=10, pady=10)

	password_lable = Label(login_frame, text="Password * ", bg='white', fg='green')
	password_lable.grid(row=2, column=0, padx=20, pady=10)

	password_entry = Entry(login_frame, textvariable=password, show='*')
	password_entry.grid(row=2, column=1, padx=10, pady=10)

	b1 = Button(login_frame, text="Register", width=15, height=1, bg="green", fg='white', command = lambda:register_user(login_frame))
	b1.grid(row=3, column=1, padx=20, pady=10)

	b2 = Button(login_frame, text="Back to Login", width=15, height=1, bg="green", fg='white', command = lambda:login(login_frame))
	b2.grid(row=3, column=0, padx=20, pady=10)


# Designing window for login 

def login(login_frame):
	clearWindow(login_frame)

	Label(login_frame, text="Login", bg='white', fg='green', font='Arial 18 bold').grid(row=0, column=0, columnspan=2, pady=20)

	global username_verify
	global password_verify

	username_verify = StringVar()
	password_verify = StringVar()

	global username_login_entry
	global password_login_entry

	Label(login_frame, text="Username * ", bg='white', fg='green').grid(row = 1, column = 0, padx=20, pady = 10)

	username_login_entry = Entry(login_frame, textvariable=username_verify)
	username_login_entry.grid(row = 1, column = 1, padx=10, pady = 10)

	Label(login_frame, text="Password * ", bg='white', fg='green').grid(row = 2, column = 0, padx=20, pady = 10)

	password_login_entry = Entry(login_frame, textvariable=password_verify, show= '*')
	password_login_entry.grid(row = 2, column = 1, padx=10, pady = 10)

	Button(login_frame, text="Register", width=15, height=1, bg='green', fg='white', command = lambda:register(login_frame)).grid(row = 3, column = 0, padx=20, pady = 10)

	Button(login_frame, text="Login", width=15, height=1, bg='green', fg='white', command = lambda:login_verify(login_frame)).grid(row = 3, column = 1, padx=10, pady = 10)

def mainWindow():
	global root
	root = Tk()
	root.title("Happiness Analysis")
	root.configure(bg='white')

	titleFrame = LabelFrame(root, width=1200, height=100, borderwidth = 0, fg = 'green', bg='white')
	titleFrame.grid(row=0, column=0, columnspan=2)
	titleFrame.grid_propagate(0)

	leftFrame = LabelFrame(root, width=400, height=400, borderwidth = 0, fg = 'green', bg='white')
	leftFrame.grid(row=1, column=0)
	leftFrame.grid_propagate(0)

	rightFrame = LabelFrame(root, width=700, height=400, borderwidth = 0, fg = 'green', bg='white')
	rightFrame.grid(row=1, column=1)
	rightFrame.grid_propagate(0)


	w=Label(titleFrame, text="Happiness Analysis", fg='navy', bg='white', font='Arial 24 bold')
	w.pack(pady=10)

	logo=PhotoImage(file="C:\\Happiness\\images\\sample.png")
	w1=Label(rightFrame, image=logo)
	w1.pack(fill=BOTH, expand=1)

	login(leftFrame)	

	#root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))	# used to disply the window at the center of screen	
	root.mainloop()

mainWindow()
exit()