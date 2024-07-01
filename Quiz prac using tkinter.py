# # # Quiz

# # #import everything from tkinter and import messagebox as mb from tkinter
# # from tkinter import *
# # from tkinter import messagebox as mb
# # import tkinter as tk
# # import tkinter

# # # data of questions and answers
# # data = {
# #   "question": [
# #     "Q1. question1",
# #     "Q2. question2",
# #     "Q3. question3",
# #     "Q4.question4"
# #   ],
# #   "answer": [
# #     1,
# #     2,
# #     3,
# #     2
# #   ],
# #   "options": [

# #     ["answer1",
# #       "answer2",
# #       "answer3",
# #       "answer4"
# #     ],
# #     ["answer1",
# #       "answer2",
# #       "answer3",
# #       "answer4"
# #     ],
# #     ["answer1",
# #       "answer2",
# #       "answer3",
# #       "answer4"
# #     ],
# #     ["answer1",
# #       "answer2",
# #       "answer3",
# #       "answer4"
# #     ]
# #   ]
# # }

# # # Let's create the Tkinter window
# # class signin:
# # 	# Let's create the Tkinter window
# # 	window = tkinter.Tk()
# # 	window.geometry("300x300")
# # 	window.title("Signing in")

# # 	# You will create two text labels namely 'username' and 'password' and and two input labels for them
# # 	tkinter.Label(window, text = "Create an account or sign in:").grid(row = 0)
# # 	tkinter.Label(window, text = "Username").grid(row = 1, column = 0) #'username' is placed on position 00 (row - 0 and column - 0)
# # 	# 'Entry' class is used to display the input-field for 'username' text label
# # 	tkinter.Entry(window).grid(row = 1, column = 0) # first input-field is placed on position 01 (row - 0 and column - 1)
# # 	tkinter.Label(window, text = "Password").grid(row = 2, column = 0) #'password' is placed on position 10 (row - 1 and column - 0)
# # 	tkinter.Entry(window).grid(row = 2, column = 0) #second input-field is placed on position 11 (row - 1 and column - 1)

# # 	tkinter.Label(window, text = "Or are you an existing user?").place(x = 2, y = 80)
# # 	var1 = IntVar()
# # 	Checkbutton(window, text='yes', variable=var1).place(x = 2, y = 100)

# # 	# Create Object  
# # 	btn = tkinter.Button(window, text = 'Done', command = window.destroy) 
# # 	btn.place(x=250,y=265)                      
	
# # 	window.mainloop()   

# # class questions:
# # 	newwindow = tkinter.Tk()
# # 	newwindow.geometry("300x300")
# # 	newwindow.title("Questions Page 1")

# # 	tkinter.Label(newwindow, text = "What is your name:").grid(row = 5)
# # 	tkinter.Entry(newwindow).place(x = 2, y = 40)

# # 	tkinter.Label(newwindow, text = "What is your birthdate:").place(x = 0, y = 150)

# # 	btn = tkinter.Button(newwindow, text = 'Done', command = newwindow.destroy) 
# # 	btn.place(x=250,y=250)   

# # 	mainloop()

# # #class to define the components of the GUI
# # class Quiz:
# # 	# This is the first method which is called when a
# # 	# new object of the class is initialized. This method
# # 	# sets the question count to 0. and initialize all the
# # 	# other methoods to display the content and make all the
# # 	# functionalities available
# # 	def __init__(self):
		
# # 		# set question number to 0
# # 		self.q_no=0
		
# # 		# assigns ques to the display_question function to update later.
# # 		self.display_title()
# # 		self.display_question()
		
# # 		# opt_selected holds an integer value which is used for
# # 		# selected option in a question.
# # 		self.opt_selected=IntVar()
		
# # 		# displaying radio button for the current question and used to
# # 		# display options for the current question
# # 		self.opts=self.radio_buttons()
		
# # 		# display options for the current question
# # 		self.display_options()
		
# # 		# displays the button for next and exit.
# # 		self.buttons()
		
# # 		# no of questions
# # 		self.data_size=len(question)
		
# # 		# keep a counter of correct answers
# # 		self.correct=0


# # 	# This method is used to display the result
# # 	# It counts the number of correct and wrong answers
# # 	# and then display them at the end as a message Box
# # 	def display_result(self):
		
# # 		# calculates the wrong count
# # 		wrong_count = self.data_size - self.correct
# # 		correct = f"Correct: {self.correct}"
# # 		wrong = f"Wrong: {wrong_count}"
		
# # 		# calcultaes the percentage of correct answers
# # 		score = int(self.correct / self.data_size * 100)
# # 		result = f"Score: {score}%"
		
# # 		# Shows a message box to display the result
# # 		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


# # 	# This method checks the Answer after we click on Next.
# # 	def check_ans(self, q_no):
		
# # 		# checks for if the selected option is correct
# # 		if self.opt_selected.get() == answer[q_no]:
# # 			# if the option is correct it return true
# # 			return True

# # 	# This method is used to check the answer of the
# # 	# current question by calling the check_ans and question no.
# # 	# if the question is correct it increases the count by 1
# # 	# and then increase the question number by 1. If it is last
# # 	# question then it calls display result to show the message box.
# # 	# otherwise shows next question.
# # 	def next_btn(self):
		
# # 		# Check if the answer is correct
# # 		if self.check_ans(self.q_no):
			
# # 			# if the answer is correct it increments the correct by 1
# # 			self.correct += 1
		
# # 		# Moves to next Question by incrementing the q_no counter
# # 		self.q_no += 1
		
# # 		# checks if the q_no size is equal to the data size
# # 		if self.q_no==self.data_size:
			
# # 			# if it is correct then it displays the score
# # 			self.display_result()
			
# # 			# destroys the GUI
# # 			gui.destroy()
# # 		else:
# # 			# shows the next question
# # 			self.display_question()
# # 			self.display_options()


# # 	# This method shows the two buttons on the screen.
# # 	# The first one is the next_button which moves to next question
# # 	# It has properties like what text it shows the functionality,
# # 	# size, color, and property of text displayed on button. Then it
# # 	# mentions where to place the button on the screen. The second
# # 	# button is the exit button which is used to close the GUI without
# # 	# completing the quiz.
# # 	def buttons(self):
		
# # 		# The first button is the Next button to move to the
# # 		# next Question
# # 		next_button = Button(gui, text="Next",command=self.next_btn,
# # 		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		
# # 		# placing the button on the screen
# # 		next_button.place(x=350,y=380)
		
# # 		# This is the second button which is used to Quit the GUI
# # 		quit_button = Button(gui, text="Leave", command=gui.destroy,
# # 		width=5,bg="black", fg="white",font=("ariel",16," bold"))
		
# # 		# placing the Quit button on the screen
# # 		quit_button.place(x=700,y=50)


# # 	# This method deselect the radio button on the screen
# # 	# Then it is used to display the options available for the current
# # 	# question which we obtain through the question number and Updates
# # 	# each of the options for the current question of the radio button.
# # 	def display_options(self):
# # 		val=0
		
# # 		# deselecting the options
# # 		self.opt_selected.set(0)
		
# # 		# looping over the options to be displayed for the
# # 		# text of the radio buttons.
# # 		for option in options[self.q_no]:
# # 			self.opts[val]['text']=option
# # 			val+=1


# # 	# This method shows the current Question on the screen
# # 	def display_question(self):
		
# # 		# setting the Question properties
# # 		q_no = Label(gui, text=question[self.q_no], width=60,
# # 		font = ( 'ariel' ,16, 'bold' ), anchor= 'w' )
		
# # 		#placing the option on the screen
# # 		q_no.place(x = 70, y = 100)


# # 	# This method is used to Display Title
# # 	def display_title(self):
		
# # 		# The title to be shown
# # 		title = Label(gui, text="Overconsumption Quiz",
# # 		width = 50, bg = "purple",fg = "white", font = ("ariel", 20, "bold"))
		
# # 		# place of the title
# # 		title.place(x=0, y=2)


# # 	# This method shows the radio buttons to select the Question
# # 	# on the screen at the specified position. It also returns a
# # 	# list of radio button which are later used to add the options to
# # 	# them.
# # 	def radio_buttons(self):
		
# # 		# initialize the list with an empty list of options
# # 		q_list = []
		
# # 		# position of the first option
# # 		y_pos = 150
		
# # 		# adding the options to the list
# # 		while len(q_list) < 4:
			
# # 			# setting the radio button properties
# # 			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
# # 			value = len(q_list)+1,font = ("ariel",14))
			
# # 			# adding the button to the list
# # 			q_list.append(radio_btn)
			
# # 			# placing the button
# # 			radio_btn.place(x = 100, y = y_pos)
			
# # 			# incrementing the y-axis position by 40
# # 			y_pos += 40
		
# # 		# return the radio buttons
# # 		return q_list

# # # Create a GUI Window
# # gui = Tk()

# # # set the size of the GUI Window
# # gui.geometry("800x450")


# # # set the title of the Window
# # gui.title("Overconsumption Quiz")

# # # set the question, options, and answer
# # question = (data['question'])
# # options = (data['options'])
# # answer = (data[ 'answer'])

# # # create an object of the Quiz Class.
# # quiz = Quiz()

# # # Start the GUI
# # gui.mainloop()


# #import everything from tkinter and import messagebox as mb from tkinter
# from tkinter import *
# from tkinter import messagebox as mb
# import tkinter as tk
# import tkinter

# # data of questions and answers
# data = {
#     "question": [
#         "Q1. question1",
#         "Q2. question2",
#         "Q3. question3",
#         "Q4. question4"
#     ],
#     "answer": [
#         1,
#         2,
#         3,
#         2
#     ],
#     "options": [
#         ["answer1", "answer2", "answer3", "answer4"],
#         ["answer1", "answer2", "answer3", "answer4"],
#         ["answer1", "answer2", "answer3", "answer4"],
#         ["answer1", "answer2", "answer3", "answer4"]
#     ]
# }

# # Class to define the components of the GUI
# class Quiz:
#     def __init__(self, root):
#         self.root = root
#         self.q_no = 0
#         self.correct = 0
#         self.opt_selected = IntVar()
        
#         self.display_title()
#         self.display_question()
#         self.opts = self.radio_buttons()
#         self.display_options()
#         self.buttons()
#         self.data_size = len(data['question'])

#     def display_result(self):
#         wrong_count = self.data_size - self.correct
#         correct = f"Correct: {self.correct}"
#         wrong = f"Wrong: {wrong_count}"
#         score = int(self.correct / self.data_size * 100)
#         result = f"Score: {score}%"
#         mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

#     def check_ans(self, q_no):
#         return self.opt_selected.get() == data['answer'][q_no]

#     def next_btn(self):
#         if self.check_ans(self.q_no):
#             self.correct += 1
#         self.q_no += 1
#         if self.q_no == self.data_size:
#             self.display_result()
#             self.root.destroy()
#         else:
#             self.display_question()
#             self.display_options()

#     def buttons(self):
#         next_button = Button(self.root, text="Next", command=self.next_btn, width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
#         next_button.place(x=350, y=380)
#         quit_button = Button(self.root, text="Leave", command=self.root.destroy, width=5, bg="black", fg="white", font=("ariel", 16, "bold"))
#         quit_button.place(x=700, y=50)

#     def display_options(self):
#         self.opt_selected.set(0)
#         for val, option in enumerate(data['options'][self.q_no]):
#             self.opts[val]['text'] = option

#     def display_question(self):
#         q_no = Label(self.root, text=data['question'][self.q_no], width=60, font=('ariel', 16, 'bold'), anchor='w')
#         q_no.place(x=70, y=100)

#     def display_title(self):
#         title = Label(self.root, text="Overconsumption Quiz", width=50, bg="purple", fg="white", font=("ariel", 20, "bold"))
#         title.place(x=0, y=2)

#     def radio_buttons(self):
#         q_list = []
#         y_pos = 150
#         while len(q_list) < 4:
#             radio_btn = Radiobutton(self.root, text=" ", variable=self.opt_selected, value=len(q_list) + 1, font=("ariel", 14))
#             q_list.append(radio_btn)
#             radio_btn.place(x=100, y=y_pos)
#             y_pos += 40
#         return q_list

# def open_quiz_window(self):
#     popup_q = tk.Toplevel()
#     popup_q.title("QUIZ")
#     popup_q.resizable(False, False)

#     window_width = 1050
#     window_height = 700
#     screen_width = popup_q.winfo_screenwidth()
#     screen_height = popup_q.winfo_screenheight()
#     x_position = (screen_width - window_width) // 2
#     y_position = (screen_height - window_height) // 4
#     popup_q.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

#     label_q = tk.Label(popup_q, text="QUIZ", font=("Helvetica", 13))
#     label_q.pack()

#     # Embed the quiz in the popup window
#     Quiz(popup_q)

# # Create a GUI Window
# root = Tk()
# root.geometry("300x200")
# root.title("Main Window")

# # Main window button to open the quiz window
# main_button = Button(root, text="Open Quiz", command=lambda: open_quiz_window(root))
# main_button.pack()

# # Start the GUI
# root.mainloop()
# Importing necessary libraries
from tkinter import *
from tkinter import messagebox as mb
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

# Data of questions and answers
data = {
    "question": [
        "Q1. question1",
        "Q2. question2",
        "Q3. question3",
        "Q4. question4"
    ],
    "answer": [
        1,
        2,
        3,
        2
    ],
    "options": [
        ["answer1", "answer2", "answer3", "answer4"],
        ["answer1", "answer2", "answer3", "answer4"],
        ["answer1", "answer2", "answer3", "answer4"],
        ["answer1", "answer2", "answer3", "answer4"]
    ]
}

# Class to define the components of the GUI
class Quiz:
    def __init__(self, root):
        self.root = root
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(data['question'])
        self.correct = 0

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        if self.opt_selected.get() == data['answer'][q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no == self.data_size:
            self.display_result()
            self.root.destroy()
        else:
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(self.root, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)
        quit_button = Button(self.root, text="Leave", command=self.root.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, "bold"))
        quit_button.place(x=700, y=50)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in data['options'][self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        q_no = Label(self.root, text=data['question'][self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')
        q_no.place(x=70, y=100)

    def display_title(self):
        title = Label(self.root, text="Overconsumption Quiz",
                      width=50, bg="purple", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(self.root, text=" ", variable=self.opt_selected,
                                    value=len(q_list)+1, font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list

class quiz_page():
    def __init__(self):
        self.quizpage = tk.Tk()
        self.quizpage.title("Overconsumption Quiz")
        self.quizpage.configure(bg="oldlace")
        self.quizpage.resizable(False, False)

        window_width = 1200
        window_height = 750
        screen_width = self.quizpage.winfo_screenwidth()
        screen_height = self.quizpage.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 4

        self.quizpage.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        class Boldtitle(tk.Label):
            def __init__(self, master=None, **kwargs):
                super().__init__(master, **kwargs)
                bold_font = font.Font(self, self.cget("font"))
                bold_font.configure(weight="bold")
                self.configure(font=bold_font)

        title = Boldtitle(self.quizpage, text="OVERCONSUMPTION QUIZ",
                          font=("Helvetica", 40), background="oldlace",
                          foreground="black")
        title.pack(pady=30)

        profile_button = tk.Button(self.quizpage, text='PROFILE',
                                   width=10, height=2, fg="green",
                                   bg="white", command=self.show_profile)
        profile_button.place(x=1100, y=35)

        exit_button = tk.Button(self.quizpage, text='EXIT', width=10,
                                height=2, fg="white", bg="black",
                                command=self.check_exit)
        exit_button.place(x=1100, y=685)

        quiz_button = tk.Button(self.quizpage, text='QUIZ', width=10,
                                height=2, fg="green", bg="white",
                                command=self.open_quiz_window)
        quiz_button.place(x=1100, y=635)

        image = Image.open("picture1.png")
        resize_image = image.resize((650, 500))
        img = ImageTk.PhotoImage(resize_image)

        label1 = tk.Label(image=img)
        label1.image = img
        label1.place(x=270, y=220)

        program_text = Boldtitle(self.quizpage, text="This is the quiz page.\n"
                                 "This program is to teach and test you on "
                                 "your knowledge about \nover-consumption."
                                 "Click the quiz button to do the quiz.",
                                 font=("Helvetica", 18),
                                 foreground="black", background="oldlace")
        program_text.place(x=290, y=135)

        self.create_sidebar()
        self.quizpage.mainloop()

    # def open_home_page(self):
    #     self.quizpage.destroy()
    #     HomePage()

    # def open_ap_page(self):
    #     self.quizpage.destroy()
    #     ap_page()

    # def open_ss_page(self):
    #     self.quizpage.destroy()
    #     ss_page()

    # def open_about_page(self):
    #     self.quizpage.destroy()
    #     about_page()

    # def open_help_page(self):
    #     self.quizpage.destroy()
        # help_page()

    def create_sidebar(self):
        buttons = [
            ("HOME", self.quiz_popup),
            ("QUIZ", self.quiz_popup),
            ("SUCCESS\nSTORIES", self.quiz_popup),
            ("ALTERNATIVE\nPRODUCTS", self.quiz_popup),
            ("ABOUT", self.quiz_popup),
            ("HELP", self.quiz_popup)
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(self.quizpage, text=text, width=10, height=2,
                            fg="green", bg="white", command=command)
            btn.place(x=50, y=50 + i * 100)

    def check_exit(self):
        popup_e = tk.Toplevel()
        popup_e.title("Exit")
        popup_e.geometry("190x100")
        popup_e.resizable(False, False)

        label = tk.Label(popup_e, text="Are you sure you want\n to exit now?",
                         font=("Helvetica", 13))
        label.pack()

        yes_button = tk.Button(popup_e, text="Yes",
                               command=self.quizpage.destroy)
        yes_button.place(x=60, y=65)

        no_button = tk.Button(popup_e, text="No", command=popup_e.destroy)
        no_button.place(x=100, y=65)

    def open_quiz_window(self):
        quiz_window = Toplevel()
        quiz_window.title("QUIZ")
        quiz_window.resizable(False, False)

        window_width = 1050
        window_height = 700
        screen_width = quiz_window.winfo_screenwidth()
        screen_height = quiz_window.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 4

        quiz_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        Quiz(quiz_window)

    def show_profile(self):
        profile_popup = tk.Toplevel()
        profile_popup.title("User Profile")
        profile_popup.geometry("300x200")
        profile_popup.resizable(False, False)

        label = tk.Label(profile_popup, text=f"First Name: {self.firstname}\nUsername: {self.username}\nBirthdate: {self.birthdate.strftime('%d/%m/%Y')}", font=("Helvetica", 13))
        label.pack(pady=20)

        close_button = tk.Button(profile_popup, text="Close", command=profile_popup.destroy)
        close_button.pack(pady=10)

    def open_popup(self):
        popup = tk.Toplevel()
        popup.title("Warning")
        popup.geometry("250x130")
        popup.resizable(False, False)

        label = tk.Label(popup, text="Feature not implemented yet.")
        label.place(x=30, y=20)

        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.place(x=95, y=90)

    def quiz_popup(self):
        popup = tk.Toplevel()
        popup.title("Warning")
        popup.geometry("250x130")
        popup.resizable(False, False)

        label = tk.Label(popup, text="You are on the quiz page.")
        label.place(x=30, y=20)

        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.place(x=95, y=90)


# Initialize the main application window
def main():
    app = quiz_page()


# Running the main application window
if __name__ == "__main__":
    main()
