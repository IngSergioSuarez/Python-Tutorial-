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

# functions of the program this lines contains the functionallity of all the buttons

def convert():
    """
    this function will be the main function, will filter the logs file from the Dispatch
    log box and filter into the threeview 
    """
    return

def clear():
    """
    when the user press this button the values in the textbox of the Dispatch Logs, 
    and the filter vaules in the threview will be erase 
    """
    return

def search(): 

    """
    Option to search values 
    """
    return


# Frame where we're place the Log strings to filter

logs_info_frame = LabelFrame(mainFrame, text='Logs info')
logs_info_frame.grid(row=0, column=0, padx= 20, pady= 10)
label_dispatch_log = Label(logs_info_frame, text='Dispatch Log: ')
label_dispatch_log.grid(row=0, column=0, sticky=W, padx= 10)
original_string_log = ScrolledText(logs_info_frame)
original_string_log.grid(row= 1, column=0, padx= 10, pady=5)
original_string_log.config(width=60, height=15)

# Frame for the buttons 

buttons_frame = LabelFrame(mainFrame)
buttons_frame.grid(row=1, column=0, padx= 20, pady= 5)

# // CONVERT BUTTON//

button_filter_logs = Button(buttons_frame, text = "Filter", command= convert)
button_filter_logs.grid(row = 0, rowspan= 2, column= 0, padx= 5, pady= 5)
button_filter_logs.config(height= 2, width= 16)

# // CLEAR BUTTON//

button_clear_logs = Button(buttons_frame, text = "Clear", command= clear)
button_clear_logs.grid(row = 0, rowspan= 2, column= 1, padx= 5, pady= 5)
button_clear_logs.config(height= 2, width= 16)

# // SEARCH BUTTON//

label_search_logs = Label(buttons_frame, text="Search: ")
label_search_logs.grid(row= 0, column= 2, sticky= W)

entry_search_logs = Entry(buttons_frame, text="Search: ")
entry_search_logs.grid(row= 1, column= 2, pady= 5, padx= (0, 5))

button_search_logs = Button(buttons_frame, text = "Search", command= search)
button_search_logs.grid(row = 0, column= 3, rowspan= 2, padx= 5, pady= 5)
button_search_logs.config(height= 2, width= 16)



"""
# // CLEAR BUTTON//

button_clear_logs = Button(buttons_frame, text = "Clear", command= clear)
button_clear_logs.grid(row = 0, column= 1, padx= 10, pady= 10)

"""

myApp.mainloop()
