from Commands import Command
import LEDcontrol

class ledCommand(Command.command):

    def execute(self):
        try:
            LEDcontrol.ledControl(self.open)
        except:
            self.main.writeError(self.dictionary.ledNotFound())

    def getCommand(self):
        return self.command

    def __init__(self, main, comm, open, dict):
        self.command = comm
        self.main = main
        self.open = open
        self.dictionary = dict