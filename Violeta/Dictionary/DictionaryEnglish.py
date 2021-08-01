import random
from Dictionary import DictSquel

class EnglishDict(DictSquel.dictSquel):

#app mesages
    def commandMessage(self):
        choice = ["\nWhat do you wanna do? (whatToDo subject)\n"]
        return random.choice(choice)

#AppCommand messages
    def chargeFiles(self):
        choice = ["Charge all the files?\n"]
        return random.choice(choice)

    def workingOnIt(self):
        choice = ["\nworking on it...\n"]
        return random.choice(choice)

    def appNotFound(self, notFoundAppli):
        choice = ["\nApp " + notFoundAppli + " not found\n"]
        return random.choice(choice)

    def whichAppOpen(self):
        choice = ["Which app do you wanna open?\n"]
        return random.choice(choice)

    def appNotSetUpYet(self):
        choice = ["The application has not been set up:))\n"]
        return random.choice(choice)

#NoCommand messages
    def commandNotFound(self):
        choice = ["Command Not Found\n"]
        return random.choice(choice)

#StrmCommand messages
    def optionNotNull(self, i, name):
        return "[" + str(i) + "]  " + str(name) + ""

    def optionNull(self, i):
        return "[" + str(i) + "]  None \n"

    def whichMovie(self):
        choice = ["\nWhich one do you want? \n"]
        return random.choice(choice)

    def ErrorInput(self, numOption, numsugges):
        choice = ["Must Be a Number \n",
                  "Must Be a Number Between 0 And " + str(numsugges) + "\n"]
        return choice[numOption]

    def nothingOpen(self):
        choice = ["Opening Nothing\n"]
        return random.choice(choice)

    def openingMovie(self, nameMovie):
        return "Opening " + nameMovie

#ledCommand messages
    def ledNotFound(self):
        choice = ["LED Not Found\n"]
        return random.choice(choice)

#LoadCommand messages
    def CantLoad(self):
        choice = ["Can't load that option\n"]
        return random.choice(choice)

    def choichesLoadMovie(self):
        choices = ['movies']
        return choices

    def choichesLoadApp(self):
        choices = ['app']
        return choices

    def sureWannaLoad(self, option):
        choice = ['Are you sure you wanna load all the ' + str(option) + '?\n']
        return random.choice(choice)

#General messages
    def actionFinish(self):
        choice = ["\nDone!!\n"]
        return random.choice(choice)

    def VocalCommands(self):
        commands = {'open' : 'open',
                    'place' : 'map',
                    'search' : 'search',
                    'YouTube' : 'yt',
                    'image' : 'img',
                    'video' : 'vid',
                    'movie' : 'strm',
                    'fun' : 'fun',
                    'load' : 'load',
                    'light' : 'led'}
        return commands