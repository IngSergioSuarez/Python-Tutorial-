from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images Viewer Tutorial")
root.iconbitmap("Tkinter/Image viewer/images/29152.ico")

my_img1 = ImageTk.PhotoImage(Image.open("Tkinter/Image viewer/images/Ferrari.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Tkinter/Image viewer/images/mcclaren.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Tkinter/Image viewer/images/Mercedes.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Tkinter/Image viewer/images/Toyota.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4]

mylabel = Label(image= my_img1).grid(row=0, column=0, columnspan=3)

root.mainloop()

