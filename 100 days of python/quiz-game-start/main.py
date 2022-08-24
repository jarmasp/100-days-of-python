from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []

for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

quizz = QuizBrain(questions)

while quizz.still_has_questions:
    quizz.next_question()

print (f'you completed the quizz, your final score was {quizz.score}/{quizz.q_number}')