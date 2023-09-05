from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="look I Clicked a Button!!!")
    myLabel.pack()


myButton =Button(root, text="Click me!", command= myClick)
myButton.pack()

root.mainloop()