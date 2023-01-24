from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"




class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(background=THEME_COLOR, pady=0, padx=20)

        # CANVAS
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.qusetion_text = self.canvas.create_text(150, 125, text="BUTU", anchor="center", font=("Arial", 20, "italic")
                                                     , fill="black", width=280)
        self.canvas.grid(row=2, column=1, columnspan=2)
        # CANVAS TEXT


        # SCORE
        self.score = Label()
        self.score.config(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=2, row=1, padx=50, pady=20)
        # CHECK BUTTON
        self.check_img = PhotoImage(file="images/true.png")
        self.check = Button(image=self.check_img, highlightthickness=0, bd=0, command=self.true_answer)
        self.check.grid(column=2, row=3, pady=50, padx=20)
        # CROSS BUTTON
        self.cross_img = PhotoImage(file="images/false.png")
        self.cross = Button(image=self.cross_img, highlightthickness=0, bd=0, command=self.flase_answer)
        self.cross.grid(column=1, row=3, pady=50, padx=20)


        self.getnext_question()



        self.window.mainloop()

    def getnext_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():

            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.qusetion_text, text= q_text)
        else:
            self.canvas.itemconfig(self.qusetion_text, text= "ENDING")
            self.check.config(state="disabled")
            self.cross.config(state="disabled")


    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.givefeed(is_right)


    def flase_answer(self):
        is_wrong = self.quiz.check_answer("False")
        self.givefeed(is_wrong)

    def givefeed(self, is_right):
        if is_right == True:
            self.canvas.config(background="green")
            # self.canvas.config(background="white")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.getnext_question)





