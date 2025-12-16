import random 

class Game:
    def __init__(self):
        self.words=['rainbow','computer','science','programing','python','mathematics','player','conditions','reverse',
        'water','board','geeks']
        self.word=random.choice(self.words)

    def play(self):
        while True:
            attempts=1
            player=input(f"enter the words and we check you guess correctly from {self.words} \n \t :")
            if self.word==player:
                print(f"your guess correct in your{attempts} ")
                return
            else:
                print("you geuess incorect try again")
                attempts+=1

game=Game()

game.play()