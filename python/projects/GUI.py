from tkinter import Tk, Label, Button
from tkinter import W

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("My new GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.grid(columnspan=2, sticky=W)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=1)

        self.text_button = Button(master, text="text", command=self.text)
        self.text_button.grid(row=2, column=2)

        self.text_button = Button(master, text="this is a button", command=self.text)
        self.text_button.grid()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        print("Go Fuck Yourself!")

    def text(self):
        print("I'm not sure what I can do with this but its pretty cool.")

    def text(self):
        print("this botton should say something different in it")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
