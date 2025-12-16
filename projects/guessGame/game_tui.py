import random

class Guess:
    def __init__(self):
        self.secret=random.randint(1,100)
   
    def guess(self):
        attempts=0
        while True:
        
            try:
                player =int(input("Guess the number 1 to 100 : "))
               
            except ValueError:
                print('input error wrong input')
                continue
            attempts+=1
            if self.secret>player:
                print("too low")
            elif self.secret<player:
                print("too high")
            else:
                return f'you guess correct write number ("{self.secret}") in {attempts} attempts'
                
game=Guess()

print(game.guess())