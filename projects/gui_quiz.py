import tkinter as tk
from quiz_game import Game
class Gui_quiz:
    def __init__(self,questions):
        self.newGame=Game(questions)
        self.root = tk.Tk()
        self.root.title("Quiz Game")

        # set widow size here
        self.root.geometry("400x300")

        # create lable here
        self.label=tk.Label(self.root,text="welcome to the quiz game")
        self.label.pack()


        # create entry box heare
        self.entry=tk.Entry(self.root)
        self.entry.pack()



        # create button heare
        self.button =tk.Button(self.root,text="start Quiz",command=self.start_quiz)
        self.button.pack()

        # submit button
        self.submit_button=tk.Button(self.root,text="submit",command=self.check_answer)
        self.submit_button.pack()

        self.submit_view_score=tk.Button(self.root,text='view score',command=self.view_score)
    def start_quiz(self):
        print("quiz started")
        self.index=0
        question=list(self.newGame.questions.keys())[self.index]
        self.label.config(text=question)
        self.entry.delete(0,tk.END)
       
    def check_answer(self):
        user_answer = self.entry.get()

        correct_answer = list(self.newGame.questions.values())[self.index]

        if user_answer.lower() == correct_answer.lower():
            self.newGame.score += 10

        # Move to next question
        self.index += 1

        # If more questions left → show next question
        if self.index < len(self.newGame.questions):
            next_q = list(self.newGame.questions.keys())[self.index]
            self.label.config(text=next_q)
            self.entry.delete(0, tk.END)
        else:
            # No more questions → show score
            self.label.config(text=f"Quiz Finished! Score: {self.newGame.score}")
            self.entry.delete(0, tk.END)

if __name__ == "__main__":

    questions={
        "CPU stands for":"central processing unit",
        "father of computer":"charls babage",
        "creater of linux":"linux torwarld"
    }
    Gui_quiz(questions)      # create the GUI object
    tk.mainloop()   # start the tkinter event loop

