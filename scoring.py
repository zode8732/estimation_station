import math as m

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