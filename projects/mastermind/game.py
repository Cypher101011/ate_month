import random

secret_number =str(random.randint(1000,10000))





def game(entry,secret_number):
        tries=0
        # correct_guess=['#','#','#','#']
        while True:
            correct_guess=['#']*4
            for i in range(4):
                if entry[i]==secret_number[i]:
                    correct_guess[i]=entry[i]
            tries+=1
            
            if entry==secret_number:
                return f"you guess number in {tries} tries"
            else:
                print(f"you guess {correct_guess} correctly guess again ")
                entry=input()
            
tries=0
entry=str(input("enter the number "))
if entry==secret_number:
    print( "you are the mastermind you guess number in 1 try")
else:
    game(entry,secret_number)