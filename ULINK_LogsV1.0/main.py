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


# frame's functions logs_info_frame 

def select_file():

    global myLogFile
    fileTypes= (
        ('Text files', '*,txt'),
        ('All files', '*,*')
    )
    myLogFile = fd.askopenfilename(
        title = 'Open a file',
        initialdir= '/',
        filetypes= fileTypes
    )


# Frame where we're place the Log strings to filter

logs_info_frame = LabelFrame(mainFrame, text='Logs info')
logs_info_frame.grid(row=0, column=0, padx= 20, pady= 10)

label_dispatch_log = Label(logs_info_frame, text='Dispatch Log: ')
label_dispatch_log.grid(row=0, column=0)
label_dispatch_file = Label(logs_info_frame, text='Dispatch File: ')
label_dispatch_file.grid(row=0, column=1)
label_log_type = Label(logs_info_frame, text='Log Type: ')
label_log_type.grid(row=0, column=2)

entry_dispatch_log = Entry(logs_info_frame)
entry_dispatch_log.grid(row=1, column=0, padx= 10, pady=10)

button_open_dispatch_log = Button(logs_info_frame, text= 'Open file', command=select_file)
button_open_dispatch_log.grid(row=1, column=1, padx= 10, pady=10)
button_open_dispatch_log.config(width= 20)

combobox_log_type = ttk.Combobox(logs_info_frame, values=['Ticket', 'Mix transaction', 'Inventory'])
combobox_log_type.grid(row=1, column=2, padx= 10, pady=10)

# Button to filter the logs

def logs_filter():

    global log_value 
    log_value = entry_dispatch_log.get()

    logs_filter_results = Tk()
    logs_filter_results.title('ULINK logs')

    mainFrame_logs_filter_results= Frame(logs_filter_results)
    mainFrame_logs_filter_results.pack()
    
    logs_info_filter_results_frame = LabelFrame(mainFrame_logs_filter_results, text='Logs Results')
    logs_info_filter_results_frame.grid(row=0, column=0, padx= 20, pady= 10)

    original_string_log = ScrolledText(logs_info_filter_results_frame)
    original_string_log.grid(row= 0, column= 0, padx= 10, pady=5)
    original_string_log.config(width=40, height=15)

    filter_string_log = ScrolledText(logs_info_filter_results_frame)
    filter_string_log.grid(row= 0, column= 1, padx= 10, pady=5)
    filter_string_log.config(width=40, height=15)

    options_results_frame = LabelFrame(mainFrame_logs_filter_results, text='Options')
    options_results_frame.grid(row=1, column=0, padx= 20, pady= 10)

    original_string_log.config(state= NORMAL)
    original_string_log.insert(END, log_value)
    original_string_log.config(state= DISABLED)



    # Functions of the frome Options 

    def copy_results():
        print(TT.mix_transaction)
    
    def clean_results():
        return
    
    def search_results():
        return

    button_copy = Button(options_results_frame, text= 'Copy results', command = copy_results)
    button_copy.grid(row= 0, column=0, padx=10, pady=10)
    button_copy.config(width= 30, height=2)

    button_clean = Button(options_results_frame, text= 'Clear results', command = clean_results)
    button_clean.grid(row= 0, column=1, padx=10, pady=10)
    button_clean.config(width= 30, height=2)

    button_search = Button(options_results_frame, text= 'Search results', command = search_results)
    button_search.grid(row= 0, column=2, padx=10, pady=10)
    button_search.config(width= 30, height=2)

    logs_filter_results.mainloop()


    return

button_logs_filter = Button(mainFrame, text= "Filter Logs", command= logs_filter)
button_logs_filter.grid(row=1, column=0, sticky='news', padx= 10, pady= 5)


myApp.mainloop()
