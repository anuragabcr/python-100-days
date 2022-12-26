from data import question_data, tdb


class Question:
    def __init__(self, ques, ans):
        self.ques = ques
        self.ans = ans


class QuizBrain:
    def __init__(self, ques_list):
        self.ques_no = 0
        self.ques_list = ques_list
        self.score = 0

    def has_ques(self):
        return self.ques_no < len(self.ques_list)

    def next_ques(self):
        question = self.ques_list[self.ques_no]
        self.ques_no += 1
        ans = input(f"Q.{self.ques_no}> {question.ques}? (true/false): ")
        if ans.lower() == question.ans.lower():
            print("Right answer...")
            self.score += 1
        else:
            print("Wrong answer.")
            print("Right answer is ", question.ans)
        print(f"Your current score is {self.score}/{self.ques_no}")


# for static questions
ques_bank = []
for item in question_data:
    ques_bank.append(Question(item['text'], item['answer']))

# for dynamic Trivia DB questions
tdb_ques = []
for item in tdb:
    tdb_ques.append(Question(item['question'], item['correct_answer']))

quiz = QuizBrain(tdb_ques)
while quiz.has_ques():
    quiz.next_ques()