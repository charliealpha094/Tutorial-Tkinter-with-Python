#Done by Carlos Amaral (11/08/2020)

# Tutorial 4 - Creating an input box

from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name:")  # A text inside the input box.


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Click here!", command=myClick)
myButton.pack()


root.mainloop()