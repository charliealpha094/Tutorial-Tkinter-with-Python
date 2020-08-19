#Done by Carlos Amaral (13/08/2020)

# Tutorial 11 - Dropdown Menus

from tkinter import *

root = Tk()
root.title('Dropdown Menus')
root.geometry("400x400")

# Drop Down Boxes

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]





clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()


myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
