import json
import random as rnd

global correct_answer
correct_answer = 0

def question_loop():
    question__number = rnd.randint(0, len(questions) - 1)
    expected_answer = questions[question__number]["answer"]
    answer = int(input(questions[question__number]["question"] + " : "))
    if answer == expected_answer:
        print("correct answer")
        global correct_answer
        correct_answer += 1
    else:
        print("wrong answer")

print("started game")
with open("data/questions.json", "r") as f:
    data = json.load(f)
questions = data["questions"]
num_questions = int(input("how many questions? "))
for _ in range(num_questions):
    question_loop()

print("gg")
print(f"score: {correct_answer}/{num_questions}")