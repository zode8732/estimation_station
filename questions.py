import json

def get_questions():
    with open("data/questions.json", "r") as f:
        data = json.load(f)
    return data["questions"]