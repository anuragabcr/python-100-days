import requests
import html

from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

response = requests.get(url="https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean")
response.raise_for_status()
results = response.json()['results']
questions = [Question(q_text=html.unescape(result['question']), q_answer=result['correct_answer']) for result in results]

quiz = QuizBrain(questions)
quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
