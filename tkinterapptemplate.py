from tkinter import *
from threading import Thread

#------------------------------------------------------------------------


class App:
    def __init__(self):
        self.win = Tk()
        self.geometry:list
        self.title:str
        self.resizable:list

    def update(self):
        self.win.title(self.title)
        self.win.geometry(f"{self.geometry[0]}x{self.geometry[1]}")
        self.win.resizable(self.resizable[0], self.resizable[1])

    def start(self):
        self.win.mainloop()


#------------------------------------------------------------------------


class StartPage:
    def __init__(self):
        self.frame = Frame()
        
    def content(self):
        
        # ----------------
        None
        # ----------------

    def create(self):
        self.content()
        self.frame.pack()

    def remove(self):
        self.frame.destroy()


#------------------------------------------------------------------------


def Runner():
    w = App()
    w.geometry = (500, 250)
    w.title = "TestApp"
    w.resizable = (0, 0)

    StartPage().create()

    w.update()
    w.start()


Runner()