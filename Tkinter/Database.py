from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Ejercicio de Base de datos')
root.geometry("400x400")

# Databases

#Create a database or connect to one
conn = sqlite3.connect('address_book.db')

#Create a cursor
c = conn.cursor()



#Create text boxes

f_name = Entry(root, width= 30)
f_name.grid(row=0, column=1, padx= 20, pady=5)

l_name = Entry(root, width= 30)
l_name.grid(row=1, column=1, padx= 20, pady=5)

address = Entry(root, width= 30)
address.grid(row=2, column=1, padx= 20, pady=5)

city = Entry(root, width= 30)
city.grid(row=3, column=1, padx= 20, pady=5)

state = Entry(root, width= 30)
state.grid(row=4, column=1, padx= 20, pady=5)

zipcode = Entry(root, width= 30)
zipcode.grid(row=5, column=1, padx= 20, pady=5)

#Create the labels

f_name_label = Label(root, text = "First name: "). grid(row= 0, column=0, padx= 10, pady= 5)
l_name_label = Label(root, text = "Last name: "). grid(row= 1, column=0, padx= 10, pady= 5)
address_name_label = Label(root, text = "address: "). grid(row= 2, column=0, padx= 10, pady= 5)
city_label = Label(root, text = "city: "). grid(row= 3, column=0, padx= 10, pady= 5)
state_label = Label(root, text = "State: "). grid(row= 4, column=0, padx= 10, pady= 5)
zipcode_label = Label(root, text = "Zip code: "). grid(row= 5, column=0, padx= 10, pady= 5)


'''

#Create a table

c.execute(""" CREATE TABLE addresses(
         first_name text,
         last_name text,
          address text,
          city text
          state text,
          zipcode integer,
)
""")'''

#Commit changes 
conn.commit()

#Close connection
conn.close()

root.mainloop()