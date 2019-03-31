from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Jeff's Calculator")

        self.menu_button = Button(master, text="Menu", command=self.menu)
        self.menu_button.grid(column=0, row=0)

        self.history_button = Button(master, text="History", command=self.show_history)
        self.history_button.grid(column=3, row=0, sticky=E)

        self.equation_label = Label(master, text="equation input will be here")
        self.equation_label.grid(column=3, row=1, sticky=E)

        # most recent string of chars entered go here until an operator has been selected.
        self.user_input_label = Label(master, text="user input here")
        self.user_input_label.grid(column=3, row=2, sticky=E)

        self.seven_button = Button(master, text="7")
        self.history_button.grid(column=0, row=3)

        self.eight_button = Button(master, text="8")
        self.history_button.grid(column=1, row=3)

        self.nine_button = Button(master, text="9")
        self.history_button.grid(column=2, row=3)

        self.multiply_button = Button(master, text="*")
        self.history_button.grid(column=3, row=3)

    def menu(self):
        pass

    def show_history(self):
        pass


root = Tk()
calculator_gui = Calculator(root)
root.mainloop()
