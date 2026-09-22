import json
import random as rnd
import math as m

correct_answer = 0
score = 0
results = []

def calculate_score(answer, expected_answer):
    if answer == expected_answer:
        print("correct answer")
        return 1000
    else:
        print("wrong answer")
        if answer == 0 or expected_answer == 0:
            temp_score = 999
        else:
            temp_score = 200 * abs(m.log2(abs(answer)) - m.log2(abs(expected_answer)))
            if temp_score > 1000:
                temp_score = 999
        print(f"added score: {1000 - temp_score}")
        return 1000 - temp_score

def question_loop():
    question__number = rnd.randint(0, len(questions) - 1)
    expected_answer = questions[question__number]["answer"]
    answer = int(input(questions[question__number]["question"] + " : "))
    global score
    global results
    points = calculate_score(answer, expected_answer)
    score += points
    results.append((answer, expected_answer, points))
    global correct_answer
    if answer == expected_answer:
        correct_answer += 1

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

# done