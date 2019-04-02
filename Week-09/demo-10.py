import tkinter as tk

counter = 0
theText = "abcdefghijklmnopqrstuvwxyz"

def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()


def string_label(label):
    theText = "abcdefghijklmnopqrstuvwxyz"

    def animate():
        global theText
        theText = theText[1::] + theText[0]
        label.config(text=theText)
        label.after(100, animate)

    animate()


root = tk.Tk()
root.title("Counting Seconds")
labelOne = tk.Label(root, fg="dark green")
labelTwo = tk.Label(root, fg="dark blue")
labelOne.pack()
labelTwo.pack()
counter_label(labelOne)
string_label(labelTwo)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
