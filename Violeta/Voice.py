import speech_recognition as sr
import threading
import time
from datetime import datetime
from Dictionary import DictionaryEnglish


class voiceRecognition(object):
    def run(self):
        while True:
            self.recon = sr.Recognizer()
            self.recon.energy_threshold = 1200
            #if microphone not pluged in device_index = 1
            with sr.Microphone(device_index=1) as source:
                self.recon.adjust_for_ambient_noise(source, duration=1)
                audio = self.recon.listen(source)
                #print(source.device_index())
                print(str(datetime.now()) + "  Listening...")
                try:
                    #English
                    #speech = self.recon.recognize_google(audio)
                    #French
                    speech = self.recon.recognize_google(audio, language="fr-CAN")
                    self.makeCommand(speech)
                    self.printConsole(speech)
                    #print(speech)
                except sr.UnknownValueError:
                    print("Wrong stuff Said")
                except sr.RequestError:
                    print("Service down")


    def makeCommand(self, string):
        for s in string.split():
            if s in self.dictionnary.VocalCommands():
                print(string)

    def printConsole(self, string):
        self.app.writeTextCommandWindow(string + "\n")
        if 'okay' in string or 'ok' in string:
            self.app.writeTextCommandWindow(string + "\n")

    def __init__(self, app, dict):
        self.app = app
        self.dictionnary = dict
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

