import os, getpass, platform
from threading import Thread


class Terminal:
    def __init__(self):
        self.running = True
        self.user = getpass.getuser()
        self.pointer = f"\n{self.user} --> "
        self.cin : str
        self.args : list
        self.command : str
        
    def run(self):
        print("Terminal Template - 2022")
        while self.running: self._input()

    def _input(self) -> None:
        self.cin = input(self.pointer)
        self.args = self.cin.split(" ")[1:]
        self.cont = self.cin.split(" ", 1)[1:]
        self.command = self.cin.split(" ")[0]
        self._process()

    def _process(self):
        if self.command == "help":
            print("Non ci sono troppi comandi per adesso")

        elif self.command == "os":
           print(platform.system())

        elif self.command == "":
            None

        else:
            print("Nessun comando oppure non valido")


t = Terminal()
t.run()
