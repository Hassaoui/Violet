from tkinter import *
from tkinter import colorchooser
import LEDcontrol

class ledController():


    def FrameStripMaker(self):

        effectName = Label(self.GraphicFrame, text = "Effect:")
            #DropDownList
        self.effectClick = StringVar()
        self.effectClick.set(self.schemeAction[0])
        strips = OptionMenu(self.GraphicFrame, self.effectClick, *self.schemeAction)
            #
        myButton = Button(self.GraphicFrame, text = "OK",  command=self.makeColorChooser)
        closeButton = Button(self.GraphicFrame, text = "Close",  command=self.closeLED)

        #columnSize
        for col in range(4):
            self.GraphicFrame.grid_columnconfigure(col, minsize=30)

        #UI in frame
        effectName.grid(row = 0, column = 0)
        strips.grid (row=1, column = 0)
        myButton.grid(row = 1, column = 3)
        closeButton.grid(row = 1, column = 4)
        self.GraphicFrame.grid(row = 2, column = 0, columnspan = 5, padx = 12)

    #Pops up the color chooser
    def makeColorChooser(self):
        if(self.effectClick.get() == self.schemeAction[0] or  self.effectClick.get() == self.schemeAction[1]):
            chooseColorStrip = Button(self.GraphicFrame, text = "Choose Color",  command=self.chooseColor)
            chooseColorStrip.grid(row = 2, column = 1)
            self.GraphicFrame.grid_columnconfigure(2, minsize=10)

    #Send data from chooser controller and make the command.
    def chooseColor(self):
        myColor = colorchooser.askcolor()[0]
        stringCommand = self.stripOptionClick.get() + "," + self.effectClick.get() + ","
        for col in myColor:
            stringCommand = stringCommand + str(col) + ","
        stringCommand = stringCommand[:-1]
        LEDcontrol.ledEffects(stringCommand)

    def closeLED(self):
        LEDcontrol.closeLED()

    def __init__(self):
        #variables
        self.root = Tk()
        self.GraphicFrame = LabelFrame(self.root, text = "Color Scheme", )
        self.stripOptions = [
            "Strip1"
        ]
        self.schemeAction = [
            "SolidColor",
            "Rainbow"
        ]

        #General UI
        self.root.geometry("250x300")

        #Creation Items UI
        myLabel = Label(self.root, text = "Strip: ")
            #DropDownList
        self.stripOptionClick = StringVar()
        self.stripOptionClick.set(self.stripOptions[0])
        strips = OptionMenu(self.root, self.stripOptionClick, *self.stripOptions)
            #
        myButton = Button(self.root, text = "OK",  command=self.FrameStripMaker)

        #UI in Root
        myLabel.grid(row = 0, column = 0)
        strips.grid (row=1, column = 0)
        self.root.grid_columnconfigure(2, minsize=70)  # Here
        myButton.grid(row = 1, column = 3)

        #Main Loop
        self.root.mainloop()

ledController()