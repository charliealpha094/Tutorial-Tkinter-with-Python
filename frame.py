#Done by Carlos Amaral (12/08/2020)

#Tutorial 6 - Adding a frame to programs

from tkinter import *


root = Tk()
root.title('Adding a frame')

frame = LabelFrame(root, text="This is my frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here!")
b2 = Button(frame, text="...or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)



root.mainloop()
