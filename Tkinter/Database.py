from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Ejercicio de Base de datos')
root.geometry("400x600")

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

# Create Delete Function For Database

def delete():

    #Create a database or connect to one
    conn = sqlite3.connect('address_book2.db')

    #Create a cursor
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())

    #Commit changes 
    conn.commit()

    #Close connection
    conn.close()

def save_update():

    #Create a database or connect to one
    conn = sqlite3.connect('address_book2.db')

    #Create a cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name= :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
        {
            'first': f_name_update.get(),
            'last' : l_name_update.get(),
            'address' : address_update.get(),
            'city' : city_update.get(),
            'state' : state_update.get(),
            'zipcode' : zipcode_update.get(),

            'oid': record_id

        }
              )
    
    
    # Clear the text boxes when we click save. 
    f_name_update.delete(0, END)
    l_name_update.delete(0, END)
    address_update.delete(0, END)
    city_update.delete(0, END)
    state_update.delete(0, END)
    zipcode_update.delete(0, END)



    #Commit changes 
    conn.commit()

    #Close connection
    conn.close()

    update_window.destroy()

    

def update():

    global update_window

    update_window = Tk()
    update_window.title('Editor de records')
    update_window.geometry("400x400")


    #Create a database or connect to one
    conn = sqlite3.connect('address_book2.db')

    #Create a cursor
    c = conn.cursor()

    record_id = delete_box.get()

    #query the Database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # Create global variables for text box names
    
    
    global f_name_update
    global l_name_update
    global address_update
    global city_update
    global state_update
    global zipcode_update

    # Create the text boxes 

    f_name_update = Entry(update_window, width= 30)
    f_name_update.grid(row=0, column=1, padx= 20, pady=5)
    l_name_update = Entry(update_window, width= 30)
    l_name_update.grid(row=1, column=1, padx= 20, pady=5)
    address_update = Entry(update_window, width= 30)
    address_update.grid(row=2, column=1, padx= 20, pady=5)
    city_update = Entry(update_window, width= 30)
    city_update.grid(row=3, column=1, padx= 20, pady=5)
    state_update = Entry(update_window, width= 30)
    state_update.grid(row=4, column=1, padx= 20, pady=5)
    zipcode_update = Entry(update_window, width= 30)
    zipcode_update.grid(row=5, column=1, padx= 20, pady=5)


    #Create the labels

    f_name_label__update = Label(update_window, text = "First name: ").grid(row= 0, column=0, padx= 10, pady= 5)
    l_name_label__update = Label(update_window, text = "Last name: ").grid(row= 1, column=0, padx= 10, pady= 5)
    address_label_update = Label(update_window, text = "address: ").grid(row= 2, column=0, padx= 10, pady= 5)
    city_label_update = Label(update_window, text = "city: ").grid(row= 3, column=0, padx= 10, pady= 5)
    state_label_update = Label(update_window, text = "State: ").grid(row= 4, column=0, padx= 10, pady= 5)
    zipcode_label_update = Label(update_window, text = "Zip code: ").grid(row= 5, column=0, padx= 10, pady= 5)

    for record in records:
        f_name_update.insert(0, record[0])
        l_name_update.insert(0, record[1])
        address_update.insert(0, record[2])
        city_update.insert(0, record[3])
        state_update.insert(0, record[4])
        zipcode_update.insert(0, record[5])

    save_btn = Button(update_window, text= "Save Record", command= save_update)
    save_btn.grid(row= 6, column= 0, columnspan= 2, pady= 10, padx= 10, ipadx= 126)

    

    #Commit changes 
    conn.commit()

    #Close connection
    conn.close()
"""
    


"""




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

    print_records = " "
    for record in records:

        print_records += str(record) + "\n"

    query_label = Label(root, text= print_records).grid(row = 12, column= 0, columnspan= 2)

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

delete_box = Entry(root, width= 30)
delete_box.grid(row=10, column=1, padx= 20, pady=5)
 


#Create the labels

f_name_label = Label(root, text = "First name: ").grid(row= 0, column=0, padx= 10, pady= 5)
l_name_label = Label(root, text = "Last name: ").grid(row= 1, column=0, padx= 10, pady= 5)
address_label = Label(root, text = "address: ").grid(row= 2, column=0, padx= 10, pady= 5)
city_label = Label(root, text = "city: ").grid(row= 3, column=0, padx= 10, pady= 5)
state_label = Label(root, text = "State: ").grid(row= 4, column=0, padx= 10, pady= 5)
zipcode_label = Label(root, text = "Zip code: ").grid(row= 5, column=0, padx= 10, pady= 5)

delete_label = Label(root, text = "Select ID: ").grid(row= 10, column=0, padx= 10, pady= 5)

# Create a Submit button 

submit_btn = Button(root, text = "Add record to Database", command = submit)
submit_btn.grid(row= 6, column= 0, columnspan= 2, pady= 10, padx= 10, ipadx= 100)

# Create a Query Button

query_btn = Button(root, text= "Show Records", command= query)
query_btn.grid(row= 7, column= 0, columnspan= 2, pady= 10, padx= 10, ipadx= 126)

#Create a Delete Button

delete_btn = Button(root, text= "Delete Record", command= delete)
delete_btn.grid(row= 9, column= 0, columnspan= 2, pady= 10, padx= 10, ipadx= 126)

#Create a Delete Button

update_btn = Button(root, text= "Edit Record", command= update)
update_btn.grid(row= 11, column= 0, columnspan= 2, pady= 10, padx= 10, ipadx= 126)

root.mainloop()