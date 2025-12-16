from survey import AnonymousSurvey
#define a question , and make a survey

question = 'what language did you first learn to speak'
language_survey =AnonymousSurvey(question)

language_survey.show_questiion()
print("enter 'q at any time to quit")
while True:
    response = input("language:")
    if response =='q':
        break
    language_survey.store_response(response)

print("\n thank you to everyone who participated in the s")
language_survey.show_result()