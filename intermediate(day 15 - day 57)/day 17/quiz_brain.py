class QuizBrain:
    def __init__(self, ques_list):
        self.ques_number = 0
        self.ques_score = 0
        self.question_list = ques_list

    def end_game(self):
        if self.ques_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.ques_number]
        self.ques_number += 1
        user_answer = input(
            f"Q{self.ques_number}: {current_question.text}? (True or False)"
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.ques_score += 1
            print("You got it right!!!!")
        else:
            print("That's wrong!!!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your score is: {self.ques_score}/{self.ques_number}")
