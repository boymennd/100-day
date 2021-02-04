from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.end_game():
    quiz.next_question()

print(f"You final complete the quiz!!!!!")
print(f"Your final score is: {quiz.ques_score}")
