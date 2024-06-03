import tkinter as tk
from tkinter import ttk
from tkinter import *

class ButtonWindow(tk.Frame):

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(bd=5, bg="purple") # replace self.bd = 5 and self.bg = "purple"
        self.label = tk.Label(self, text="Question 1\nWhat is the definition of over-consumption?", font=13, fg='white', bg='purple') # quiz question
        self.label.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) # pack the label, otherwise it is not visible

        # creating Tk window TRY ADD IN SAME WINDOW
        master = Tk()

        # creating a Fra, e which can expand according
        # to the size of the window
        pane = Frame(master)
        pane.pack(fill = BOTH, expand = True)

        # button widgets which can also expand and fill
        # in the parent widget entirely
        # Button 1
        b1 = Button(pane, text = "Click me !", 
                    background = "red", fg = "white")
        b1.pack(side = TOP, expand = True, fill = BOTH)

        # Button 2
        b2 = Button(pane, text = "Click me too", 
                    background = "blue", fg = "white")
        b2.pack(side = TOP, expand = True, fill = BOTH)

        # Button 3
        b3 = Button(pane, text = "I'm also button",
                    background = "green", fg = "white")
        b3.pack(side = TOP, expand = True, fill = BOTH)


    def button_fun(self):
        pass


class MainWindow(tk.Frame):

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label = tk.Label(self, text="Overconsumption Quiz!", font=12) # quiz title (always there)
        self.label.pack(pady=10, padx=10)
        self.button_window = ButtonWindow(self) 
        self.button_window.pack()


root = tk.Tk() # create root window explicitly
MainWindow(root).pack()
root.mainloop()