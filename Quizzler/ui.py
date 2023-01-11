from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, font=('ariel', 20))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=400, width=400, bg='white')
        self.question = self.canvas.create_text(200, 200, text="question", font=('ariel', 20, 'italic'), width=350)
        self.canvas.grid(row=1, column=0, columnspan=2)

        right = PhotoImage(file='./images/true.png')
        self.right_button = Button(image=right, borderwidth=0, command=self.right_clicked)
        self.right_button.config(padx=50, pady=50, bg=THEME_COLOR)
        self.right_button.grid(row=2, column=0)

        wrong = PhotoImage(file='./images/false.png')
        self.wrong_button = Button(image=wrong, borderwidth=0, command=self.wrong_clicked)
        self.wrong_button.config(padx=30, pady=30, bg=THEME_COLOR)
        self.wrong_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.update_score()
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
        else:
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.question, text="Reached the end of the Questions.")

    def right_clicked(self):
        if self.quiz.check_answer('true'):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.update()
        self.window.after(2000, func=self.next_question())

    def wrong_clicked(self):
        if self.quiz.check_answer('false'):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.update()
        self.window.after(2000, func=self.next_question())

    def update_score(self):
        self.score.config(text=f"Score: {self.quiz.score}")
