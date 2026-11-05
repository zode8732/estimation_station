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
    questioning()

def questioning():
    label.config(text="placeholder text")

def get_questions():
    global exp_input, exp_output
    from questions import get_questions
    questions = get_questions()
    exp_input = questions[0]
    exp_output = questions[1]

root = tk.Tk()
root.title("Estimation Station")
# root.iconphoto(True, tk.PhotoImage(file='temp icon.png'))
root.geometry("1200x900")
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(frame, text="Hello World", font=(default_font, font_size))
label.pack()
entry = tk.Entry(frame, font=(default_font, font_size))
entry.pack(anchor='center')
button = tk.Button(frame, text="click here", command=start_estimation, anchor='center', font=(default_font, font_size))
button.pack()

root.mainloop()

