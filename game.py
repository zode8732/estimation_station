import json
import random as rnd
import math as m
import time
import threading

from questions import get_questions
from scoring import calculate_score
from statistics import print_stats

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

correct_answer = 0
score = 0
results = []


questions = get_questions()
num_questions = int(input("how many questions? "))
for _ in range(num_questions):
    question_loop()

print_stats(score, correct_answer, num_questions)