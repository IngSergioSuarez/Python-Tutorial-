from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width= 75, borderwidth= 5)
e.grid(row= 0, column=0, columnspan= 4, padx= 10, pady= 10)

def button_Click(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_Clear():

    e.delete(0, END)

def button_Add():

    first_number = e.get()
    global f_num 
    global operation
    operation = "Adding"
    f_num = int(first_number)
    e.delete(0, END)

def button_Substract():

    first_number = e.get()
    global f_num
    global operation
    operation = "Substract"
    f_num = int(first_number)
    e.delete(0, END)

def button_Multiply():
    first_number = e.get()
    global f_num
    global operation
    operation = "Multiply"
    f_num = int(first_number)
    e.delete(0, END)

def button_Divide():
    first_number = e.get()
    global f_num
    global operation
    operation = "Divide"
    f_num = int(first_number)
    e.delete(0, END)

def button_Equal():
    second_number = e.get()
    global s_num
    s_num = int(second_number)
    e.delete(0, END)

    if operation == "adding":
        e.insert(0, f_num + int(s_num))
    elif operation == "Substract":
        e.insert(0, f_num - int(s_num))
    elif operation == "Multiply":
        e.insert(0, f_num * int(s_num))
    elif operation == "Divide":
        e.insert(0, f_num / int(s_num))

# Define Buttons

button_1 = Button(root, text = "1", padx=40, pady=20, command=lambda: button_Click(1))
button_2 = Button(root, text = "2", padx=40, pady=20, command=lambda: button_Click(2))
button_3 = Button(root, text = "3", padx=40, pady=20, command=lambda: button_Click(3))
button_4 = Button(root, text = "4", padx=40, pady=20, command=lambda: button_Click(4))
button_5 = Button(root, text = "6", padx=40, pady=20, command=lambda: button_Click(5))
button_6 = Button(root, text = "6", padx=40, pady=20, command=lambda: button_Click(6))
button_7 = Button(root, text = "7", padx=40, pady=20, command=lambda: button_Click(7))
button_8 = Button(root, text = "8", padx=40, pady=20, command=lambda: button_Click(8))
button_9 = Button(root, text = "9", padx=40, pady=20, command=lambda: button_Click(9))
button_0 = Button(root, text = "0", padx=40, pady=20, command=lambda: button_Click(0))

button_add = Button(root, text = "+", padx=40, pady=20, command=lambda: button_Add())
button_substract = Button(root, text = "-", padx=40, pady=20, command=lambda: button_Substract())
button_multiply = Button(root, text = "*", padx=40, pady=20, command=lambda: button_Multiply())
button_divide = Button(root, text = "/", padx=40, pady=20, command=lambda: button_Divide())

button_equal = Button(root, text = "=", padx=150, pady=20, command=lambda: button_Equal())
button_clear = Button(root, text = "Clear", padx=100, pady=20, command=lambda: button_Clear())

# Display the buttons on the screen

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

button_add.grid(row=1, column=4)
button_substract.grid(row=2, column= 4)
button_multiply.grid(row=3, column= 4)
button_divide.grid(row=4, column= 4)


button_clear.grid(row =4, column=1, columnspan=2)

button_equal.grid(row=5, column=0, columnspan=4)

root.mainloop()