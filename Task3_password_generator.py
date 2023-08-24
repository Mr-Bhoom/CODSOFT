import random
from tkinter import *
from tkinter.ttk import *
from functools import partial

#def upperpg():
def low():
	entry.delete(0, END)
	length = var1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""

	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password

	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password

	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(digits)
		return password
	else:
		print("Please choose an option")

def generate():
	password1 = low()
	entry.insert(10, password1)

def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)

def Login(username):
	print("username entered :", username.get())
	return

root = Tk()  
root.geometry('400x150')  
root.title('Password Generator')
var = IntVar()
var1 = IntVar()
root.title("Random Password Generator")

usernameLabel = Label(root, text="User Name :").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1)

Random_password = Label(root, text="Password Generated :")
Random_password.grid(row=2)
entry = Entry(root)
entry.grid(row=2, column=1)

c_label = Label(root, text="Length :")
c_label.grid(row=1)

copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=4, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=2, column=2)

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)

combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, 24, 25,
				26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

Login = partial(Login,username)

loginButton = Button(root, text="Login", command=Login).grid(row=4, column=0)  

root.mainloop()
