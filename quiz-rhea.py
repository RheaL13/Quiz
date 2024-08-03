# MAIN UP TO DATE CODE - 2 August

import tkinter as tk
import tkinter.messagebox as mb
from datetime import datetime
from PIL import Image, ImageTk
import os
import random
from tkinter import ttk, IntVar, Text, INSERT
import tkinter as tk
import tkinter.messagebox as mb
import re
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from datetime import datetime
import re
from tkinter import *
from tkinter import messagebox as mb
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import IntVar
import tkinter as tk
from tkinter import IntVar, messagebox as mb, ttk
import random
import tkinter as tk
from tkinter import messagebox as mb, IntVar
from tkinter import ttk
from datetime import datetime
import random
import webbrowser

# data of questions and answers
data = {
    "question": [
        "What does over-consumption mean?",
        "Who do you think is the biggest consumer group for material stuff?",
        "How many kgs of waste ends up in our landfill every year?",
        "How many kgs does each household contribute?",
        "What percent of the waste ends up getting recycled?",
        "If all 8 billion of us consumed at the level of the average citizen "
        "of the United States of America, we would need about ___ earths.",
        "What are some ways to consume sustainability?",
        "By 2100, if we do nothing, the temperature of the Earth's surface is"
        " projected to increase by how much?",
        "How much e-waste is generated globally each year?",
        "Which material is the most commonly overconsumed and leads to "
        "significant environmental pollution?",
        "How does overconsumption contribute to climate change?",
        "What percentage of global food production is wasted annually?",
        "What is the main driver of overconsumption in developed countries?",
        "What is the average carbon footprint of an individual in a high-"
        "consumption country per year?",
        "What is the estimated amount of plastic waste produced globally "
        "each year?"
    ],
    "answer": [
        2,  # question 1 answer
        2,  # question 2 answer
        1,  # question 3 answer
        3,  # question 4 answer
        3,  # question 5 answer
        3,  # question 6 answer
        4,  # question 7 answer
        2,  # question 8 answer
        3,  # question 9 answer
        4,  # question 10 answer
        1,  # question 11 answer
        3,  # question 12 answer
        2,  # question 13 answer
        4,  # question 14 answer
        1  # question 15 answer
    ],
    "options": [
        ["The decrease of the use of cars",
         "The excessive consumption or use of something",
         "The decrease consumption of something",
         "The excessive use of energy"
         ],
        ["Millennials (1981 - 1996)",
         "Gen Z (1997 - 2012)",
         "Gen X (1965 - 1980)",
         "Baby Boomers (1946 - 1964)"
         ],
        ["17,000,000 tonnes",
         "25,000,000 tonnes",
         "14,000,000 tonnes",
         "1,000,000 tonnes"
         ],
        ["510 kgs",
         "626 kgs",
         "784 kgs",
         "976 kgs"
         ],
        ["12%",
         "28%",
         "37%",
         "72%"
         ],
        ["At least 3",
         "At least 4",
         "At least 5",
         "At least 6"
         ],
        ["Reduce, Reuse, Recycle",
         "Support Local and Organic",
         "Advocate for Change",
         "All of the above"
         ],
        ["2°C",
         "4°C",
         "6°C",
         "8°C"
         ],
        ["10 million tonnes",
         "20 million tonnes",
         "50 million tonnes",
         "100 million tonnes"
         ],
        ["Glass",
         "Wood",
         "Metal",
         "Plastic"
         ],
        ["It increases greenhouse gas emissions.",
         "It reduces greenhouse gas emissions.",
         "It has no impact on climate change.",
         "It stabilizes the climate."
         ],
        ["10%",
         "20%",
         "30%",
         "40%"
         ],
        ["Lack of awareness",
         "Cultural values and consumerism",
         "Government policies",
         "Environmental regulations"
         ],
        ["2 tonnes CO2",
         "5 tonnes CO2",
         "10 tonnes CO2",
         "20 tonnes CO2"
         ],
        ["300 million tonnes",
         "500 million tonnes",
         "700 million tonnes",
         "1 billion tonnes"
         ]
    ]
}
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("EcoSmart")
        self.master.configure(bg="oldlace")
        self.master.resizable(False, False)

        # Calculate center position
        window_width = 1200
        window_height = 750
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 4

        # Set window geometry
        self.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.firstwindow = tk.Frame(self.master, bg="oldlace")
        self.firstwindow.pack(fill="both", expand=True)

        label = tk.Label(self.firstwindow, text="EcoSmart\nOverconsumption Quiz", font=("Helvetica", 35, "bold"), fg="green", bg="oldlace")
        label.pack(pady=40)

        description = tk.Label(self.firstwindow, text="Welcome!\nThis "
                                 "program is to teach and test you on "
                                 "your knowledge about \nover-consumption. "
                                 "If you are new here, please sign up, "
                                 "otherwise login.",font=("Helvetica", 18), 
                                 fg="green", bg="oldlace")
        description.place(x = 320, y = 140)

        signup_button = tk.Button(self.firstwindow, text="SIGN UP", width=10, 
                                  height=2, fg="green", bg="white",
                                  command=self.signup)
        signup_button.place(x=1050, y=35)

        login_button = tk.Button(self.firstwindow, text="LOGIN", width=10, 
                                 height=2, fg="green", bg="white",
                                 command=self.login)
        login_button.place(x=900, y=35)

        exit_button = tk.Button(self.firstwindow, text='EXIT', width=10, 
                                height=2, fg="black", bg="white", 
                                command=self.check_exit)
        exit_button.place(x=1050, y=685)

        # code to add a picture to first window
        # Read the Image
        image = Image.open("picture1.png")

        # Resize the image using resize() method
        resize_image = image.resize((650, 500))

        img = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
        label1 = tk.Label(image=img)
        label1.image = img
        label1.place(x=280, y=220)

        self.pending_user_info = {}
        self.create_sidebar()

    def create_sidebar(self):
        buttons = [
            ("HOME", self.open_popup),
            ("USER\nMANUAL", self.open_popup),
            ("QUIZ", self.open_popup),
            ("LEARN", self.open_popup),
            ("ALTERNATIVE\nPRODUCTS", self.open_popup),
            ("ABOUT", self.open_popup),
            ("HELP", self.open_popup)
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(self.master, text=text, width=10, height=2, fg="green", bg="white", command=command)
            btn.place(x=50, y=50 + i * 100)

    def check_exit(self):
        result = mb.askquestion("Exit", "Are you sure you want to exit the program now?")
        if result == "yes":
            self.master.destroy()

    def open_popup(self):
        mb.showwarning("Warning", "Please login or sign up first please.")

    def signup(self):
        self.signup_window = SignupWindow(self)
    
    def login(self):
        self.login_window = LoginWindow(self)

    def store_pending_user_info(self, first_name, username, password, date_of_birth):
        self.pending_user_info = {
            "username": username,
            "password": password,
            "first_name": first_name,
            "date_of_birth": date_of_birth
        }
        self.user_info = self.pending_user_info

class SignupWindow:
    def __init__(self, parent):
        self.parent = parent
        self.signup_window = tk.Toplevel()
        self.signup_window.title("Signup Window")
        self.signup_window.configure(bg="oldlace")
        self.signup_window.resizable(False, False)

        # Calculate center position
        window_width = 600
        window_height = 550
        screen_width = self.signup_window.winfo_screenwidth()
        screen_height = self.signup_window.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 4

        # Set window geometry
        self.signup_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        title = tk.Label(self.signup_window, text="Sign Up", 
                         font=("Helvetica", 20, "bold"), fg="black", bg="oldlace")
        title.pack(pady=20)

        title1 = tk.Label(self.signup_window, text="First Name", 
                          font=("Helvetica", 15, "bold"), fg = "black", bg="oldlace")
        title1.pack(pady=2)

        self.first_name = self.create_entry("First Name")

        title2 = tk.Label(self.signup_window, text="Username", 
                          font=("Helvetica", 15, "bold"), fg = "black", bg="oldlace")
        title2.pack(pady=2)

        self.username = self.create_entry("Username")

        title3 = tk.Label(self.signup_window, text="Password", 
                          font=("Helvetica", 15, "bold"), fg = "black", bg="oldlace")
        title3.pack(pady=2)

        self.password = self.create_entry("Password", show="*")

        title4 = tk.Label(self.signup_window, text="Confirm Password", 
                          font=("Helvetica", 15, "bold"), fg = "black", 
                          bg="oldlace")
        title4.pack(pady=2)

        self.confirm_password = self.create_entry("Password", show="*")

        title5 = tk.Label(self.signup_window, text="Date of Birth (DD/MM/YYYY)", 
                          font=("Helvetica", 15, "bold"), fg = "black", 
                          bg="oldlace")
        title5.pack(pady=2)

        self.date_of_birth = self.create_entry("Date of Birth (DD/MM/YYYY)")

        next_button = tk.Button(self.signup_window, text="NEXT", width=7,
                                font = ("Helvetica", 15, "bold"), 
                                height=2, fg="green", bg="white", 
                                command=self.signup)
        next_button.pack(pady=20)

        def change2():
            LoginWindow(parent)
            self.signup_window.destroy()

        login_change_button = tk.Button(self.signup_window, text="LOGIN", 
                                        font = ("Helvetica", 15, "bold"),
                                        width=7, height=2, fg="green", 
                                        bg="white", command=change2)
        login_change_button.place(x=480, y=20)

        back_button = tk.Button(self.signup_window, text="BACK", width=7,
                                font = ("Helvetica", 15, "bold"),
                                height=2, fg="black", bg="white", 
                                command=self.signup_window.destroy)
        back_button.place(x=480, y=485)

    def create_entry(self, placeholder, show=None):
        entry = tk.Entry(self.signup_window, show=show)
        entry.pack(pady=10)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event, e=entry, p=placeholder: self.on_entry_click(event, e, p))
        entry.bind("<FocusOut>", lambda event, e=entry, p=placeholder: self.on_focusout(event, e, p))
        entry.config(fg="grey")
        return entry

    def on_entry_click(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(fg="white")

    def on_focusout(self, event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    def validate_date_of_birth(self, date_of_birth):
        try:
            birthdate = datetime.strptime(date_of_birth, "%d/%m/%Y")
            return birthdate
        except ValueError:
            return None

    def validate_fields(self):
        first_name = self.first_name.get().strip()
        username = self.username.get().strip()
        password = self.password.get().strip()
        confirm_password = self.confirm_password.get().strip()
        date_of_birth = self.date_of_birth.get().strip()

        if (first_name == "First Name" or username == "Username" or 
            password == "Password" or confirm_password == "Confirm Password" or 
            date_of_birth == "Date of Birth (DD/MM/YYYY)"):
            mb.showwarning("Incomplete Fields", "Please fill out all the fields.", parent=self.signup_window)
            return False
        
        if len(first_name) > 10 or len(username) > 10 or len(password) > 10:
            mb.showwarning("Invalid Input", "First name, username, and password must be 10 characters or less.", parent=self.signup_window)
            return False

        if not first_name.isalpha():
            mb.showwarning("Invalid First Name", "First name can only contain letters.", parent=self.signup_window)
            return False

        if not re.match("^[A-Za-z0-9]+$", username):
            mb.showwarning("Invalid Username", "Username can only contain letters and numbers without spaces.", parent=self.signup_window)
            return False

        if password != confirm_password:
            mb.showerror("Error", "Passwords do not match.", parent=self.signup_window)
            return False

        birthdate = self.validate_date_of_birth(date_of_birth)
        if not birthdate:
            mb.showerror("Invalid Birthdate", "Please enter a valid birthdate.", parent=self.signup_window)
            return False

        age = (datetime.today() - birthdate).days // 365
        if age < 0 or age > 90:
            mb.showerror("Invalid Birthdate", "Invalid birthdate.", parent=self.signup_window)
            return False
        elif age < 18 or age > 30:
            if age < 10:
                age_maybe = mb.askquestion("Age Notice", "Are you sure that is the correct age?", parent=self.signup_window)
                if age_maybe == "no":
                    return False
            else:
                mb.showwarning("Age Notice", "This program is designed for ages 18-30. You are still able to use the program.", parent=self.signup_window)
        else:
            mb.showwarning("Age Notice", "This program is designed for ages 18-30.", parent=self.signup_window)
                
        return True
    
    def open_dashboard(self):
        self.dashboard = DashboardWindow(self.parent.master, self.parent.pending_user_info)

    def signup(self):
        if not self.validate_fields():
            return

        first_name = self.first_name.get().strip()
        username = self.username.get().strip()
        password = self.password.get().strip()
        date_of_birth = self.date_of_birth.get().strip()
        birthdate = self.validate_date_of_birth(date_of_birth)

        if os.path.exists(f"{username}.txt"):
            mb.showwarning("Warning", "Your username already exists. Please choose another one or if you have already signed up before, please login (click the button on the top right)", parent=self.signup_window)
            return

        with open(f"{username}.txt", "w") as file:
            file.write(f"First Name: {first_name}\n")
            file.write(f"Birthdate: {birthdate.strftime('%d/%m/%Y')}\n")
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n")

        self.parent.store_pending_user_info(first_name, username, password, date_of_birth)
        
        mb.showinfo("Success", "Your data has been saved. Please login next "
                    "time with your exact details. Thank you :)", 
                    parent=self.signup_window)
        self.signup_window.destroy()
        self.open_dashboard()

class LoginWindow:
    def __init__(self, parent):
        self.parent = parent
        self.login_window = tk.Toplevel()
        self.login_window.title("Login Window")
        self.login_window.configure(bg="oldlace")
        self.login_window.resizable(False, False)

        # Calculate center position
        window_width = 600
        window_height = 320
        screen_width = self.login_window.winfo_screenwidth()
        screen_height = self.login_window.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 4

        # Set window geometry
        self.login_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        title = tk.Label(self.login_window, text="Login", font=("Helvetica", 20, "bold"), fg = "black", bg="oldlace")
        title.pack(pady=20)

        title1 = tk.Label(self.login_window, text="Username", font=("Helvetica", 15, "bold"), fg = "black", bg="oldlace")
        title1.pack(pady=2)

        self.username = self.create_entry("Username")

        title2 = tk.Label(self.login_window, text="Password", font=("Helvetica", 15, "bold"), fg = "black", bg="oldlace")
        title2.pack(pady=2)
        
        self.password = self.create_entry("Password", show="*")

        next_button = tk.Button(self.login_window, text="NEXT", width=7, 
                                height=2, fg="green", bg="white", 
                                font = ("Helvetica", 15, "bold"),
                                command=self.login)
        next_button.pack(pady=20)

        def change():
            SignupWindow(parent)
            self.login_window.destroy()

        signup_change_button = tk.Button(self.login_window, text="SIGN UP", 
                                         font = ("Helvetica", 15, "bold"), width=7, 
                                height=2, fg="green", bg="white", command=change)
        signup_change_button.place(x=480, y=20)

        back_button = tk.Button(self.login_window, text="BACK", 
                                font = ("Helvetica", 15, "bold"), width=7, 
                                height=2, fg="black", bg="white", 
                                command=self.login_window.destroy)
        back_button.place(x=480, y=260)

    def create_entry(self, placeholder, show=None):
        entry = tk.Entry(self.login_window, show=show)
        entry.pack(pady=10)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event, e=entry, p=placeholder: self.on_entry_click(event, e, p))
        entry.bind("<FocusOut>", lambda event, e=entry, p=placeholder: self.on_focusout(event, e, p))
        entry.config(fg="grey")
        return entry

    def on_entry_click(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(fg="white")

    def on_focusout(self, event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    def open_dashboard(self):
        self.dashboard = DashboardWindow(self.parent.master, self.parent.pending_user_info)

    def validate_login(self, username, password):
        if os.path.exists(f"{username}.txt"):
            with open(f"{username}.txt", "r") as file:
                lines = file.readlines()
                stored_username = lines[2].split(": ")[1].strip()
                stored_password = lines[3].split(": ")[1].strip()
                if username == stored_username and password == stored_password:
                    self.parent.store_pending_user_info(
                        first_name=lines[0].split(": ")[1].strip(),
                        username=stored_username,
                        password=stored_password,
                        date_of_birth=lines[1].split(": ")[1].strip()
                    )
                    return True
        return False

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if self.validate_login(username, password):
            self.login_window.destroy()
            self.open_dashboard()
        else:
            mb.showerror("Error", "Invalid username or password")

# Randomised quiz questions
class R_Quiz:
    def __init__(self, root, user_info):
        self.root = root
        self.root.configure(bg="oldlace")
        self.q_no = 0
        self.correct = 0
        self.user_info = user_info
        self.display_title()

        # Prepare and shuffle the questions
        self.prepare_questions()

        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_question()
        self.display_options()
        self.buttons()
        self.data_size = len(self.questions)

        # Progress bar
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("green.Horizontal.TProgressbar", 
                        thickness=30, 
                        troughcolor='black', 
                        background='green')
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, maximum=100, length=300, variable=self.progress_var, style="green.Horizontal.TProgressbar")
        self.progress_bar.place(x=50, y=95)
        self.update_progress_bar()

    def prepare_questions(self):
        combined = list(zip(data['question'], data['answer'], data['options']))
        random.shuffle(combined)
        self.questions, self.answers, self.options = zip(*combined)

    def next_btn(self):
        if self.opt_selected.get() == 0:
            mb.showwarning("Warning", "Please select an option before proceeding.", parent=self.root)
            return
        
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        self.update_progress_bar()
        if self.q_no == self.data_size:
            self.update_progress_bar(final=True)  # Set progress bar to 100%
            self.display_result()
            self.root.destroy()
        else:
            self.display_question()
            self.display_options()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}", parent=self.root)

        # Save results to user's file with their info
        username = self.user_info.get("username", "user")
        with open(f"{username}.txt", 'a') as data: 
            data.write("\nQuiz scores: \n")
            data.write(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            data.write(f"Correct: {self.correct}\n")
            data.write(f"Wrong: {wrong_count}\n")
            data.write(f"Score: {score}%\n")
        
        # Add the popup messagebox
        mb.showinfo("Learn More", "To do better next time, go to the 'LEARN' tab to learn more about over-consumption.", parent=self.root)

    def check_ans(self, q_no):
        return self.opt_selected.get() == self.answers[q_no]

    def buttons(self):
        next_button = tk.Button(self.root, text="NEXT", command=self.next_btn,
                             bg="white", fg="black", width = 7, height = 2, 
                             font=("Helvetica", 18, "bold"))
        next_button.place(x=470, y=550)
        quit_button = tk.Button(self.root, text="EXIT", 
                             bg="white", width = 7, height = 2,
                             fg="black", command = self.check_exit,
                             font=("Helvetica", 18, "bold"))
        quit_button.place(x=920, y=95)

    def check_exit(self):
        result = mb.askquestion("Exit", "Are you sure you want to exit the quiz now?", parent=self.root)
        if result == "yes":
            self.root.destroy()

    def display_options(self):
        val = 0
        self.opt_selected.set(0)  # Reset the selected option
        for option in self.options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        if hasattr(self, 'q_label'):
            self.q_label.destroy()  # Destroy previous question label
        self.q_label = tk.Label(self.root, text=self.questions[self.q_no], 
                             width=100, font=('Helvetica', 27, 'bold'), anchor='w', 
                             wraplength=900, justify='left', bg = "oldlace",
                             fg  = "black")
        self.q_label.place(x=50, y=150)

    def display_title(self):
        title = tk.Label(self.root, text="OVERCONSUMPTION QUIZ",
                      width=63, height = 2, bg="green", fg="white", 
                      font=("Helvetica", 30, "bold"))
        title.place(x=0, y=0)

    def radio_buttons(self):
        q_list = []
        y_pos = 250
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(self.root, text=" ", 
                                    variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("Helvetica", 24),
                                    fg = "black", bg = "oldlace")
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 60
        return q_list

    def update_progress_bar(self, final=False):
        if final:
            self.progress_var.set(100)
        else:
            self.progress_var.set((self.q_no / self.data_size) * 100)

class Quiz:
    def __init__(self, root, user_info):
        self.root = root
        self.root.configure(bg="oldlace")
        self.q_no = 0
        self.correct = 0
        self.user_info = user_info
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(data['question'])
        
        # Progress bar
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("green.Horizontal.TProgressbar", 
                        thickness=30, 
                        troughcolor='black', 
                        background='green')
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, maximum=100, length=300, variable=self.progress_var, style="green.Horizontal.TProgressbar")
        self.progress_bar.place(x=50, y=95)
        self.update_progress_bar()

    def next_btn(self):
        if self.opt_selected.get() == 0:
            mb.showwarning("Warning", "Please select an option before proceeding.", parent=self.root)
            return
        
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        self.update_progress_bar()
        if self.q_no == self.data_size:
            self.update_progress_bar(final=True)  # Set progress bar to 100%
            self.display_result()
            self.root.destroy()
        else:
            for opt in self.opts:  # Clear previous options
                opt.destroy()
            self.opts = self.radio_buttons()  # Recreate radio buttons for new options
            self.display_question()
            self.display_options()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}", parent=self.root)

        # Save results to user's file with their info
        username = self.user_info.get("username", "user")
        with open(f"{username}.txt", 'a') as data: 
            data.write("\nQuiz scores: \n")
            data.write(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            data.write(f"Correct: {self.correct}\n")
            data.write(f"Wrong: {wrong_count}\n")
            data.write(f"Score: {score}%\n")

        # Add the popup messagebox
        mb.showinfo("Learn More", "To do better next time, go to the 'LEARN' tab to learn more about over-consumption.", parent=self.root)

    def check_ans(self, q_no):
        return self.opt_selected.get() == data['answer'][q_no]

    def buttons(self):
        next_button = tk.Button(self.root, text="NEXT", command=self.next_btn,
                             bg="white", fg="black", width = 7, height = 2, 
                             font=("Helvetica", 18, "bold"))
        next_button.place(x=470, y=550)
        quit_button = tk.Button(self.root, text="EXIT", 
                             bg="white", width = 7, height = 2,
                             fg="black", command = self.check_exit,
                             font=("Helvetica", 18, "bold"))
        quit_button.place(x=920, y=95)

    def check_exit(self):
        result = mb.askquestion("Exit", "Are you sure you want to exit the quiz now?", parent=self.root)
        if result == "yes":
            self.root.destroy()

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in data['options'][self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        if hasattr(self, 'q_label'):
            self.q_label.destroy()  # Destroy previous question label
        self.q_label = tk.Label(self.root, text=data['question'][self.q_no], 
                             width=100, font=('Helvetica', 27, 'bold'), 
                             anchor='w', wraplength=900, justify='left',
                             bg = "oldlace", fg  = "black")
        self.q_label.place(x=50, y=150)

    def display_title(self):
        title = tk.Label(self.root, text="OVERCONSUMPTION QUIZ",
                      width=63, bg="green", fg="white", height = 2,
                      font=("Helvetica", 30, "bold"))
        title.place(x=0, y=0)

    def radio_buttons(self):
        q_list = []
        y_pos = 250
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(self.root, text=" ", 
                                    variable=self.opt_selected,
                                    value=len(q_list) + 1, 
                                    font=("Helvetica", 24),
                                    fg = "black", 
                                    bg = "oldlace")
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 60
        return q_list

    def update_progress_bar(self, final=False):
        if final:
            self.progress_var.set(100)
        else:
            self.progress_var.set((self.q_no / self.data_size) * 100)

class DashboardWindow:
    def __init__(self, master, user_info):
        self.master = master
        self.user_info = user_info
        self.dashboard_window = tk.Toplevel(master)
        self.dashboard_window.title("Dashboard")
        self.dashboard_window.configure(bg="oldlace")
        self.dashboard_window.resizable(False, False)

        # Calculate center position
        window_width = 1200
        window_height = 750
        screen_width = self.dashboard_window.winfo_screenwidth()
        screen_height = self.dashboard_window.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 4

        # Set window geometry
        self.dashboard_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        title = tk.Label(self.dashboard_window, text="EcoSmart", font=("Helvetica", 20, "bold"), fg="green", bg="oldlace")
        title.pack(pady=20)

        title2 = tk.Label(self.dashboard_window, text="User Manual", font=("Helvetica", 18, "bold"), fg="green", bg="oldlace")
        title2.pack(pady=10)

        # Sidebar and main area
        self.create_sidebar()
        self.create_main_area()

        exit_button = tk.Button(self.dashboard_window, text='EXIT', width=10, height=2, fg="black", bg="white", command=self.check_exit)
        exit_button.place(x=1050, y=685)

        signout_button = tk.Button(self.dashboard_window, text='SIGN OUT', width=10, height=2, fg="black", bg="white", command=self.signout)
        signout_button.place(x=1050, y=620)

        profile_button = tk.Button(self.dashboard_window, text='PROFILE', width=10, height=2, fg="green", bg="white", command=self.display_profile)
        profile_button.place(x=1050, y=50)

        self.display_home()

    def check_exit(self):
        result = mb.askquestion("Exit", "Are you sure you want to exit the program now?")
        if result == "yes":
            self.master.destroy()

    def signout(self):
        result = mb.askquestion("Sign Out", "Are you sure you want to sign out of the program now?")
        if result == "yes":
            self.dashboard_window.destroy()

    def create_sidebar(self):
        buttons = [
            ("HOME", self.display_home),
            ("USER\nMANUAL", self.display_manual),
            ("QUIZ", self.display_quiz),
            ("LEARN", self.display_success_stories),
            ("ALTERNATIVE\nPRODUCTS", self.display_alternative_products),
            ("ABOUT", self.display_about),
            ("HELP", self.display_help)
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(self.dashboard_window, text=text, width=10, height=2, fg="green", bg="white", command=command)
            btn.place(x=50, y=50 + i * 100)

    def create_main_area(self):
        self.main_frame = tk.Frame(self.dashboard_window, bg="oldlace")
        self.main_frame.place(x=250, y=50, width=900, height=700)

    def clear_main_area(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def display_home(self):
        self.clear_main_area()

        # Title label
        title_label = tk.Label(self.main_frame, text="Home Page", font=("Helvetica", 40), fg="black", bg="oldlace")
        title_label.place(x=240, y=5)

        label = tk.Label(self.main_frame, text="Welcome to the Home Page\nThis program is to teach and test you on "
                                               "your knowledge about \nover-consumption. Click the buttons on the side "
                                               "to navigate through the program.", font=("Helvetica", 16),
                         fg="green", bg="oldlace")
        label.place(x=80, y=60)

        # Load and display image
        home_image_path = "picture1.png"
        home_image = Image.open(home_image_path)
        resize_image = home_image.resize((750, 530))
        self.home_img = ImageTk.PhotoImage(resize_image)

        home_image_label = tk.Label(self.main_frame, image=self.home_img)
        home_image_label.image = self.home_img  # Keep reference to the image to prevent garbage collection
        home_image_label.place(y=130, x=0)

    def display_manual(self):
        self.clear_main_area()

        title2 = tk.Label(self.main_frame, text="User Manual", font=("Helvetica", 40), fg="black", bg="oldlace")
        title2.place(x = 230, y = 5)

        # Load and display image
        manual_image_path = "manual.png"
        manual_image = Image.open(manual_image_path)
        resize_image = manual_image.resize((730, 600))
        self.manual_img = ImageTk.PhotoImage(resize_image)

        manual_image_label = tk.Label(self.main_frame, image=self.manual_img)
        manual_image_label.image = self.manual_img  
        manual_image_label.place(y=80, x=5)

    def display_quiz(self):
        self.clear_main_area()

        # Title label
        title_label = tk.Label(self.main_frame, text="Quiz Page", 
                               font=("Helvetica", 40), fg="black", 
                               bg="oldlace")
        title_label.place(x=249, y=5)

        label = tk.Label(self.main_frame, text="Welcome to the Quiz Page\nTo"
                         " take the quiz, press the quiz button below.\n"
                         "And decide if you want to have it randomised or not"
                         ".\nThen go onto the Learn tab to teach yourself "
                         "more, to do better in the quiz.",
                         font=("Helvetica", 18), fg="green", bg="oldlace")
        label.place(x=50, y=80)

        # Load and display image
        image_path = "overconsumption.jpg"
        image = Image.open(image_path)
        resize_image = image.resize((775, 350))
        img = ImageTk.PhotoImage(resize_image)

        image_label = tk.Label(self.main_frame, image=img)
        image_label.image = img  # Keep reference to the image to prevent garbage collection
        image_label.place(y=230, x=0)

        # Quiz button
        quiz_button = tk.Button(self.main_frame, text='QUIZ', width=10,  # Adjusted placement to be within main_frame
                                height=2, fg="green", bg="white", 
                                command=self.step1_open_quiz_window)
        quiz_button.place(x=300, y=635)

    def display_success_stories(self):
        self.clear_main_area()

        # Title
        title_label = tk.Label(self.main_frame, text="Learn About Over-Consumption", font=("Helvetica", 40), fg="black", bg="oldlace")
        title_label.place(x=70, y=5)

        # Create a Canvas widget
        canvas = tk.Canvas(self.main_frame, bg="oldlace", width=750, height=530)
        canvas.place(x=-20, y=70)

        # Add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.place(x=733, y=70, height=536)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas
        frame = tk.Frame(canvas, bg="oldlace")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Function to update the scrollregion of the canvas
        def update_scrollregion(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        frame.bind("<Configure>", update_scrollregion)

        # Information content
        content = """
What is Over-Consumption?
Over-consumption refers to the excessive use of resources beyond what is sustainable. This habit leads to significant 
environmental degradation, including deforestation, loss of biodiversity, pollution, and climate change. The 
constant demand for new products fuels over-consumption, driven by the desire for the latest technology, fashion 
trends, and other consumer goods.

Historical Context of Over-Consumption
The Industrial Revolution
The roots of over-consumption trace back to the Industrial Revolution, which began in the late 18th century. This 
period marked a significant shift from manual labor to industrialized production, leading to mass production and 
mass consumption. Industries heavily relied on non-renewable resources such as coal and oil, driving economic 
growth but also causing severe environmental degradation and resource depletion.

Environmental Impact
The rapid industrialization resulted in increased pollution, deforestation, and the extraction of natural resources 
at unprecedented rates. The focus on economic expansion often overlooked environmental sustainability, setting a 
precedent for future consumption patterns.

The Current State of Over-Consumption
Affluent Lifestyles and Global Disparities
Today, over-consumption is a global challenge, predominantly driven by affluent lifestyles in developed countries. 
The consumption of natural resources varies widely across the globe, with wealthier nations consuming far more 
resources than developing countries. For instance, the average North American consumes 90 kilograms of resources 
each day, significantly higher than the global average.

Environmental Consequences
Modern consumption patterns contribute to increased carbon emissions, pollution, and biodiversity loss. The demand 
for new products and technological advancements exacerbates these issues. Despite efforts to improve efficiency 
through technology, the continuous rise in consumption levels offsets any gains towards sustainability.

Impact of Over-Consumption
Environmental Pollution: Over-consumption leads to increased waste production, much of which ends up in landfills or 
oceans. For example, plastic pollution has become a critical issue, contributing to the destruction of marine life and 
ecosystems.

Resource Depletion: The extraction and use of natural resources at unsustainable rates result in the depletion of vital 
resources such as water, minerals, and fossil fuels. This creates a strain on the environment and future generations.

Climate Change: The production and disposal of consumer goods are significant contributors to greenhouse gas 
emissions, driving climate change. The carbon footprint of high-consumption lifestyles, particularly in wealthier 
countries, exacerbates global warming.

Sustainable Practices
Addressing over-consumption requires individual lifestyle changes and broader economic reforms. Sustainable 
practices such as using renewable resources, reducing waste, and promoting circular economies are essential 
for mitigating the impacts of over-consumption.

Addressing Over-Consumption
Innovative Solutions
Looking ahead, addressing over-consumption demands a fundamental shift in how economies operate and how 
individuals perceive wealth and consumption. Relying solely on technological solutions is insufficient; systemic 
changes are necessary.

Economic and Policy Reforms
Future strategies include implementing policies that promote sustainable consumption, encouraging the development 
of green technologies, and fostering a culture of conservation and mindfulness.

Success Stories in Combating Over-Consumption
   Tamil Nadu, India: Tamil Nadu has shown that increasing literacy and workforce participation can correlate with 
   reduced carbon emissions. By focusing on education and sustainable economic practices, the state has made 
   strides in mitigating the impact of urbanization on the environment.

   Malaysia and the Philippines: These countries have implemented “ship-back” initiatives to return waste to the 
   originating countries in the Global North. This move has forced international measures for better waste management 
   and reinforced the importance of global environmental justice.

   UNICEF’s Efforts: UNICEF has been actively working to improve children’s environments worldwide. Their reports 
   highlight the need for better environmental policies that are child-sensitive, reducing pollutants, and ensuring 
   high-quality housing and neighborhoods. This effort also focuses on protecting the most vulnerable children 
   from environmental harms.

Conclusion
Understanding the historical context, current state, and future strategies for addressing over-consumption helps us 
appreciate the urgency of adopting sustainable practices. By learning from past mistakes and current successes, we 
can work towards a more sustainable and equitable future.
    """

        # Add the information content to the frame
        text_widget = tk.Text(frame, wrap=tk.WORD, font=("Helvetica", 14), bg="oldlace", bd=0, fg="black", width=100, height=33)
        text_widget.insert(tk.END, content)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(expand=True, fill=tk.BOTH)

        # Configure the scrollbar
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)

        # Add padding around the main frame for a cleaner look
        self.main_frame.pack_propagate(False)
        self.main_frame.config(padx=20, pady=20)

        # Add the Photos button
        photos_button = tk.Button(self.main_frame, text="MORE INFORMATION", font = ("Helvetica", 13, "bold"), command=self.open_photos_window)
        photos_button.place(x=260, y=625)

    def open_photos_window(self):
        self.photos_window = tk.Toplevel(self.master)
        self.photos_window.title("Photo / Videos")
        self.photos_window.configure(bg="oldlace")
        self.photos_window.resizable(False, False)

        # Calculate center position
        window_width = 1000
        window_height = 600
        screen_width = self.photos_window.winfo_screenwidth()
        screen_height = self.photos_window.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 4

        # Set window geometry
        self.photos_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        title = tk.Label(self.photos_window, text="EcoSmart", font=("Helvetica", 20, "bold"), fg="green", bg="oldlace")
        title.pack(pady=20)

                # VIDEO LINKS AND BUTTONS
        def open_video1():
            # URL of the YouTube video
            video_url = "https://www.youtube.com/watch?v=KLiXmteCvUI"
            webbrowser.open(video_url)
        
        # Label for video URL input
        video_url_label = Label(self.photos_window, text="Video About Our Obsession With Economic Growth:", font=("Helvetica", 14, 'bold'), fg="green", bg="oldlace")
        video_url_label.pack(pady=20)
        
        # Button to open the video
        btn = Button(self.photos_window, text="Play Video 1",font = ("Helvetica", 13, 'bold'), command=open_video1)
        btn.pack(pady=7)

        # VIDEO LINKS AND BUTTONS
        def open_video2():
            # URL of the YouTube video
            video_url = "https://www.youtube.com/watch?v=MilcnqXKjR4&t=177s"
            webbrowser.open(video_url)
        
        # Label for video URL input
        video_url_label = Label(self.photos_window, text="Video About How Consumerism Ruins Our Planet\nAnd Finances:", font=("Helvetica", 14, 'bold'), fg="green", bg="oldlace")
        video_url_label.pack(pady=20)

        # Button to open the video
        btn = Button(self.photos_window, text="Play Video 2",font = ("Helvetica", 13, 'bold'), command=open_video2)
        btn.pack(pady=7)

        # VIDEO LINKS AND BUTTONS
        def open_video3():
            # URL of the YouTube video
            video_url = "https://www.youtube.com/watch?v=8eoeB_Dxba8"
            webbrowser.open(video_url)

        # Label for video URL input
        video_url_label = Label(self.photos_window, text="Video About How Overconsumption\nThreatens Our Planet:", font=("Helvetica", 14, 'bold'), fg="green", bg="oldlace")
        video_url_label.pack(pady=20)
        
        # Button to open the video
        btn = Button(self.photos_window, text="Play Video 3",font = ("Helvetica", 13, 'bold'), command=open_video3)
        btn.pack(pady=7)

        # VIDEO LINKS AND BUTTONS
        def open_video4():
            # URL of the YouTube video
            video_url = "https://www.youtube.com/watch?v=gDc6PB5iGjI"
            webbrowser.open(video_url)
        
        # Label for video URL input
        video_url_label = Label(self.photos_window, text=" Video About Global Environmental\nImpacts Of Consumption:", font=("Helvetica", 14, 'bold'), fg="green", bg="oldlace")
        video_url_label.pack(pady=20)
        
        # Button to open the video
        btn = Button(self.photos_window, text="Play Video 4",font = ("Helvetica", 13, 'bold'), command=open_video4)
        btn.pack(pady=7)

        back = Button(self.photos_window, text="EXIT", font = ("Helvetica", 13, 'bold'), command=self.photos_window.destroy)
        back.pack(pady=10)

        # Load and display image 1
        image_path1 = "picture4.webp"
        image1 = Image.open(image_path1)
        resize_image1 = image1.resize((250, 250))
        img1 = ImageTk.PhotoImage(resize_image1)

        image_label1 = tk.Label(self.photos_window, image=img1)
        image_label1.image = img1  # Keep reference to the image to prevent garbage collection
        image_label1.place(y=20, x=19)

        # Load and display image 2
        image_path2 = "picture3.jpg"
        image2 = Image.open(image_path2)
        resize_image2 = image2.resize((250, 250))
        img2 = ImageTk.PhotoImage(resize_image2)

        image_label2 = tk.Label(self.photos_window, image=img2)
        image_label2.image = img2  # Keep reference to the image to prevent garbage collection
        image_label2.place(y=20, x=730)

        # Load and display image 3
        image_path3 = "picture2.jpg"
        image3 = Image.open(image_path3)
        resize_image3 = image3.resize((350, 250))
        img3 = ImageTk.PhotoImage(resize_image3)

        image_label3 = tk.Label(self.photos_window, image=img3)
        image_label3.image = img3  # Keep reference to the image to prevent garbage collection
        image_label3.place(y=330, x=630)

        # Load and display image 4
        image_path4 = "picture5.png"
        image4 = Image.open(image_path4)
        resize_image4 = image4.resize((350, 250))
        img4 = ImageTk.PhotoImage(resize_image4)

        image_label4 = tk.Label(self.photos_window, image=img4)
        image_label4.image = img4  # Keep reference to the image to prevent garbage collection
        image_label4.place(y=330, x=19)
        
    def display_alternative_products(self):
        self.clear_main_area()

        title_label = tk.Label(self.main_frame, text="Budget-Friendly Alternative Products Page", 
                            font=("Helvetica", 40), fg="black", bg="oldlace")
        title_label.place(x=0, y=5)

        columns = ('PRODUCTS', 'ALTERNATIVES')
        tree = ttk.Treeview(self.main_frame, columns=columns, show='headings')
        tree.heading('PRODUCTS', text='PRODUCTS')
        tree.heading('ALTERNATIVES', text='ALTERNATIVES')

        products_alternatives = [
            ('Glad Wrap', 'Beeswax wraps'),
            ('Plastic Bags', 'Reusable cloth bags'),
            ('Plastic Containers', 'Glass or stainless steel containers'),
            ('Plastic Straws', 'Metal, bamboo, or glass straws'),
            ('Disposable Coffee Cups', 'Reusable coffee cups'),
            ('Plastic Cutlery', 'Bamboo or metal cutlery'),
            ('Paper Towels', 'Reusable cloth towels'),
            ('Single-use Water Bottles', 'Reusable water bottles'),
            ('Disposable Razors', 'Safety razors'),
            ('Plastic Toothbrushes', 'Bamboo toothbrushes'),
            ('Conventional Cotton Pads', 'Reusable makeup remover pads'),
            ('Plastic Wrap', 'Silicone food covers'),
            ('Disposable Menstrual Products', 'Menstrual cups or reusable cloth pads')
        ]

        for product, alternative in products_alternatives:
            tree.insert('', tk.END, values=(product, alternative))

        tree.place(x=0, y=100, width=770, height=530)

        # line between the 2 columns???
        # self.main_frame.create_line(15, 25, 200, 25, width=5)
        # self.main_frame.pack()

        # Add some styling
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 16, "bold"), foreground="green")
        style.configure("Treeview", font=("Helvetica", 14), rowheight=38)

    def display_about(self):
        self.clear_main_area()

        label = tk.Label(self.main_frame, text="Welcome to the About Page", font=("Helvetica", 16), fg="oldlace", bg="oldlace")
        label.pack(pady=20)

        # Title label
        title_label = tk.Label(self.main_frame, text="About Page", font=("Helvetica", 40), fg="black", bg="oldlace")
        title_label.place(x=235, y=5)

        # Create a Text widget to display file contents
        self.configfile = Text(self.main_frame, wrap="word", bd=0, bg="oldlace", font=("Helvetica", 14))
        self.configfile.config(state='normal')  # Temporarily set to normal to insert text
        self.configfile.place(x = 0, y = 100, width = 775, height = 250)

        # Add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.configfile.yview)
        scrollbar.place(x=762, y=100, height=250)
        self.configfile.configure(yscrollcommand=scrollbar.set)

        # Define tags for the font color and bold text
        self.configfile.tag_configure("custom_color", foreground="black")
        self.configfile.tag_configure("bold", font=("Helvetica", 14, "bold"))

        # Open and read the file
        filename = "aboutpagetext"
        try:
            with open(filename, 'r') as f:
                content = f.read()
                self.configfile.insert(INSERT, content)
                
                # Example of making specific text bold
                self.configfile.tag_add("bold", "1.0", "1.end")
                self.configfile.tag_add("bold", "5.0", "5.end")
                self.configfile.tag_add("bold", "6.0", "6.end")
                self.configfile.tag_add("bold", "9.0", "9.end")
                self.configfile.tag_add("bold", "12.0", "12.end")
                self.configfile.tag_add("bold", "15.0", "15.end")
                self.configfile.tag_add("bold", "18.0", "18.end")
                
                # Apply custom color to the entire content
                self.configfile.tag_add("custom_color", "1.0", "end")
        except FileNotFoundError:
            self.configfile.insert(INSERT, f"Error: File '{filename}' not found.")
        
        self.configfile.config(state='disabled')  # Make the Text widget read-only

        # Load and display image
        image_path = "aboutus.png"
        image = Image.open(image_path)
        resize_image = image.resize((700, 300))
        img = ImageTk.PhotoImage(resize_image)

        image_label = tk.Label(self.main_frame, image=img)
        image_label.image = img  # Keep reference to the image to prevent garbage collection
        image_label.place(x = 30, y = 370)

    def display_help(self):
        self.clear_main_area()

        # Title label
        title_label = tk.Label(self.main_frame, text="Help Page", font=("Helvetica", 40), fg="black", bg="oldlace")
        title_label.place(x=255, y=5)

        # Create a Text widget to display file contents
        self.configfile = Text(self.main_frame, wrap="word", bd=0, bg="oldlace", font=("Helvetica", 14))
        self.configfile.config(state='normal')  # Temporarily set to normal to insert text
        self.configfile.place(x = 0, y = 100, width = 775, height = 250)

        # Add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.configfile.yview)
        scrollbar.place(x=762, y=100, height=250)
        self.configfile.configure(yscrollcommand=scrollbar.set)

        # Define tags for the font color and bold text
        self.configfile.tag_configure("custom_color", foreground="black")
        self.configfile.tag_configure("bold", font=("Helvetica", 14, "bold"))

        # Open and read the file
        filename = "helppagetext"
        try:
            with open(filename, 'r') as f:
                content = f.read()
                self.configfile.insert(INSERT, content)
                
                # Making specific text bold
                self.configfile.tag_add("bold", "1.0", "1.end")
                self.configfile.tag_add("bold", "2.0", "2.9")
                self.configfile.tag_add("bold", "3.0", "3.7")
                self.configfile.tag_add("bold", "5.0", "5.9")
                self.configfile.tag_add("bold", "6.0", "6.7")
                self.configfile.tag_add("bold", "8.0", "8.9")
                self.configfile.tag_add("bold", "9.0", "9.7")
                self.configfile.tag_add("bold", "11.0", "11.9")
                self.configfile.tag_add("bold", "12.0", "12.7")
                self.configfile.tag_add("bold", "14.0", "14.end")
                self.configfile.tag_add("bold", "15.0", "15.9")
                self.configfile.tag_add("bold", "16.0", "16.7")
                self.configfile.tag_add("bold", "18.0", "18.9")
                self.configfile.tag_add("bold", "19.0", "19.7")
                self.configfile.tag_add("bold", "21.0", "21.9")
                self.configfile.tag_add("bold", "22.0", "22.7")
                self.configfile.tag_add("bold", "24.0", "24.9")
                self.configfile.tag_add("bold", "25.0", "25.7")
                self.configfile.tag_add("bold", "27.0", "27.9")
                self.configfile.tag_add("bold", "28.0", "28.7")
                self.configfile.tag_add("bold", "30.0", "30.9")
                self.configfile.tag_add("bold", "31.0", "31.7")
                
                # Apply custom color to the entire content
                self.configfile.tag_add("custom_color", "1.0", "end")
        except FileNotFoundError:
            self.configfile.insert(INSERT, f"Error: File '{filename}' not found.")
        
        self.configfile.config(state='disabled')  # Make the Text widget read-only

        # Load and display image
        image_path = "helppagepic.jpg"
        image = Image.open(image_path)
        resize_image = image.resize((700, 300))
        img = ImageTk.PhotoImage(resize_image)

        image_label = tk.Label(self.main_frame, image=img)
        image_label.image = img 
        image_label.place(x = 30, y = 370)

    def display_profile(self):
        self.clear_main_area()
        if 'first_name' in self.user_info:
            profile_frame = tk.Frame(self.main_frame, bg="oldlace")
            profile_frame.place(x=240, y=45)  # Position the frame at x=250, y=60

            title_label = tk.Label(profile_frame, text="Profile Information", font=("Helvetica", 24, "bold"), bg="oldlace", fg="black")
            title_label.grid(row=0, column=0, columnspan=2, pady=(5, 20))

            labels = ["First Name:", "Username:", "Date of Birth:", "Password:"]
            values = [self.user_info['first_name'], self.user_info['username'], self.user_info['date_of_birth'], self.user_info['password']]

            for i, (label_text, value_text) in enumerate(zip(labels, values)):
                label = tk.Label(profile_frame, text=label_text, font=("Helvetica", 18, "bold"), bg="oldlace", fg="black", anchor="w")
                label.grid(row=i+1, column=0, sticky="w", padx=(0, 20), pady=5)
                value = tk.Label(profile_frame, text=value_text, font=("Helvetica", 18), bg="oldlace", fg="black", anchor="w")
                value.grid(row=i+1, column=1, sticky="w", pady=5)
        else:
            label = tk.Label(self.main_frame, text="Profile information not available", font=("Helvetica", 16), fg="black", bg="oldlace")
            label.place(x=250, y=60)  # Position the label at x=250, y=60

        # Label saying 'quiz results:'
        quiz_label = tk.Label(self.main_frame, text="Quiz Results:", font=("Helvetica", 18, "bold"), fg="black", bg="oldlace")
        quiz_label.place(x=295, y=280)

        # Create a Text widget to display file contents
        text_widget = tk.Text(self.main_frame, wrap="word", font=("Helvetica", 14, "bold"), bg="oldlace", bd=0, fg="black", width=60, height=17)
        text_widget.place(x=140, y=320, width=485, height=280)

        # Add the code to display the file content below the profile information
        file_path = f"{self.user_info['username']}.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()[5:]  # Skip the first 5 lines
                content = ''.join(lines)
                text_widget.insert(tk.END, content)
                text_widget.tag_configure('bold', font=("Helvetica", 14, "bold"))

                # Apply the bold tag to "Quiz scores:"
                start_idx = 1.0
                while True:
                    start_idx = text_widget.search("Quiz scores:", start_idx, tk.END)
                    if not start_idx:
                        break
                    end_idx = f"{start_idx}+{len('Quiz scores:')}c"
                    text_widget.tag_add('bold', start_idx, end_idx)
                    start_idx = end_idx
        else:
            no_file_label = tk.Label(self.main_frame, text="File not found", font=("Helvetica", 16), fg="black", bg="oldlace")
            no_file_label.place(x=250, y=250)  # Position the label at x=250, y=250

        text_widget.config(state=tk.DISABLED)

        # Add scrollbar
        scrollbar1 = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=text_widget.yview)
        scrollbar1.place(x=615, y=320, height=280)
        text_widget.configure(yscrollcommand=scrollbar1.set)

    def step1_open_quiz_window(self):
        popup_q1 = tk.Toplevel()
        popup_q1.title("QUIZ")
        popup_q1.resizable(False, False)
        popup_q1.attributes('-topmost', True)  # keep window on top

        # Calculate center position
        window_width = 1050
        window_height = 650
        screen_width = popup_q1.winfo_screenwidth()
        screen_height = popup_q1.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 4

        # Set window geometry
        popup_q1.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        result = messagebox.askquestion("Option", "Do you want a randomised order of the questions, or the original order?\n(Yes for randomised, No for original)")

        if result == 'yes':
            R_Quiz(popup_q1, self.user_info)
        else:
            Quiz(popup_q1, self.user_info)

root = tk.Tk()
app = MainWindow(root)
root.mainloop()