from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images Viewer Tutorial")
root.iconbitmap("Tkinter/Image viewer/images/logo.ico")

my_img1 = ImageTk.PhotoImage(Image.open("Tkinter\Image viewer\images\Ferrari.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Tkinter\Image viewer\images\mclaren.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Tkinter\Image viewer\images\Mercedes.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Tkinter\Image viewer\images\Toyota.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4]

mylabel = Label(image= my_img1)
mylabel.grid(row=0, column=0, columnspan=3)

def forward(image_number):

    global mylabel
    global button_forward
    global button_Back

    mylabel.grid_forget()
    mylabel = Label(image=image_list[image_number-1])
    button_forward = Button(root, text = ">>", command=lambda: forward(image_number+1))
    button_Back = Button(root, text = "<<", command=lambda: back(image_number-1))

    if image_number == len(image_list):
        button_forward = Button(root, text = ">>", state= DISABLED)

    mylabel.grid(row=0, column=0, columnspan=3)
    button_Back.grid(row= 1, column=0)    
    button_forward.grid(row= 1, column=2)



def back(image_number):
    global mylabel
    global button_forward
    global button_Back

    mylabel.grid_forget() # Elimina la imagen anterior para que se pueda mostra la nueva imagen sin sobreponerse 
    mylabel = Label(image=image_list[image_number-1])
    button_forward = Button(root, text = ">>", command=lambda: forward(image_number+1))
    button_Back = Button(root, text = "<<", command=lambda: back(image_number-1))

    if image_number == 0:
        button_Back = Button(root, text = "<<", state= DISABLED)

    mylabel.grid(row=0, column=0, columnspan=3)
    button_Back.grid(row= 1, column=0)    
    button_forward.grid(row= 1, column=2)

button_Back = Button(root, text= "<<", command= back).grid(row= 1, column=0)
button_exit = Button(root, text= "Exit", command= root.quit).grid(row= 1, column=1)# root.quit cerrara el programa al momento de presionar el boton
button_forward = Button(root, text = ">>", command=lambda: forward(2)).grid(row= 1, column=2)

root.mainloop()

