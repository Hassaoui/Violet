import os
import subprocess


def lookForApplication():
    pathFiles = ["C:\Program Files",
                 "C:\Program Files (x86)",
                 "D:\Program Files",
                 "D:\Program Files (x86)",
                 "D:\league"]

    #path of the application that are gonna be in the text file
    pathName = []
    #nom des applications dans le fichier texte
    _nomAppli = []
    nameFile = []
    #Rempli un tableau avec le nom des applications avec .exe
    with open("TextFiles/ApplicationsOuvrable.txt", "r") as file:
        i = 0
        for line in file:
            _nomAppli.append(line.strip() + ".exe")

    #Loop to find certain application in windows/system32
    for nom in _nomAppli:
        try:
            string = where(nom)[0]
            if string != "":
                pathName.append(where(nom)[0])
                _nomAppli.remove(nom)
        except IndexError as error:
            pathName = pathName

    #Loop only for Users directory bcs doesnt wanna be in array
    for root, dirs, files in os.walk(r'C:\Users'):
        for file in files:
            if file in _nomAppli:
                pathName.append(os.path.join(root, file))
                _nomAppli.remove(file)
                nameFile.append(file)

    #Loop for normal files
    for path in pathFiles:
        for root, dirs, files in os.walk(r"{}".format(path)):
            for file in files:
                if file in _nomAppli:
                    pathName.append(os.path.join(root, file))
                    _nomAppli.remove(file)
                    nameFile.append(file)

    #Writing to the .txt file
    pathToApplications = open("TextFiles/pathToApplications.txt", "w")
    for path in pathName:
        pathToApplications.write(path + "\n")
    pathToApplications.close()

    return _nomAppli


class CytherError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        self.message = 'CytherError: {}'.format(repr(message))

def where(name, flags=os.F_OK):
    result = []
    extensions = os.environ.get('PATHEXT', '').split(os.pathsep)
    if not extensions:
        raise CytherError("The 'PATHEXT' environment variable doesn't exist")

    paths = os.environ.get('PATH', '').split(os.pathsep)
    if not paths:
        raise CytherError("The 'PATH' environment variable doesn't exist")

    for path in paths:
        path = os.path.join(path, name)
        if os.access(path, flags):
            result.append(os.path.normpath(path))
        for ext in extensions:
            whole = path + ext
            if os.access(whole, flags):
                result.append(os.path.normpath(whole))
    return result

def openApp(appName):
    appToOpen = str(appName) + ".exe"
    with open("TextFiles/pathToApplications.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            if appToOpen in stripped_line:
                s = stripped_line
                break

    raw_string = r"{}".format(s)
    subprocess.Popen(raw_string, shell=True)
