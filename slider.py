#Done by Carlos Amaral (13/08/2020)

# Tutorial 9 - Sliders

from tkinter import *

root = Tk()
root.title('My sliders')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()


my_btn = Button(root, text="Click Me!", command=slide).pack()


root.mainloop()
