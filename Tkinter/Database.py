from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Ejercicio de Base de datos')
root.geometry("400x400")

# Databases


#Create a table
'''
c.execute(""" CREATE TABLE "addresses" (
         first_name text,
         last_name text,
         address text,
         city text,
         state text,
         zipcode integer
)
""")'''
# Create Submit Function For Database

def submit():

    #Create a database or connect to one
    conn = sqlite3.connect('address_book2.db')

    #Create a cursor
    c = conn.cursor()
    

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get(),
              }
              
              )

    #Commit changes 
    conn.commit()

    #Close connection
    conn.close()



    # Clear the text boxes when we click submit. 
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query Function For Database

def query():

    #Create a database or connect to one
    conn = sqlite3.connect('address_book2.db')

    #Create a cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    #Commit changes 
    conn.commit()

    #Close connection
    conn.close()


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

f_name_label = Label(root, text = "First name: ").grid(row= 0, column=0, padx= 10, pady= 5)
l_name_label = Label(root, text = "Last name: ").grid(row= 1, column=0, padx= 10, pady= 5)
address_label = Label(root, text = "address: ").grid(row= 2, column=0, padx= 10, pady= 5)
city_label = Label(root, text = "city: ").grid(row= 3, column=0, padx= 10, pady= 5)
state_label = Label(root, text = "State: ").grid(row= 4, column=0, padx= 10, pady= 5)
zipcode_label = Label(root, text = "Zip code: ").grid(row= 5, column=0, padx= 10, pady= 5)

# Create a Submit button 

submit_btn = Button(root, text = "Add record to Database", command = submit)
submit_btn.grid(row= 6, column= 0, columnspan= 2, pady= 10, padx= 10, ipadx= 100)

# Create a Query Button

query_btn = Button(root, text= "Show Records", command= query)
query_btn.grid(row= 7, column= 0, columnspan= 2, pady= 10, padx= 10, ipadx= 126)

root.mainloop()