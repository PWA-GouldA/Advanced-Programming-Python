from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()

w = Label(root, text="red", bg="red", fg="white")
w.pack(padx=5, pady=10, ipadx=5, side=LEFT)
w = Label(root, text="green", bg="green", fg="black")
w.pack(padx=5, pady=20, ipadx=5, side=LEFT)
w = Label(root, text="blue", bg="blue", fg="white")
w.pack(padx=5, pady=20, ipadx=5, side=LEFT)

mainloop()
