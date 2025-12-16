
class Game:
    def __init__(self,questions,answers=[]):
        self.answers=answers
        self.score=0
        self.questions=questions
    def playing(self):

        for question,ans in self.questions.items():

            answer=input(f"{question.title()}\t: ")
            self.answers.append(answer)
            if answer.lower()==ans.lower():
                self.score+=10
        print(f"your result is {self.score}")

        condition = input("do you want to view your answer as well as correct answers : ")
        if condition.lower()=="yes":
            i=0
            for key,value in self.questions.items():
                print(f"the correct is of question {i+1} {value} and your answer is {answers[i]} ")
                i+=1

