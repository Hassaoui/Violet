from Commands import Command
import OpenApp
import NetResearch
from Dictionary import DictionaryGeneral

class loadCommand(Command.command):

    def execute(self):
        if self.numCallBack == 0:
            self.main.waitForInput()
            self.main.writeLog(self.dictionnary.sureWannaLoad(self.command[0]))

        if self.numCallBack == 1:
            if self.newinput in DictionaryGeneral.wordsToYes():
                for s in self.command:
                    if s in self.dictionnary.choichesLoadMovie():
                        self.main.writeLog("chargin Movies \n")
                        #self.chargeMovies()
                    elif s in self.dictionnary.choichesLoadApp():
                        #NetResearch.LoadMovieStream()
                        self.main.writeLog("chargin App \n")
                    else:
                        self.main.writeError(self.dictionnary.CantLoad())
            self.main.stopWaiting()

    def chargeMovies(self):
        self.main.writeLog(self.dictionnary.workingOnIt())
        appnotFound = OpenApp.lookForApplication()
        for notFoundAppli in appnotFound:
            self.main.writeLog(self.dictionnary.appNotFound(notFoundAppli))
        self.main.writeLog(self.dictionnary.actionFinish())

    def newInput(self, text):
        self.newinput = text
        self.numCallBack = self.numCallBack + 1
        self.execute()

    def getCommand(self):
        return self.command

    def __init__(self, main, comm, dict):
        self.numCallBack = 0
        self.command = comm
        self.main = main
        self.dictionnary = dict