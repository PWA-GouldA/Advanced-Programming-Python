#!/usr/bin/python3
# write tkinter as Tkinter to be Python 2.x compatible
from tkinter import *
def button1(event):
    print("Single Click, Button-l")
def button2(event):
    print("Single Click, Button-2")
def button3(event):
    print("Single Click, Button-3")
def quit(event):
    print("Double Click, so let's stop")
    import sys; sys.exit()

widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', button1)
widget.bind('<Button-2>', button2)
widget.bind('<Button-3>', button3)
widget.bind('<Double-1>', quit)
widget.mainloop()