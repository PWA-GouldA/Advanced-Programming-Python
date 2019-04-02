# Install Pillow: pip install pillow
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
logo = tk.PhotoImage(file="images/python-powered-h-70x91.png")

w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(root,
              justify=tk.LEFT,
              padx=10,
              pady=10,
              text=explanation).pack(side="left")
root.mainloop()
