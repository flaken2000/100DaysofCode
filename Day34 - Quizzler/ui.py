from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler 3000")
        self.window.eval('tk::PlaceWindow . center')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("arial", 8, "normal"))
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question", width=280, fill=THEME_COLOR, font=("arial", 18, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # False Button
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, bg=THEME_COLOR, highlightthickness=0, command=self.false_button)
        self.false_button.grid(column=0, row=2)

        # True Button
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, bg=THEME_COLOR, highlightthickness=0, command=self.true_button)
        self.true_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz!!!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
