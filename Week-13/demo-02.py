# Connect to a web site and accept the content

import socket
import time
import threading
from queue import Queue
from tkinter import *


# main window
# input:    server name
# input:    start port
# input:    end port
# input:    number threads

# output:   number running threads
# output:   graph of completed scans?
# output:   list of open ports
# output:   pixel-chart of running, open and 'closed' ports

def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

class PortScannerInputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Host:").grid(row=0)
        tk.Entry(self).grid(row=0, column=1, columnspan=2)
        tk.Label(self, text="Start Port:").grid(row=1)
        tk.Entry(self).grid(row=1, column=1, columnspan=2)
        tk.Label(self, text="End Port:").grid(row=2)
        tk.Entry(self).grid(row=2, column=1, columnspan=2)
        tk.Label(self, text="Threads:").grid(row=2)
        tk.Entry(self).grid(row=3, column=1, columnspan=2)
        tk.Label(self, text=" ").grid(row=4, columnspan=2)
        tk.Label(self, text=" ").grid(row=6, columnspan=2)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Port Scanner")

        root_menu = tk.Menu(self)
        self.config(menu=root_menu)

        # creating sub menus in the root menu
        file_menu = tk.Menu(root_menu)
        root_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New file.....", command=self.function)
        file_menu.add_command(label="Open files", command=self.function)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # creating another sub menu
        edit_menu = tk.Menu(root_menu)
        root_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.function)
        edit_menu.add_command(label="Redo", command=self.function)

        self.frame_a = PortScannerInputFrame(self)

        tk.Button(self, text="Start", command=self.start_scan).grid(row=5, column=1)
        tk.Button(self, text="Stop", command=self.end_scan).grid(row=5, column=2)

    def start_scan(self):
        tk.Label(self, text="Start").grid(row=7, column=0)

    def end_scan(self):
        tk.Label(self, text="Stop").grid(row=7, column=0)

    def function(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
