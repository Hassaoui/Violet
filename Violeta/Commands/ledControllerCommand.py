from Commands import Command
import ledController

class ledControllerCommand(Command.command):

    def execute(self):
        print("here")

    def getCommand(self):
        return self.command

    def __init__(self, main, comm, dict):
        self.command = comm
        self.main = main
        self.dictionary = dict