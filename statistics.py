def print_stats(score, correct_answer, num_questions):
    print(f"score: {score}")
    print(f"correct answers: {correct_answer}/{num_questions}")
    print(f"avg score: {score/num_questions if num_questions > 0 else 0}")