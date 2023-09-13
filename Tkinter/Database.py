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

#Commit changes 
conn.commit()

#Close connection
#conn.close()

#Create a table

c.execute(""" CREATE TABLE addresses(
          first_name text,
          last_name text,
          address text,
          city text
          state text,
          zipcode integer,
)
""")

root.mainloop()