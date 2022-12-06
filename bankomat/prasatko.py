
from bankomat import Bankomat
from os.path import basename, splitext
import tkinter as tk
from PIL import Image, ImageTk


# from tkinter import ttk


class Application(tk.Tk):
    name = "Prasátko"

    def __init__(self):
        super().__init__(className=self.name)

        self.bankomat = Bankomat('trezor.txt')

        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Prasátko")
        self.lbl.pack()

        self.Cislo = tk.IntVar(self, 0, "Cislo")

        self.entry = tk.Entry(self, textvariable=self.Cislo)
        self.entry.bind('<Return>', self.make)
        self.entry.pack()
      
      
        self.message = tk.Message(self, text="start", width=300)
        self.message.pack()



    def make(self, event):
        self.bankomat.read()
        number = self.Cislo.get()
        vysledek = self.bankomat.make(number)
        self.bankomat.write()
        self.message.config(text=vysledek)

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
