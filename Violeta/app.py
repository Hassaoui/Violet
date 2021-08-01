import threading
import tkinter as tk
from tkinter import *
import LeaMain
from Dictionary import DictionaryEnglish, DictionaryFrench
import Voice


class appli:
    def writeTextCommandWindow(self,t):
        self.text.config(state='normal')
        self.text.insert(tk.END, t)
        self.text.see(tk.END)
        self.text.config(state=DISABLED)

    def writeWhatToDO(self):
        self.writeTextCommandWindow(self.dictionnary.commandMessage())

    def program(self, input):
        self.writeTextCommandWindow(input.get()  + "\n")
        if self.waitInput == False:
            self.main.mainPorg(input.get())
            if self.waitInput == False:
                self.writeWhatToDO()
        else:
            self.main.newInput(input.get())
        input.delete(0, END)

    def WriteErrorCmdWindow(self, t):
        self.text.tag_config("color", foreground = "red")
        self.text.config(state='normal')
        self.text.insert(tk.END, t)
        line, column = self.text.index('end').split('.')
        s = int(line) - 2
        self.text.tag_add("color", '{}.{}'.format(s, 0), '{}.{}'.format(s,len(t)))
        self.text.see(tk.END)
        self.text.config(state=DISABLED)

    def waitForInput(self):
        self.waitInput = True

    def stopWainting(self):
        self.waitInput = False
        self.writeWhatToDO()

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x200")
        self.root.title("AppLea")
        self.text = tk.Text(self.root, width=61, height=10)
        self.text.pack()
        self.text.config(state=DISABLED)
        inputfield = Entry(self.root, width=55)
        inputfield.pack()

        self.dictionnary = DictionaryEnglish.EnglishDict()

        self.main = LeaMain.leaMain(self, self.dictionnary)
        inputfield.bind('<Return>', lambda _: self.program(inputfield))
        self.writeTextCommandWindow(self.dictionnary.commandMessage())
        self.waitInput = False
        voice = Voice.voiceRecognition(self, self.dictionnary)


        self.root.mainloop()
