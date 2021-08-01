
from Dictionary import DictionaryGeneral
from Commands import NoCommand, MapCommand, AppCommand, SearchCommand, ImgCommand, VidCommand, YtCommand, StrmCommand, FunCommand, LoadCommand, LedCommand, ledControllerCommand

class leaMain:


    def writeErrorLog(self, text):
        self.app.WriteErrorCmdWindow(text)


    def mainPorg(self, input):
        result = input.split()
        typeCommand = result.pop(0)

        wordsToQuit = DictionaryGeneral.wordsToQuit()
        if typeCommand in wordsToQuit:
            return

        if typeCommand == 'open':
            self.command = AppCommand.appCommand(self, result, self.dictionnary)

        elif typeCommand == 'map':
            self.command = MapCommand.mapCommand(self, result)

        elif typeCommand == 'search':
            self.command = SearchCommand.searchCommand(self, result)

        elif typeCommand == 'img':
            self.command = ImgCommand.imgCommand(self, result)

        elif typeCommand == 'vid':
            self.command = VidCommand.vidCommand(self, result)

        elif typeCommand == 'yt':
            self.command = YtCommand.ytCommand(self, result)

        elif typeCommand == 'strm':
            self.command = StrmCommand.strmCommand(self, result, self.dictionnary)

        elif typeCommand == 'fun':
            self.command = FunCommand.funCommand(self, result)

        elif typeCommand == 'load':
            self.command = LoadCommand.loadCommand(self, result, self.dictionnary)

        elif typeCommand == 'led':
            self.command = LedCommand.ledCommand(self, result, self.open, self.dictionnary)
            if self.open:
                self.open = False
            else:
                self.open = True

        elif typeCommand == 'ledco':
            self.command = ledControllerCommand.ledControllerCommand(self, result, self.dictionnary)

        self.command.execute()

    def writeLog(self, text):
        self.app.writeTextCommandWindow(text)

    def writeError(self, text):
        self.app.WriteErrorCmdWindow(text)

    def waitForInput(self):
        self.app.waitForInput()

    def stopWaiting(self):
        self.app.stopWainting()

    def newInput(self, text):
        self.command.newInput(text)

    def __init__(self, appli, dictionnary):
        self.open = False
        self.app = appli
        self.dictionnary = dictionnary
        self.command = NoCommand.noCommand(self, "nothing", self.dictionnary)