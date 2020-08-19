#Done by Carlos Amaral (12/08/2020)

#Tutorial 7 - Create Radio Buttons

from tkinter import *

root = Tk()
root.title('Radio Buttons')



TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),

]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()



myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()
mainloop()


root.mainloop()