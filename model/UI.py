from tkinter import *
from tkinter import ttk

root = ttk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello world").grid(column=0, row=0)
ttk.Button(frm, text="quit", command=root.destroy).grid(column=0, row=0)
root.mainloop()

class SelftrackUI:
    root: ttk
    frm: ttk

    def __init__(self) -> None:
        self.root = ttk()
        self.frm = ttk.Frame(root, padding=10)

    def start(self):
        ttk.Label(self.frm, text="Hello world").grid(column=0, row=0)
        ttk.Button(self.frm, text="quit", command=root.destroy).grid(column=0, row=0)
        self.root.mainloop()