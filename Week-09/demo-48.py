from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()

w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=X)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=X, padx=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X, pady=10)
w = Label(root, text="Aqua Ocean", bg="aqua", fg="black")
w.pack(fill=X, ipadx=10)
w = Label(root, text="Yellow Flowers", bg="yellow", fg="black")
w.pack(fill=X, ipady=10)
w = Label(root, text="Filled Window", bg="white", fg="black")
w.pack(fill=X)

mainloop()
