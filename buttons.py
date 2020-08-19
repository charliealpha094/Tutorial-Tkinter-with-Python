#Done by Carlos Amaral (11/08/2020)

# Tutorial 3 - Creating buttons

from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()



myButton = Button(root, text="Click Me!", command=myClick, fg="blue")
myButton.pack()


root.mainloop()