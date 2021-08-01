from Commands import Command

class noCommand(Command.command):

    def execute(self):
        self.main.writeErrorLog(self.dictionnary.commandNotFound())

    def getCommand(self):
        return self.command

    def __init__(self, main, comm, dict):
        self.command = comm
        self.main = main
        self.dictionnary = dict