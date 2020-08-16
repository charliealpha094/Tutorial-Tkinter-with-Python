#Done by Carlos Amaral (11/08/2020)

# Tutorial 2 - Using Tkinter's Grid System to position our output

from tkinter import *

root = Tk()


# Creating a Label Widget
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="My name is John Elder")

#Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)



root.mainloop()