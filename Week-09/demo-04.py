import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="images/python-powered-h-70x91.png")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w = tk.Label(root,
             justify=tk.LEFT,
             compound=tk.LEFT,
             padx=10,
             text=explanation,
             image=logo).pack(side="right")

root.mainloop()
