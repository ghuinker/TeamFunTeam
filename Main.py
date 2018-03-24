from tkinter import *

master = Tk()
master.geometry("750x600")


# Code to add widgets will go here...
def test_go():
    print("TestGo")


testText = Text(master, width=45)
testButton = Button(master, text="Go", command=test_go)
testResult = Label(master, text="ResultsGoHere")

trainURL = Text(master, width=30, height=1)
consCheck = Checkbutton(master, text="Conservative")
libCheck = Checkbutton(master, text="Liberal")
trainResult = Text(master, width=45)


def train_go():
    print("Train Go")


trainButton = Button(master, text="Go", command=train_go)

Label(master, text="Test").grid(row=0)
testText.grid(row=4, column=0)
testButton.grid(row=5, column=0)
testResult.grid(row=6, column=0)

Label(master, text="Train URL").grid(row=0, column=1)
trainURL.grid(row=1, column=1, sticky=N)
consCheck.grid(row=2, column=1, sticky=W)
libCheck.grid(row=2, column=1, sticky=E)
trainButton.grid(row=3, column=1, sticky=N)
trainResult.grid(row=4, column=1)

master.mainloop()
