import json
import random as rnd
import math as m

global correct_answer
correct_answer = 0
global score
score = 0

def question_loop():
    question__number = rnd.randint(0, len(questions) - 1)
    expected_answer = questions[question__number]["answer"]
    answer = int(input(questions[question__number]["question"] + " : "))
    global score
    if answer == expected_answer:
        print("correct answer")
        global correct_answer
        correct_answer += 1
        
        score += 1000
    else:
        print("wrong answer")
        temp_score = abs(score - expected_answer)
        temp_score = 10 *m.log10(temp_score)
        score += 1000 - temp_score

print("started game")
with open("data/questions.json", "r") as f:
    data = json.load(f)
questions = data["questions"]
num_questions = int(input("how many questions? "))
for _ in range(num_questions):
    question_loop()

print("gg")
print(f"score: {score}")
print(f"correct answers: {correct_answer}/{num_questions}")