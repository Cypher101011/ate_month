import random
import tkinter as tk
from tkinter import messagebox
class GuessNumber:
    def __init__(self):
        self.secret = random.randint(0, 100)

    def guess(self, player):
        if player == self.secret:
            return "🎉 Correct!"
        elif player > self.secret:
            return "📈 Too high"
        else:
            return "📉 Too low"

class GuessNumberUI:
    def __init__(self,root):
        self.game=GuessNumber()
        root.title("guess the number")
        root.geometry("300x180")

        self.label=tk.Label(root,text="guess a number 1 -100")
        self.label.pack(pady=5)
        
        self.entry=tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root,text="Guess",
        command=self.handle_guess
        )

        self.button.pack(pady=5)
        
        self.result_label=tk.Label(root,text="")
        self.result_label.pack(pady=5)

    def handle_guess(self):
            try:
                value = int(self.entry.get())
                result=self.game.guess(value)
                self.result_label.config(text=result)

                if result =="correct":
                    messagebox.shwinfo("win", "you guess the number")
                    self.button.config(state="disabled")

            except ValueError:
                self.result_label.config(text="invalid number")

if __name__=="__main__":
    root=tk.Tk()
    app=GuessNumberUI(root)
    root.mainloop()