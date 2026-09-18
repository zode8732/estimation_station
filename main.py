import json
import random as rnd

with open("data/questions.json", "r") as f:
    data = json.load(f)

print("started game")
questions = data["questions"]
question__number = rnd.randint(0, len(questions) - 1)
expected_answer = questions[question__number]["answer"]
answer = input(questions[question__number]["question"] + " : ")

if answer == expected_answer:
    print("correct answer")
else:
    print("wrong answer")