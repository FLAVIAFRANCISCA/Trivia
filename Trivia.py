import random
import tkinter as tk
from tkinter import messagebox

# The questions and answers for each category
questions_answers = {
    'Car Brands': [
        ("Which car brand is known for its luxury vehicles such as the Phantom and the Ghost?", "Rolls Royce"),#change rolls-royce to rolls royce
        ("What car brand's logo features a blue oval with the company name written in white?", "Ford"),
        ("Which Italian car manufacturer produces the 488 and the Portofino models?", "Ferrari")
    ],
    'Celebrities': [
        ("Which actor played the lead role in the movie 'Forrest Gump'?", "Tom Hanks"),
        ("Who is known as the 'Queen of Pop' and has hits like 'Like a Virgin' and 'Vogue'?", "Madonna"),
        ("Which actor portrayed Tony Stark/Iron Man in the Marvel Cinematic Universe?", "Robert Downey Jr.")
    ],
    'Countries': [
        ("What is the largest country in the world by land area?", "Russia"),
        ("Which European country is known for its windmills, tulips, and bicycles?", "Netherlands"),
        ("Which Asian country is famous for its ancient temples like Angkor Wat?", "Cambodia")
    ],
    'Inventors': [
        ("Who is credited with inventing the telephone?", "Alexander Graham Bell"),
        ("Which inventor is known for creating the light bulb?", "Thomas Edison"),
        ("Who invented the World Wide Web?", "Tim Berners-Lee")
    ]
}

# This is the function to show a hint for the current question
def show_hint():
    hint = f"Hint: {correct_answer[0].upper()}"
    messagebox.showinfo("Hint", hint)

# This is the function to validate the user's answer
def check_answer():
    user_answer = entry.get().strip()
    if user_answer.lower() == correct_answer.lower():#compared user answer to full answer because you were only comparing to a single letter
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showerror("Incorrect!", f"Sorry, the correct answer is: {correct_answer}")#removed word indexing when displaying correct answer
    next_question()#this works but i suggest moving it into the differnt conditions


# This is the function to display the next question
def next_question():
    global current_category, current_question, correct_answer
    if len(questions_answers[current_category]) == 0:
        messagebox.showinfo("Game Over", "You have completed all questions in this category!")
        return
    
    current_question, correct_answer = random.choice(questions_answers[current_category])
    label.config(text=current_question)
    entry.delete(0, tk.END)

# This is the function to start the game
def start_game():
    global current_category
    current_category = category_var.get()
    next_question()

# Creating a tkinter window
window = tk.Tk()
window.title("Trivia Game")

# Styling the window
window.geometry("400x400")
window.configure(bg="#f0f0f0")

# Creating a frame for better organization
frame = tk.Frame(window, bg="#f0f0f0")
frame.pack(pady=20)

# Creating widgets
instruction_label = tk.Label(frame, text="Welcome to Trivia!", font=("Helvetica", 18), bg="#f0f0f0")
instruction_label.grid(row=0, column=0, columnspan=2, pady=10)

category_label = tk.Label(frame, text="Choose a category:", font=("Helvetica", 12), bg="#f0f0f0")
category_label.grid(row=1, column=0, padx=10)

category_var = tk.StringVar()
category_var.set('Car Brands')
categories = ['Car Brands', 'Celebrities', 'Countries', 'Inventors']
category_dropdown = tk.OptionMenu(frame, category_var, *categories)
category_dropdown.config(font=("Helvetica", 12))
category_dropdown.grid(row=1, column=1, padx=10)

start_button = tk.Button(frame, text="Start Game", command=start_game, font=("Helvetica", 12))
start_button.grid(row=2, column=0, columnspan=2, pady=10)

label = tk.Label(window, text="", font=("Helvetica", 14), bg="#ffffff", padx=10, pady=10, relief="groove")
label.pack(pady=10, padx=20, fill="both", expand=True)

entry = tk.Entry(window, font=("Helvetica", 12))
entry.pack(pady=10, padx=20, fill="x")

submit_button = tk.Button(window, text="Submit Answer", command=check_answer, font=("Helvetica", 12))
submit_button.pack(pady=10, padx=20, fill="x")

hint_button = tk.Button(window, text="Hint", command=show_hint, font=("Helvetica", 12))
hint_button.pack(pady=10, padx=20, fill="x")

# Run the tkinter event loop
window.mainloop()


# Run the tkinter event loop
window.mainloop()

##