from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("My Image Viewer")
#root.iconbitmap("logo.png")

my_img = ImageTk.PhotoImage(Image.open("jawid illustration.jpg"))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()