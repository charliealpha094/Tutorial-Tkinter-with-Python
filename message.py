#Done by Carlos Amaral (12/08/2020)

# Tutorial 8 - Message Boxes

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message Boxes')

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked Yes!!").pack()
    else:
        Label(root, text="You clicked No!!").pack()


Button(root, text="Popup", command=popup).pack()






root.mainloop()