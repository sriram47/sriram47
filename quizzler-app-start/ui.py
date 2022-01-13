from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label()
        self.label.config(text="Score: ", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150
            , 125
            , width=280
            , text="Some question here"
            , fill=THEME_COLOR
            , font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=2, columnspan=2, pady=50)



        right_button_img = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_button_img, highlightthickness=0, command=self.check_user_answer_true)
        self.right_button.grid(column=0, row=4)

        wrong_button_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=self.check_user_answer_false)
        self.wrong_button.grid(column=1, row=4)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.right_button.config(state="active")
            self.wrong_button.config(state="active")
            self.canvas.config(bg="white")
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You have reached the end.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_user_answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        # print(q_answer)

    def check_user_answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        # print(q_answer)

    def give_feedback(self, is_right):
        if is_right:
            # Canvas.itemconfig(canvas, fill="green")
            self.canvas.config(bg="green")
        elif not is_right:
            # Canvas.itemconfig(self.canvas, fill="red")
            self.canvas.config(bg="red")
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
        self.window.after(1000,self.get_next_question)


