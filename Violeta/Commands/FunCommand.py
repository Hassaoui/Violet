from Commands import Command
import FunFeature

class funCommand(Command.command):

    def execute(self):
        FunFeature.Donut()

    def getCommand(self):
        return self.command

    def __init__(self, main, comm):
        self.command = comm
        self.main = main