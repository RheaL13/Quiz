import tkinter as tk
from tkinter import *

# window = tk.Tk()
# label = tk.Label(text="Overconsumption!")
# label.pack()

# master = Tk()
# var1 = IntVar()
# root = Tk()
# w = Label(root, text='What is the definition of over-consumption?')
# w.pack()
# Checkbutton(master, text='answer 1', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text='answer 2', variable=var2).grid(row=1, sticky=W)
# var3 = IntVar()
# Checkbutton(master, text='answer 3', variable=var3).grid(row=2, sticky=W)
# var4 = IntVar()
# Checkbutton(master, text='answer 4', variable=var4).grid(row=3, sticky=W)
# mainloop()

class ButtonWindow(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(bd=5, bg="purple") # replace self.bd = 5 and self.bg = "purple"
        self.label = tk.Label(self, text="Question 1\nWhat is the definition of over-consumption?", font=13, fg='white', bg='purple') # quiz question
        self.label.pack() # pack the label, otherwise it is not visible


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