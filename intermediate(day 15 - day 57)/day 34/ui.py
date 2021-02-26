from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.win = Tk()
        self.win.title("Qizzler")
        self.win.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        self.quiz_text = self.canvas.create_text(
            150, 125, width=250, text="", font=("Arial", 15, "italic")
        )
        self.image1 = PhotoImage(file="images/true.png")
        self.image2 = PhotoImage(file="images/false.png")
        self.but_true = Button(
            image=self.image1, highlightthickness=0, command=self.true
        )
        self.but_true.grid(column=1, row=3)
        self.but_false = Button(
            image=self.image2, highlightthickness=0, command=self.false
        )
        self.but_false.grid(column=2, row=3)
        self.label = Label(
            text="Score:0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic")
        )
        self.label.grid(column=2, row=1)
        self.next_quest()

        self.win.mainloop()

    def next_quest(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(
                self.quiz_text,
                text=f"You've reached the end of the question list \nYour final score:{self.quiz.score} ",
            )
            self.but_true.config(state="disabled")
            self.but_false.config(state="disabled")

    def false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.quiz.score += 1

        else:
            self.canvas.config(bg="red")
        self.win.after(500, self.next_quest)
