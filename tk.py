from tkinter import *
import tkinter as tk
import sys

# OS-specific ratio to adjust for platform differences
if sys.platform == "darwin":  # macOS
    ratio = 1.375
else:  # windows and linux
    ratio = 1.0

default_font = 'BIZ UDMincho' if sys.platform == "darwin" else 'Sans'
font_size = int(12 * ratio)
exp_input = None
exp_output = None
score = 0

def start_estimation():
    print("Estimation started")
    global points
    points = tk.Label(frame, text="score: "+str(score), font=(default_font, font_size))
    points.pack(anchor='center')
    questioning()

def questioning():
    label.configure(text=change_exp())
    entry.configure(background="grey")
    button.configure(text= "submit", command=submit_ans())


def change_exp():
    global exp_input, exp_output
    from questions import get_questions
    questions = get_questions()
    exp_input = questions[0]["answer"]
    exp_output = questions[0]["question"]
    return exp_output

def submit_ans():
    try:
        input = int(entry.get())
        from scoring import calculate_score
        global score
        score += calculate_score(input, exp_input)
        points.configure(text="score: "+str(score))
    except ValueError:
        print("invalid input. please enter a valid integer.")

root = tk.Tk()
root.title("Estimation Station")
# root.iconphoto(True, tk.PhotoImage(file='temp icon.png'))
root.geometry("512x288")
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(frame, text="EstimationStation", font=(default_font, font_size))
label.pack(anchor='center')
entry = tk.Entry(frame, font=(default_font, font_size))
entry.pack(anchor='center')
button = tk.Button(frame, text="click to start", command=start_estimation, font=(default_font, font_size))
button.pack(anchor='center')
points = None

root.mainloop()