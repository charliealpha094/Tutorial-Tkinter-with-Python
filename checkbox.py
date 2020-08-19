#Done by Carlos Amaral (13/08/2020)

# Tutorial 10 - Checkboxes

from tkinter import *

root = Tk()
root.title('Checkboxes')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()



var = StringVar()

c = Checkbutton(root, text="Check this box, it's an order!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


myButton = Button(root, text="Show selection", command=show).pack()



root.mainloop()

