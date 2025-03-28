class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {self.question_list[self.question_number].text} (Trues/False)? :')
        self.check_answer(user_answer, self.question_list[self.question_number].answer)


    def still_has_questions(self):
        if self.question_number < (len(self.question_list)-1):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1


        else:
            print("That's wrong!")
        print(f"the correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

    def final_score(self):
        print("You have completed the quiz")
        print(f"Your final score is {self.score}/{self.question_number}")