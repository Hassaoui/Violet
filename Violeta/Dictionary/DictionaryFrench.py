import random
from Dictionary import DictSquel


class FrenchDict(DictSquel.dictSquel):

#app mesages
    def commandMessage(self):
        choice = ["\nQuelle action voulez-vous effectuer? (QuoiFaire Sujet)\n"]
        return random.choice(choice)

#AppCommand messages
    def chargeFiles(self):
        choice = ["Voulez-vous charger les fichiers?\n"]
        return random.choice(choice)

    def workingOnIt(self):
        choice = ["\nChargement...\n"]
        return random.choice(choice)

    def appNotFound(self, notFoundAppli):
        choice = ["\nl'application " + notFoundAppli + " n'a pas été trouvé\n"]
        return random.choice(choice)

    def whichAppOpen(self):
        choice = ["Quelle application voulez-vous ouvrir?\n"]
        return random.choice(choice)

    def appNotSetUpYet(self):
        choice = ["l'application n'a pas encore été initiée:))\n"]
        return random.choice(choice)

#NoCommand messages
    def commandNotFound(self):
        choice = ["la commande n'a pas été trouvée\n"]
        return random.choice(choice)

#StrmCommand messages
    def optionNotNull(self, i, name):
        return "[" + str(i) + "]  " + str(name) + ""

    def optionNull(self, i):
        return "[" + str(i) + "]  Aucun \n"

    def whichMovie(self):
        choice = ["\nLequel voulez-vous? \n"]
        return random.choice(choice)

    def ErrorInput(self, numOption, numsugges):
        choice = ["Dois être un chiffre \n",
                  "Dois être un chiffre entre 0 et " + str(numsugges) + "\n"]
        return choice[numOption]

    def nothingOpen(self):
        choice = ["Rien ne va être ouvert\n"]
        return random.choice(choice)

    def openingMovie(self, nameMovie):
        return "Ouverture de " + nameMovie

#ledCommand messages
    def ledNotFound(self):
        choice = ["LED introuvable\n"]
        return random.choice(choice)


#LoadCommand messages
    def CantLoad(self):
        choice = ["Impossible de charger\n"]
        return random.choice(choice)

    def choichesLoadMovie(self):
        choices = ['films']
        return choices

    def choichesLoadApp(self):
        choices = ['app']
        return choices

    def sureWannaLoad(self, option):
        choice = ['Vous êtes sûr de vouloir charger tous les ' + str(option) + '?\n']
        return random.choice(choice)
#General messages
    def actionFinish(self):
        choice = ["\nFini!!\n"]
        return random.choice(choice)

    def VocalCommands(self):
        commands = {'ouvre' : 'open',
                    'adresse' : 'map',
                    'cherche' : 'search',
                    'recherche' : 'search',
                    'youtube' : 'yt',
                    'image' : 'img',
                    'video' : 'vid',
                    'film' : 'strm',
                    'amusement' : 'fun',
                    'charge' : 'load',
                    'lumière' : 'led'}
        return commands