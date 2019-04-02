from tkinter import *

master = Tk()

genderM = IntVar()
Checkbutton(master, text="male", variable=genderM).grid(row=0, sticky=W)

genderF = IntVar()
Checkbutton(master, text="female", variable=genderF).grid(row=1, sticky=W)

genderX = IntVar()
Checkbutton(master, text="other", variable=genderX).grid(row=2, sticky=W)

mainloop()
