from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

app = Tk()
app.title('CRM database exercise')
app.geometry('400x700')

# Connect to mysql

mydb =mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd= "68HC_908gp32",
    database = "crm_Exercise"

)

# Create a cursor and initialize it 

my_cursor = mydb.cursor()

# Create database (We just need to run once)

# my_cursor.execute("CREATE DATABASE crm_Exercise")

# Create a table

"""

my_cursor.execute('CREATE TABLE IF NOT EXISTS customers (\
                   first_name VARCHAR(255),\
                   last_name VARCHAR(255),\
                   zipcode INT(10),\
                   price_paid DECIMAL(10,2),\
                   user_id INT AUTO_INCREMENT PRIMARY KEY)')

"""

# To add more columns to an existing table we can do it in the following way
"""
my_cursor.execute( "ALTER TABLE customers ADD(\
                    email VARCHAR(255),\
                    address_1 VARCHAR(255),\
                    address_2 VARCHAR(255),\
                    city VARCHAR(50),\
                    state VARCHAR(50),\
                    country VARCHAR(255),\
                    phone VARCHAR(255),\
                    payment_method VARCHAR(50),\
                    discount_code VARCHAR(255))")
"""
# Show table

#my_cursor.execute("SELECT * FROM Customers")

# Display the values of the table 

#for thing in my_cursor.description:
#   print(thing)

# Create the APP's title 

title_label = Label(app, text= "CRM Exercise", font=("helvetica", 16)).grid(row= 0, column= 0, columnspan=2, pady= 10)

# Create Main form to enter customer Data 

# Function Clear fields

def clear_fields():
    f_name_box.delete(0, END)
    l_name_box.delete(0, END)
    zipcode_box.delete(0, END)
    price_paid_box.delete(0, END)
    email_box.delete(0, END)
    address_1_box.delete(0, END)
    address_2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)

# Create the Labels

f_name_label = Label(app, text= "First Name: ").grid(row= 1, column= 0, sticky= W, pady= 2, padx=(10,0))
l_name_label = Label(app, text= "Last Name: ").grid(row= 2, column= 0, sticky= W, pady= 2, padx=(10,0))
zipcode_label= Label(app, text= "Zipcode: ").grid(row= 3, column= 0, sticky= W, pady= 2, padx=(10,0))
price_paid_label = Label(app, text= "Price paid: ").grid(row= 4, column= 0, sticky= W, pady= 2, padx=(10,0))
email_label = Label(app, text= "Email: ").grid(row= 5, column= 0, sticky= W, pady= 2, padx=(10,0))
address_1_label = Label(app, text= "Address 1: ").grid(row= 6, column= 0, sticky= W, pady= 2, padx=(10,0))
address_2_label = Label(app, text= "Address 2: ").grid(row= 7, column= 0, sticky= W, pady= 2, padx=(10,0))
city_label = Label(app, text= "City: ").grid(row= 8, column= 0, sticky= W, pady= 2, padx=(10,0))
state_label = Label(app, text= "State: ").grid(row= 9, column= 0, sticky= W, pady= 2, padx=(10,0))
country_label = Label(app, text= "Country: ").grid(row= 10, column= 0, sticky= W, pady= 2, padx=(10,0))
phone_label = Label(app, text= "Phone: ").grid(row= 11, column= 0, sticky= W, pady= 2, padx=(10,0))
payment_method_label = Label(app, text= "Payment method: ").grid(row= 12, column= 0, sticky= W, pady= 2, padx=(10,0))
discount_code_label = Label(app, text= "Discount code: ").grid(row= 13, column= 0, sticky= W, pady= 2, padx=(10,0))

#Create the textbox

f_name_box = Entry(app, width= 40)
f_name_box.grid(row=1, column=1, pady= 5, padx= 10)
l_name_box = Entry(app, width= 40)
l_name_box.grid(row=2, column=1, pady= 5, padx= 10)
zipcode_box = Entry(app, width= 40)
zipcode_box.grid(row=3, column=1, pady= 5, padx= 10)
price_paid_box = Entry(app, width= 40)
price_paid_box.grid(row=4, column=1, pady= 5, padx= 10)
email_box = Entry(app, width= 40)
email_box.grid(row=5, column=1, pady= 5, padx= 10)
address_1_box = Entry(app, width= 40)
address_1_box.grid(row=6, column=1, pady= 5, padx= 10)
address_2_box = Entry(app, width= 40)
address_2_box.grid(row=7, column=1, pady= 5, padx= 10)
city_box = Entry(app, width= 40)
city_box.grid(row=8, column=1, pady= 5, padx= 10)
state_box = Entry(app, width= 40)
state_box.grid(row=9, column=1, pady= 5, padx= 10)
country_box = Entry(app, width= 40)
country_box.grid(row=10, column=1, pady= 5, padx= 10)
phone_box = Entry(app, width= 40)
phone_box.grid(row=11, column=1, pady= 5, padx= 10)
payment_method_box = Entry(app, width= 40)
payment_method_box.grid(row=12, column=1, pady= 5, padx= 10)
discount_code_box = Entry(app, width= 40)
discount_code_box.grid(row=13, column=1, pady= 5, padx= 10)

# Create buttons

add_customer_button = Button(app, text= "Add Customer")
add_customer_button.grid(row= 14, column=0, padx= 10, pady= 5)

clear_fields_button = Button(app, text= "Clear Fields", command=clear_fields)
clear_fields_button.grid(row= 14, column=1, padx= 10, pady= 5)

app.mainloop()
