import json
import random as rnd
import math as m
import time
import threading

correct_answer = 0
score = 0
results = []

def calculate_score(answer, expected_answer):
    if answer == expected_answer:
        print("correct answer")
        return 1000
    else:
        print("wrong answer")
        if answer == 0 or expected_answer == 0 or answer == -1:
            temp_score = 999
        else:
            temp_score = 200 * abs(m.log2(abs(answer)) - m.log2(abs(expected_answer)))
            if temp_score > 1000:
                temp_score = 999
        print(f"added score: {1000 - temp_score}")
        print(f"percent error: {(answer-expected_answer)/expected_answer*100}%")
        return 1000 - temp_score

def question_loop():
    question__number = rnd.randint(0, len(questions) - 1)
    expected_answer = questions[question__number]["answer"]
    timer = threading.Timer(10.0, lambda: print(" time's up!\nusing -1\npress enter to continue"))
    timer.start()
    answer = int(input(questions[question__number]["question"] + " : "))
    timer.cancel()
    global score
    global results
    points = calculate_score(answer, expected_answer)
    score += points
    results.append((questions[question__number]["question"], answer, expected_answer, points))
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
print(f"avg score: {score/num_questions if num_questions > 0 else 0}")

# done