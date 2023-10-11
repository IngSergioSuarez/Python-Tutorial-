"""ULINK application"""

from tkinter import *
from tkinter import ttk as ttk
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText 
import transactions.ticket_transaction as TT



myApp = Tk()

myApp.title('ULINK logs')
# myApp.geometry('600x400')

mainFrame = Frame(myApp)
mainFrame.pack()

# Frame where we're place the Log strings to filter

logs_info_frame = LabelFrame(mainFrame, text='Logs info')
logs_info_frame.grid(row=0, column=0, padx= 20, pady= 10)
label_dispatch_log = Label(logs_info_frame, text='Dispatch Log: ')
label_dispatch_log.grid(row=0, column=0, sticky=W, padx= 10)
original_string_log = ScrolledText(logs_info_frame)
original_string_log.grid(row= 1, column=0, padx= 10, pady=5)
original_string_log.config(width=60, height=15)

myApp.mainloop()
