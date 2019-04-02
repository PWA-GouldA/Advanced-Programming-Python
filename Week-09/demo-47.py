from tkinter import *
from tkinter.colorchooser import askcolor


root = Tk()

Label(root, text="Red Sun", bg="red", fg="white").pack()
Label(root, text="Green Grass", bg="green", fg="black").pack()
Label(root, text="Blue Sky", bg="blue", fg="white").pack()
Label(root, text="Packed Window", bg="white", fg="black").pack()

mainloop()
