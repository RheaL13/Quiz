import tkinter as tk
from tkinter import *
import tkinter
m = tkinter.Tk()

root = Tk()
w = Label(root, text='GeeksForGeeks.org!')
w.pack()
root.mainloop()

# import tkinter module 
from tkinter import *        

# Following will import tkinter.ttk module and 
# automatically override all the widgets 
# which are present in tkinter module. 
from tkinter.ttk import *

# Create Object
root = Tk() 

# Initialize tkinter window with dimensions 100x100             
root.geometry('100x100')     

btn = Button(root, text = 'Click me !', 
                command = root.destroy) 

# Set the position of button on the top of window 
btn.pack(side = 'top')     

root.mainloop() 



# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()

# master = Tk()
# Label(master, text='First Name').grid(row=0)
# Label(master, text='Last Name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()

# master = Tk()
# var1 = IntVar()
# Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
# mainloop()

# top = Tk()
# Lb = Listbox(top)
# Lb.insert(1, 'Python')
# Lb.insert(2, 'Java')
# Lb.insert(3, 'C++')
# Lb.insert(4, 'Any other')
# Lb.pack()
# top.mainloop()

# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
# mylist = Listbox(root, yscrollcommand=scrollbar.set)

# for line in range(100):
#     mylist.insert(END, 'This is line number' + str(line))
    
# mylist.pack(side=LEFT, fill=BOTH)
# scrollbar.config(command=mylist.yview)
# mainloop()

# import tkinter as tk
# from tkinter import ttk

# def on_select(event):
#     selected_item = combo_box.get()
#     label.config(text="Selected Item: " + selected_item)

# root = tk.Tk()
# root.title("Combobox Example")

# # Create a label
# label = tk.Label(root, text="Selected Item: ")
# label.pack(pady=10)

# # Create a Combobox widget
# combo_box = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
# combo_box.pack(pady=5)

# # Set default value
# combo_box.set("Option 1")

# # Bind event to selection
# combo_box.bind("<<ComboboxSelected>>", on_select)

# root.mainloop()

# from tkinter import *

# main = Tk()
# ourMessage = 'This is our Message'
# messageVar = Message(main, text=ourMessage)
# messageVar.config(bg='lightgreen')
# messageVar.pack()
# main.mainloop()

# import tkinter as tk
# from tkinter import ttk
# import time

# def start_progress():
#     progress.start()

#     # Simulate a task that takes time to complete
#     for i in range(101):
#       # Simulate some work
#         time.sleep(0.05)  
#         progress['value'] = i
#         # Update the GUI
#         root.update_idletasks()  
#     progress.stop()

# root = tk.Tk()
# root.title("Progressbar Example")

# # Create a progressbar widget
# progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
# progress.pack(pady=20)

# # Button to start progress
# start_button = tk.Button(root, text="Start Progress", command=start_progress)
# start_button.pack(pady=10)

# root.mainloop()

# from tkinter import *

# root = Tk()
# T = Text(root, height=2, width=30)
# T.pack()
# T.insert(END, 'GeeksforGeeks\nBEST WEBSITE\n')
# mainloop()

# from tkinter import *

# master = Tk()
# w = Canvas(master, width=40, height=60)
# w.pack()
# canvas_height=20
# canvas_width=500
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y )
# mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.title("Color Options in Tkinter")

# # Create a button with active background and foreground colors
# button = tk.Button(root, text="Click Me", activebackground="red", activeforeground="white")
# button.pack()

# # Create a label with background and foreground colors
# label = tk.Label(root, text="Hello, Tkinter!", bg="lightgray", fg="black")
# label.pack()

# # Create an Entry widget with selection colors
# entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black")
# entry.pack()

# root.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.title("Pack Example")

# # Create three buttons
# button1 = tk.Button(root, text="Button 1")
# button2 = tk.Button(root, text="Button 2")
# button3 = tk.Button(root, text="Button 3")

# # Pack the buttons vertically
# button1.pack()
# button2.pack()
# button3.pack()

# root.mainloop()

# import tkinter
# # Let's create the Tkinter window
# window = tkinter.Tk()
# window.title("GUI")

# # You will create two text labels namely 'username' and 'password' and and two input labels for them

# tkinter.Label(window, text = "Username").grid(row = 0) #'username' is placed on position 00 (row - 0 and column - 0)

# # 'Entry' class is used to display the input-field for 'username' text label
# tkinter.Entry(window).grid(row = 0, column = 1) # first input-field is placed on position 01 (row - 0 and column - 1)

# tkinter.Label(window, text = "Password").grid(row = 1) #'password' is placed on position 10 (row - 1 and column - 0)

# tkinter.Entry(window).grid(row = 1, column = 1) #second input-field is placed on position 11 (row - 1 and column - 1)

# # 'Checkbutton' class is for creating a checkbutton which will take a 'columnspan' of width two (covers two columns)
# tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2)                 

# window.mainloop()


# m.mainloop()