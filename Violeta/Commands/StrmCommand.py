from Commands import Command
import NetResearch

class strmCommand(Command.command):

    def execute(self):
        if self.numCallBack == 0:
            self.main.waitForInput()
            numSuggestion = 5
            LookalikeMin = 40 #in %
            self.suggestion = NetResearch.StreamingSearch(self.command, numSuggestion, LookalikeMin)
            i = 0
            for s in self.suggestion:
                # print(str(s.split(":", 1)[0]) + "  " + str(similar(movieName, s.split(":", 1)[0])))
                self.main.writeLog(self.dictionary.optionNotNull(i, s))
                i = i + 1
            self.main.writeLog(self.dictionary.optionNull(i))
            self.main.writeLog(self.dictionary.whichMovie())
            self.numCallBack = self.numCallBack + 1
            return

        if self.numCallBack == 1:
            if self.RepresentsInt(self.newinput) == False:
                self.main.writeError(self.dictionary.ErrorInput(0, ""))
            elif int(self.newinput) < 0 or int(self.newinput) > len(self.suggestion):
                self.main.writeError(self.dictionary.ErrorInput(1, str(len(self.suggestion))))
            elif int(self.newinput) == len(self.suggestion):
                self.main.writeLog(self.dictionary.nothingOpen())
                self.main.stopWaiting()
            else:
                self.main.writeLog(self.dictionary.openingMovie(self.suggestion[int(self.newinput)]))
                self.main.stopWaiting()

    def RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def getCommand(self):
        return self.command

    def newInput(self, text):
        self.newinput = text
        self.execute()

    def __init__(self, main, comm, dict):
        self.command = comm
        self.main = main
        self.numCallBack = 0
        self.newinput = ""
        self.suggestion = []
        self.dictionary = dict
