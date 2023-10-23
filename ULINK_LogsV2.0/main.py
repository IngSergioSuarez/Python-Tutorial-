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

    for item in my_tree.get_children():
        my_tree.delete(item)

    global input_value
    input_value = original_string_log.get("1.0","end-1c")

    first_Filter_Logs = input_value[16:]
    second_Filter_Logs = first_Filter_Logs.split("<cr>")

    for x in second_Filter_Logs:

        if x.startswith('T') == True:
            ulink_field = x[:4]
            ulink_field_description = TT.tkt_transaction.get(ulink_field)
            my_tree.insert("",'end', values=(x[:4],str(ulink_field_description),x[4:]))

        else:
            ulink_field = x[:3]
            ulink_field_description = TT.tkt_transaction.get(ulink_field)
            my_tree.insert("",'end', values=(x[:3],str(ulink_field_description),x[3:]))
            

def clear():
    """
    when the user press this button the values in the textbox of the Dispatch Logs, 
    and the filter vaules in the threview will be erase 
    """
    for item in my_tree.get_children(): # remove all the information on the treeview
        my_tree.delete(item)

    original_string_log.delete('1.0', END) # Remove the information on the Dispatch log text box


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

# Frame where we are going to place the treeview

tv_frame = LabelFrame(mainFrame)
tv_frame.grid(row=2, column=0, padx= 20, pady= 5)

# Create a treeview Frame

tree_frame= Frame(tv_frame)
tree_frame.pack(pady=10)

# Create a treeview Scrollbar

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side= RIGHT, fill=Y)

# Create the treeview

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar

tree_scroll.config(command=my_tree.yview)

# Define our columns 

my_tree['columns'] = ("Field", "Description", "Value")

# Format Our Columns 

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Field", anchor=CENTER, width= 100)
my_tree.column("Description", anchor=CENTER, width= 200)
my_tree.column("Value", anchor=CENTER, width= 200)

# Create Headings

my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Field", text="Field", anchor=CENTER)
my_tree.heading("Description", text="Description", anchor=CENTER)
my_tree.heading("Value", text="Value", anchor=CENTER)



myApp.mainloop()
