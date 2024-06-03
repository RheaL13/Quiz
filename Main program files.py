#import everything from tkinter and import messagebox as mb from tkinter
from tkinter import *
# from tkinter import messagebox as mb
import tkinter as tk
import tkinter
import tkinter as tk
from tkinter import font
from tkinter import *      
from tkinter.ttk import *

# First window
class first:
    firstwindow = tkinter.Tk()
    firstwindow.geometry("1200x750")
    firstwindow.title("Overconsumption Quiz")
	
    class Boldtitle(tk.Label):
        def __init__(self, master = None, **kwargs):
            super().__init__(master, **kwargs)
            bold_font = font.Font(self, self.cget("font"))
            bold_font.configure(weight = "bold")
            self.configure(font = bold_font)

    # title code
    title = Boldtitle(firstwindow, text = "OVERCONSUMPTION QUIZ", \
                      font = ("Helvetica", 40))
    title.pack(pady = 23)

    # login / sign up button 
    login = tk.Button(firstwindow, text = 'LOGIN', width = 10, height = 2,
                   fg = "green", bg = "white", command = firstwindow.destroy) 
    signup = tk.Button(firstwindow, text = 'SIGN UP', width = 10, height = 2,
                    fg = "green", bg = "white", command = firstwindow.destroy) 
    exit = tk.Button(firstwindow, text = 'EXIT', width = 10, height = 2,
                     fg = "white", bg = "black", command = firstwindow.destroy) 

    # Set the position of button on the top of window 
    login.place(x=1000, y=35)
    signup.place(x=1100, y=35) 
    exit.place(x=1100, y=685) 

    # text for the window (stuff about the program)
    title = Boldtitle(firstwindow, text = "Text about program", \
                      font = ("Helvetica", 20))
    title.pack(pady = 50)

    # # side bar
    # class line:
    #     def __init__(self, master = None):
    #         self.master = master

    #         # Calls create method of class GFG
    #         self.create()

    #     def create(self):

    #         # This creates a object of class canvas
    #         self.canvas = Canvas(self.master)

    #         # This creates a line of length 200 (straight horizontal line)
    #         self.canvas.create_line(300, 100, 300, 500)

    #         # This pack the canvas to the main window and make it expandable
    #         self.canvas.pack(fill = BOTH, expand = True)

    # if __name__ == "__main__":

    #     draw = line(firstwindow)

    # buttons for side bar
    homebtn = tk.Button(firstwindow, text = 'LOGIN', width = 10, height = 2,
                   fg = "green", bg = "white", command = firstwindow.destroy) 
    quizbtn = tk.Button(firstwindow, text = 'SIGN UP', width = 10, height = 2,
                    fg = "green", bg = "white", command = firstwindow.destroy) 
    altbtn = tk.Button(firstwindow, text = 'SIGN UP', width = 10, height = 2,
                    fg = "green", bg = "white", command = firstwindow.destroy)
    sucessbtn = tk.Button(firstwindow, text = 'LOGIN', width = 10, height = 2,
                   fg = "green", bg = "white", command = firstwindow.destroy) 
    aboutbtn = tk.Button(firstwindow, text = 'SIGN UP', width = 10, height = 2,
                    fg = "green", bg = "white", command = firstwindow.destroy) 
    helpbtn = tk.Button(firstwindow, text = 'SIGN UP', width = 10, height = 2,
                    fg = "green", bg = "white", command = firstwindow.destroy)

    # Set the position of button on the top of window 
    homebtn.place(x=50, y=50)
    quizbtn.place(x=50, y=150) 
    altbtn.place(x=50, y=250)
    sucessbtn.place(x=50, y=350)
    aboutbtn.place(x=50, y=450) 
    helpbtn.place(x=50, y=550)

    # picture 
    our_canvas=Canvas(firstwindow,width=300,height=200,bg="blue")
    our_canvas.pack()
    
    firstwindow.mainloop()


# # Let's create the Tkinter window
# class signin:
# 	# Let's create the Tkinter window
# 	window = tkinter.Tk()
# 	window.geometry("300x300")
# 	window.title("Signing in")

# 	# You will create two text labels namely 'username' and 'password' and and two input labels for them
# 	tkinter.Label(window, text = "Create an account or sign in:").grid(row = 0)
# 	tkinter.Label(window, text = "Username").grid(row = 1, column = 0) #'username' is placed on position 00 (row - 0 and column - 0)
# 	# 'Entry' class is used to display the input-field for 'username' text label
# 	tkinter.Entry(window).grid(row = 1, column = 0) # first input-field is placed on position 01 (row - 0 and column - 1)
# 	tkinter.Label(window, text = "Password").grid(row = 2, column = 0) #'password' is placed on position 10 (row - 1 and column - 0)
# 	tkinter.Entry(window).grid(row = 2, column = 0) #second input-field is placed on position 11 (row - 1 and column - 1)

# 	tkinter.Label(window, text = "Or are you an existing user?").place(x = 2, y = 80)
# 	var1 = IntVar()
# 	Checkbutton(window, text='yes', variable=var1).place(x = 2, y = 100)

# 	# Create Object  
# 	btn = tkinter.Button(window, text = 'Done', command = window.destroy) 
# 	btn.place(x=250,y=265)                      
	
# 	window.mainloop()   