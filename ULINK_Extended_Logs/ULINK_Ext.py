
from tkinter import *
from tkinter import ttk as ttk
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText 
import os

myApp = Tk()

myApp.title("Ulink_Extended_Logs")



mainFrame = Frame(myApp)
mainFrame.pack()

def openFile():
    log_file = fd.askopenfilename(title="Open")
    f = open(log_file, 'r')
    
    lineas = f.readlines()

    for l in lineas:
        if "Ulink" in l:
            print(l)


logs_info_frame = LabelFrame(mainFrame, text='Logs info')
logs_info_frame.grid(row=0, column=0, padx= 20, pady= 10)

button_open_file = Button(logs_info_frame, text= "Open file", command=openFile)
button_open_file.grid(row=0, column=0, padx= 20, pady= 5)



myApp.mainloop()