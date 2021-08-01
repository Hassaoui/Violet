from Commands import Command
import NetResearch

class vidCommand(Command.command):

    def execute(self):
        NetResearch.vidSearch(self.command)

    def getCommand(self):
        return self.command

    def __init__(self, main, comm):
        self.command = comm
        self.main = main