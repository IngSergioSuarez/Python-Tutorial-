from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

app = Tk()
app.title('CRM database exercise')
app.geometry('400x400')

# Connect to mysql

mydb =mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd= "68HC_908gp32",
    database ='crm_exercise'
)

# Create a cursor and initialize it 

my_cursor = mydb.cursor()

# Create database (We just need to run once)

# my_cursor.execute("CREATE DATABASE crm_Exercise")

# Create a table

my_cursor.execute('CREATE TABLE IF NOT EXISTS customers (\
                   first_name VARCHAR(255),\
                   last_name VARCHAR(255),\
                   zipcode INT(10),\
                   price_paid DECIMAL(10,2),\
                   user_id INT AUTO_INCREMENT PRIMARY KEY)')



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

app.mainloop()