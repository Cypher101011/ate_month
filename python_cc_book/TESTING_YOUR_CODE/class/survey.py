class AnonymousSurvey:
    def __init__(self,question):
        self.question=question
        self.responses=[]
    
    def show_questiion(self):
        print(self.question)
    
    def store_response(self,new_responese):
        self.responses.append(new_responese)
    
    def show_result(self):
        print("survey results:")
        for response in self.responses:
            print(f" - {response}")
