#Done by Carlos Amaral (11/08/2020)

# Tutorial 1 - Simple GUI (Graphical user interface) "hello_world" label using tkinter

from tkinter import *

root = Tk()


# Creating a Label Widget
myLabel = Label(root, text="Hello World!")
# Shoving it onto the screen
myLabel.pack()


root.mainloop()