from Commands import Command
import OpenApp
import time
from Dictionary import DictionaryGeneral

class appCommand(Command.command):
    def execute(self):
        ApplicationOuvrable = DictionaryGeneral.nomApps()
        newinput = ""
        for s in self.command:
            print(s)
            newinput = newinput + str(s) + " "
        newinput = newinput[:-1]
        if newinput.lower() not in ApplicationOuvrable:
            self.main.writeError(self.dictionnary.appNotSetUpYet())
        else:
            OpenApp.openApp(ApplicationOuvrable.get(newinput.lower()))
            self.main.writeLog(ApplicationOuvrable.get(newinput.lower()) + "\n")

    def newInput(self, text):
        self.newinput = text
        self.numCallBack = self.numCallBack + 1
        self.execute()

    def getCommand(self):
        return self.command

    def __init__(self, main, comm, dict):
        self.command = comm
        self.main = main
        self.numCallBack = 0
        self.newinput = ""
        self.dictionnary = dict