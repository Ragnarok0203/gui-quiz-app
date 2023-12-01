from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Some Questions",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        falseImage = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=falseImage, highlightthickness=0, command=self.false_ans)
        self.falseButton.grid(column=0, row=2)

        trueImage = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=trueImage, highlightthickness=0, command=self.true_ans)
        self.trueButton.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():

            self.label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number + 1}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz")
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")

    def false_ans(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def true_ans(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
