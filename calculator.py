#A simple calculator app for desktop to run. Developed to learn tkinter and GUI with Python 
#Author: Phil Fiess

try:
    #for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

import math

root= Tk()
root.title("Calculator")

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#handles which operation is being performed on the numbers
global math_operation
#global variable to store first number value when performing operations
global f_num 

#CLICK EVENT HANDLING
def button_click(number):
    current_value = e.get()
    e.delete(0, END)
    e.insert(0, str(current_value) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    #handles which operation is being performed on the numbers
    global math_operation
    #global variable to store first number value when performing operations
    global f_num 
    math_operation = "addition"
    first_num = e.get()
    f_num = int(first_num)
    e.delete(0, END)

def button_subtract():
    global math_operation
    global f_num 
    math_operation = "subtraction"
    first_num = e.get()
    f_num = int(first_num)
    e.delete(0, END)

def button_divide():
    global math_operation
    global f_num 
    math_operation = "division"
    first_num = e.get()
    f_num = int(first_num)
    e.delete(0, END)

def button_multiply():
    global math_operation
    global f_num
    math_operation = "multiplication"
    first_num = e.get()
    f_num = int(first_num)
    e.delete(0, END)

def button_mod():
    global math_operation
    global f_num
    math_operation = "modular"
    first_num = e.get()
    f_num = int(first_num)
    e.delete(0, END)

#these operators don't need a second number, and will return the value immediately on click
def button_squared():
    global math_operation
    base_num = int(e.get())
    math_operation = "squared"
    e.delete(0, END)
    e.insert(0, base_num ** 2)

def button_abs():
    global math_operation
    math_operation = "absolute"
    num = int(e.get())
    e.delete(0, END)
    e.insert(0, abs(num))

def button_factorial():
    global math_operation
    math_operation = "factorial"
    num = int(e.get())
    e.delete(0, END)
    e.insert(0, math.factorial(num))


def button_equals():
    second_number = e.get()
    e.delete(0, END)
    #parses numbers depending on operation being performed
    if math_operation == "addition":
        e.insert(0, f_num + int(second_number))
    elif math_operation == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math_operation == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math_operation == "division":
        e.insert(0, f_num / int(second_number))
    elif math_operation == "modular":
        e.insert(0, f_num % int(second_number))
    else:
        return


#OPERATOR BUTTONS
button_add = Button(root, text="+", padx=37, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=42, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)
button_mod = Button(root, text="%", padx=40, pady=20, command=button_mod)
button_squared = Button(root, text="x^2", padx=33, pady=20, command=button_squared)
button_abs = Button(root, text="|x|", padx=40, pady=20, command=button_abs)
button_factorial = Button(root, text="x!", padx=40, pady=20, command=button_factorial)

#Clear
button_clear = Button(root, text="Clear", padx=28, pady=20, command=button_clear)
#Equals
button_equals = Button(root, text="=", padx=39, pady=20, command=button_equals)

#NUMERICAL BUTTONS
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

#DECIMAL BUTTON
button_decimal = Button(root, text=".", padx=40, pady=20)


#Places buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equals.grid(row=4, column=2)

#logical operators on screen
#add, subtract, divide, multiply
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

# #modular, square, absolute value, factorial
button_mod.grid(row=1, column=4)
button_squared.grid(row=2, column=4)
button_abs.grid(row=3, column=4)
button_factorial.grid(row=4, column=4)


root.mainloop()