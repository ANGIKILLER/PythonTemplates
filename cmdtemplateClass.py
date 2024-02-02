import os, getpass, platform
from threading import Thread


class Terminal:
    def __init__(self):
        # Ext Vars
        self.example = "This is an Example"
        self.example_list = [1, 2, "Example"]

        # Sys vars
        self.running = True
        self.user = getpass.getuser()
        self.startbar = f"Terminal Template by 👾@angikiller - 2024"
        self.pointer = f"\n{self.user} --> "
        self.cin : str
        self.args : list
        self.command : str


    def _clear(self):
        os.system("clear")
        print(f"{self.startbar}")
        

    def run(self):
        self._clear()
        while self.running: self._input()


    def _input(self) -> None:
        self.cin = input(self.pointer)
        self.command = self.cin.split(" ", 1)[0].lower()
        try:
            self.full_args = self.cin.split(" ", 1)[1]
            self.args = self.cin.split(" ")[1:]
        except: 
            self.args, self.full_args = None, None
        self._process()


    def _process(self):
        if self.command in ["help"]:
            print("Non ci sono troppi comandi per adesso")

        elif self.command in ["os"]:
           print(platform.system())

        elif self.command in ["test"]:
            None

        else:
            print("Nessun comando oppure non valido")




t = Terminal()
t.run()
