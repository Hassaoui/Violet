from abc import ABC, abstractmethod

class dictSquel(ABC):

#app mesages
    @abstractmethod
    def commandMessage(self):
        pass

#AppCommand messages
    @abstractmethod
    def chargeFiles(self):
        pass

    @abstractmethod
    def workingOnIt(self):
        pass

    @abstractmethod
    def appNotFound(self, notFoundAppli):
        pass

    @abstractmethod
    def whichAppOpen(self):
        pass

    @abstractmethod
    def appNotSetUpYet(self):
        pass

#NoCommand messages
    @abstractmethod
    def commandNotFound(self):
        pass

#StrmCommand messages
    @abstractmethod
    def optionNotNull(self, i, name):
        pass

    @abstractmethod
    def optionNull(self, i):
        pass

    @abstractmethod
    def whichMovie(self):
        pass

    @abstractmethod
    def ErrorInput(self, numOption, numsugges):
        pass

    @abstractmethod
    def nothingOpen(self):
        pass

    @abstractmethod
    def openingMovie(self, nameMovie):
        pass

#LedCommand messages
    @abstractmethod
    def ledNotFound(self):
        pass


#LoadCommand messages
    @abstractmethod
    def CantLoad(self):
        pass

    @abstractmethod
    def choichesLoadMovie(self):
        pass

    @abstractmethod
    def choichesLoadApp(self):
        pass

    @abstractmethod
    def sureWannaLoad(self):
        pass

#General messages
    @abstractmethod
    def actionFinish(self):
        pass

    @abstractmethod
    def VocalCommands(self):
        pass

