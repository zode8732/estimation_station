from tkinter import *
import tkinter as tk

default_font = 'AppleSystemUIFont'

def start_estimation():
    print("Estimation started")


root = tk.Tk()
root.title("Estimation Station")
root.geometry("1200x900")
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(frame, text="Hello World", font=(default_font))
label.pack()
button = tk.Button(frame, text="click here", command=start_estimation, anchor='center', font=(default_font))
button.pack()
entry = tk.Entry(frame, placeholder="hello")
entry.pack(anchor='center')

root.mainloop()

