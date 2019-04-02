import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5),
    ("PHP", 6),
    ("Ruby", 7),
    ("Go", 8),
    ("C#", 9)
]


def ShowChoice():
    print(v.get())


tk.Label(root,
         text="""Choose your favourite programming language:""",
         justify=tk.LEFT,
         padx=20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root,
                   text=language,
                   indicatoron=0,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
