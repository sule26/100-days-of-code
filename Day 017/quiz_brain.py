class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"\nQ.{self.q_number}: {current_question.text}? (True/False): ").capitalize()
        self.check_answer(current_question.answer, user_answer)

    def still_has_question(self):
        return self.q_number < len(self.q_list)

    def check_answer(self, correct_answer, user_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.q_number}.")
