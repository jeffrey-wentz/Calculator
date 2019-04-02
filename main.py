from tkinter import *


class Calculator:
    def user_action(self):
        print(self.user_input)

    def __init__(self, master):
        # Constructor method
        master.title('Calculator')
        self.user_input = ""
        self.entry = Entry(master)
        self.entry.grid(row=0, column=0, columnspan=6, pady=3)
        self.user_input += self.entry.get()
        Label(master, text=self.user_input).grid(row=0, column=4, columnspan=2)
        Button(master, text="print", width=10, command=self.user_action()).grid(row=4, column=4, columnspan=2)


root = Tk()
obj = Calculator(root)
root.mainloop()
