from tkinter import *

canvas_width = 190
canvas_height = 150

master = Tk()
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()


def circle(canvas, x, y, r):
    id = canvas.create_oval(x - r, y - r, x + r, y + r)
    return id


circle(w, 20, 50, 30)
circle(w, 60, 30, 50)
circle(w, 50, 50, 70)

mainloop()
