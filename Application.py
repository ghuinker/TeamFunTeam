from tkinter import *


class Application(Frame):
    conVar = None
    libVar = None

    def __init__(self, master):
        Frame.__init__(self, master)
        self.conVar = IntVar()
        self.libVar = IntVar()
        self.grid()
        self.create_widgets()



    def create_widgets(self):

        testText = Text(self, width=45)
        testResult = Label(self, text="ResultsGoHere")

        testButton = Button(self, text="Go", command=self.test_go)

        trainURL = Text(self, width=30, height=1)
        consCheck = Checkbutton(self, text="Conservative", variable=self.conVar)
        libCheck = Checkbutton(self, text="Liberal", variable=self.libVar)
        trainResult = Text(self, width=45)

        trainButton = Button(self, text="Go", command=self.train_go)

        Label(self, text="Test").grid(row=0)
        testText.grid(row=4, column=0)
        testButton.grid(row=5, column=0)
        testResult.grid(row=6, column=0)

        Label(self, text="Train URL").grid(row=0, column=1)
        trainURL.grid(row=1, column=1, sticky=N)
        consCheck.grid(row=2, column=1, sticky=W)
        libCheck.grid(row=2, column=1, sticky=E)
        trainButton.grid(row=3, column=1, sticky=N)
        trainResult.grid(row=4, column=1)

    def train_go(self):
        print("TrainGo")
        if(self.conVar.get()):
            print("Conservative")
        if(self.libVar.get()):
            print("Liberal")


    def test_go(self):
        print("Self Go")

root = Tk()
root.title("PolAI")
app = Application(root)
root.mainloop()
