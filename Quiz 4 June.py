#import everything from tkinter and import messagebox as mb from tkinter
from tkinter import *
# from tkinter import messagebox as mb
import tkinter as tk
import tkinter
import tkinter as tk
from tkinter import font
from tkinter import *      
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox


# # Function to validate login
# def validate_login():
#     username = entry_username.get()
#     password = entry_password.get()
    
#     # For demonstration purposes, using a hardcoded username and password
#     if username == "admin" and password == "password":
#         messagebox.showinfo("Login Info", "Login Successful!")
#     else:
#         messagebox.showerror("Login Info", "Invalid Username or Password")

# create sign up window when clicked
def signup():
    # Create the main window
    signupw = tk.Tk()
    signupw.title("Sign Up Page")
    signupw.geometry("300x300")

    # Set the size of the window and center it
    window_width = 300
    window_height = 200
    screen_width = signupw.winfo_screenwidth()
    screen_height = signupw.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Create a frame to hold the widgets and center it
    frame2 = tk.Frame(signupw)
    frame2.pack(expand=True)

    # buttons to change (sign up or login)
    signupbtn = tk.Button(signupw, text = "Login", font = ("Helvetica", 11), 
                        command = login)
    signupbtn.place(x = 225, y = 10)

    # Create and place the username label and entry
    title = tk.Label(signupw, text="SIGN UP", font = ("Helvetica", 12))
    title.place(x = 130, y = 15)

    # Create and place the username label and entry
    label_username = tk.Label(frame2, text="Username", font = ("Helvetica", 11))
    label_username.pack(pady=(0, 5))

    entry_username = tk.Entry(frame2)
    entry_username.pack(pady=(0, 10))

    # Create and place the password label and entry
    label_password = tk.Label(frame2, text="Password", font = ("Helvetica", 11))
    label_password.pack(pady=(0, 5))

    entry_password = tk.Entry(frame2, show="*")
    entry_password.pack(pady=(0, 20))

    # Create and place the login button
    login_button = tk.Button(frame2, text="Next", font = ("Helvetica", 11))
                            #   command=validate_login)
    login_button.pack()

    signupw.mainloop()

def login():
    # Create the main window
    login = tk.Tk()
    login.title("Login Page")
    login.geometry("300x300")

    # Set the size of the window and center it
    window_width = 300
    window_height = 200
    screen_width = login.winfo_screenwidth()
    screen_height = login.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Create a frame to hold the widgets and center it
    frame = tk.Frame(login)
    frame.pack(expand=True)

    # buttons to change (sign up or login)
    signupbtn = tk.Button(login, text = "Sign Up", font = ("Helvetica", 11), 
                        command = signup)
    signupbtn.place(x = 225, y = 10)

    # Create and place the username label and entry
    title = tk.Label(login, text="LOGIN", font = ("Helvetica", 12))
    title.place(x = 130, y = 15)

    # Create and place the username label and entry
    label_username = tk.Label(frame, text="Username", font = ("Helvetica", 11))
    label_username.pack(pady=(0, 5))

    entry_username = tk.Entry(frame)
    entry_username.pack(pady=(0, 10))

    # Create and place the password label and entry
    label_password = tk.Label(frame, text="Password", font = ("Helvetica", 11))
    label_password.pack(pady=(0, 5))

    entry_password = tk.Entry(frame, show="*")
    entry_password.pack(pady=(0, 20))

    # Create and place the login button
    login_button = tk.Button(frame, text="Next", font = ("Helvetica", 11))
                            #   command=validate_login)
    login_button.pack()

    login.mainloop()

# First window
class first:
    # Creating window
    firstwindow = tkinter.Tk()
    firstwindow.geometry("1200x750")
    firstwindow.title("Overconsumption Quiz")
    firstwindow.configure(bg="oldlace")  
	
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

    # # Function to create the pop-up login window
    # def open_signup():
    #     popup = tkinter.Tk()
    #     popup.title("Sign Up")
    #     popup.geometry("500x400")  # size of the pop-up window

    #     label = tk.Label(popup, text="SIGN UP")
    #     label.pack()

    #     closebutton1 = tk.Button(popup, text = "Next", command = popup.destroy)
    #     closebutton1.place(x = 230, y = 320)

    # # Function to create the pop-up sign up window 
    # def open_login():
    #     popup = tkinter.Tk()
    #     popup.title("Login")
    #     popup.geometry("500x400")  #size of the pop-up window

    #     label = tk.Label(popup, text="LOGIN")
    #     label.pack()

    #     closebutton2 = tk.Button(popup, text = "Next", command = popup.destroy)
    #     closebutton2.place(x = 230, y = 320)

    # Function to create the pop-up exit window 
    def check():
        popup = tkinter.Tk()
        popup.title("Exit")
        popup.geometry("190x100")  #size of the pop-up window

        label = tk.Label(popup, text="Are you sure you want\n to exit now?", 
                         font = ("Helvetica", 13))
        label.pack()

        yesbutton = tk.Button(popup, text = "Yes", command = popup.destroy)
        # firstone.destroy()
        yesbutton.place(x = 60, y = 65)

        nobutton = tk.Button(popup, text = "No", command = popup.destroy)
        nobutton.place(x = 100, y = 65)

    # login / sign up button 
    login = tk.Button(firstwindow, text = 'LOGIN', width = 10, height = 2,
                   fg = "green", bg = "white", command = login) 
    signup = tk.Button(firstwindow, text = 'SIGN UP', width = 10, height = 2,
                    fg = "green", bg = "white", command = signup) 
    exit = tk.Button(firstwindow, text = 'EXIT', width = 10, height = 2,
                     fg = "white", bg = "black", command = check) 

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

    #message for button click
    # message = "Please sign in or login first please."

    # def clickAbout():
    #     toplevel = Toplevel()
    #     label1 = Label(toplevel, text="message", height=0, width=100)
    #     label1.pack()

    # Function to create the pop-up window
    def open_popup():
        popup = tkinter.Tk()
        popup.title("Pop Up")
        popup.geometry("250x130")  # Set the size of the pop-up window

        label = tk.Label(popup, text="Please login or sign up first please.")
        label.place(x = 30, y = 20)

        closebutton = tk.Button(popup, text="Close", command=popup.destroy)
        closebutton.place(x = 115, y = 90)

    # buttons for side bar
    homebtn = tk.Button(firstwindow, text = 'HOME', width = 10, height = 2,
                   fg = "green", bg = "white", command = open_popup) 
    quizbtn = tk.Button(firstwindow, text = 'QUIZ', width = 10, height = 2,
                    fg = "green", bg = "white", command = open_popup) 
    altbtn = tk.Button(firstwindow, text = 'SUCCESS\nSTORIES', width = 10, 
                       height = 2, fg = "green", bg = "white", 
                       command = open_popup)
    sucessbtn = tk.Button(firstwindow, text = 'ALTERNATIVE\nPRODUCTS', 
                          width = 10, height = 2, fg = "green", bg = "white", 
                          command = open_popup) 
    aboutbtn = tk.Button(firstwindow, text = 'ABOUT', width = 10, height = 2,
                    fg = "green", bg = "white", command = open_popup) 
    helpbtn = tk.Button(firstwindow, text = 'HELP', width = 10, height = 2,
                    fg = "green", bg = "white", command = open_popup)
    
    # Set the position of button on the top of window 
    homebtn.place(x=50, y=50)
    quizbtn.place(x=50, y=150) 
    altbtn.place(x=50, y=250)
    sucessbtn.place(x=50, y=350)
    aboutbtn.place(x=50, y=450) 
    helpbtn.place(x=50, y=550)

    # picture 
    our_canvas = Canvas(firstwindow, width = 300, height = 200, bg = "blue")
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