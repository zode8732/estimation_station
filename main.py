import json
import random as rnd
import math as m

correct_answer = 0
score = 0

def calculate_score(answer, expected_answer):
    global score
    if answer == expected_answer:
        print("correct answer")
        global correct_answer
        correct_answer += 1
        
        score += 1000
    else:
        print("wrong answer")
        temp_score = abs(answer - expected_answer)
        if temp_score == 0:
            quit("score calculation error")
        temp_score = 10 *m.log10(temp_score)
        score += 1000 - temp_score

def question_loop():
    question__number = rnd.randint(0, len(questions) - 1)
    expected_answer = questions[question__number]["answer"]
    answer = int(input(questions[question__number]["question"] + " : "))
    calculate_score(answer, expected_answer)

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