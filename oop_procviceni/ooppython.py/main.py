from data import question_data
from question_model import Kviz
from quiz_brain import QuizBrain

question_list =[]

for one_question in question_data:
    questiont =one_question["text"]
    questiona = one_question["answer"]
    new_question = Kviz(questiont,questiona)
    question_list.append(new_question)

quiz = QuizBrain(question_list)
while quiz.has_question() == True:
    quiz.next_question()
print(f"Konec kvízu")
print(f"Celkové skore je: {quiz.score} /{quiz.question_number}")