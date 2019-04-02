from tkinter import *

master = Tk()

def var_states():
   print("male: %d,\nfemale: %d,\nother: %d" % (genderM.get(), genderF.get(), genderX.get()))

Label(master, text="Your sex:").grid(row=0, sticky=W)

genderM = IntVar()
Checkbutton(master, text="male", variable=genderM).grid(row=1, sticky=W)

genderF = IntVar()
Checkbutton(master, text="female", variable=genderF).grid(row=2, sticky=W)

genderX = IntVar()
Checkbutton(master, text="other", variable=genderX).grid(row=3, sticky=W)

Button(master, text='Quit', command=master.quit).grid(row=5, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=6, sticky=W, pady=4)

mainloop()
