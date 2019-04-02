from tkinter import *

colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

r = 0
for c in colours:
    # relief: flat, groove, raised, ridge, solid, or sunken
    Label(text=c, relief=FLAT, width=15).grid(row=r, column=0)
    Entry(bg=c, relief=GROOVE, width=10).grid(row=r, column=1)
    r = r + 1

mainloop()
