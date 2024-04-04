import random
import tkinter as tk
from tkinter import messagebox

# The questions and answers for each category
questions_answers = {
    'Cars': [
        ("Which car brand is known for its luxury vehicles such as the Phantom and the Ghost?", "Rolls Royce"),
        ("What car brand's logo features a blue oval with the company name written in white?", "Ford"),
        ("Which Italian car manufacturer produces the 488 and the Portofino models?", "Ferrari"),
        ("What car model is often associated with James Bond?", "Aston Martin"),
        ("What car manufacturer produces the Civic and Accord models?", "Honda"),
        ("What is the name of the luxury division of Toyota?", "Lexus"),
        ("Which car brand uses the slogan “The Ultimate Driving Machine”?", "BMW"),
        ("What is the name of the supercar brand founded by Christian von Koenigsegg?", "Koenigsegg"),
        ("What was the first mass produced car in the world?", "Ford Model T"),
        ("What does SUV stand for in the automotive world?", "Sport Utility Vehicle"),
        ("What is the most popular car color worldwide?", "White"),
        ("What car brand is known for its “Zoom Zoom” marketing slogan?", "Mazda"),
        ("Which car model is often associated with the term “muscle car”?", "Chevrolet Camaro"),
        ("Which electric car company was founded by Elon Musk?", "Tesla"),    
        ("What does MPG stand for when referring to a car's fuel efficiency?", "Miles Per Gallon"),
        ("What car brand is known for its “Twin Turbo” technology?", "Nissan"),
        ("Which automaker introduced the first mass produced hybrid SUV?", "Toyota"),
        ("Which car manufacturer is known for its “Super Cruise” advanced driver-assistance system?", "Cadillac"),
        ("What classic car brand is famous for its split-window Corvette model?", "Chevrolet"),
        ("Which car brand features a logo with four interlocking rings?", "Audi"),
        ("What automaker's logo resembles a silver arrow pointing upward?", "Mercedes-Benz"),
        ("Which automaker is known for its winged emblem featuring a red and blue oval?", "Subaru"),
        ("What car brand's logo is a stylized letter “K” inside a circle?", "Kia"),
        ("What automaker uses a logo that combines the letters “V” and “W” in a blue and silver design?", "Volkswagen"),
    ],
    'Celebrities': [
        ("Which actor played the lead role in the movie 'Forrest Gump'?", "Tom Hanks"),
        ("Who is known as the 'Queen of Pop' and has hits like 'Like a Virgin' and 'Vogue'?", "Madonna"),
        ("Which actor portrayed Tony Stark/Iron Man in the Marvel Cinematic Universe?", "Robert Downey Jr."),
        ("What is Rihanna's real name?", "Robyn Fenty"),
        ("Ariana Grande got her start on what kids TV show?", "Victorious"),
        ("Which pop star is the godmother of both of Elton John's sons?", "Lady Gaga"),
        ("Which artist made history in 2020 as the youngest winner of the Grammys four main categories?", "Billie Eilish"),
        ("Who was the first winner of The Masked Singer?", "T-Pain"),
        ("Who is the oldest Kardashian sister?", "Kourtney"),
        ("Who sings the famous 'All I want for christmas is You?'", "Mariah Carey"),
        ("Which tech entrepreneur named his son X Æ A-12?", "Elon Musk"),
        ("Which artist is known for the moonwalk?", "Michael Jackson"),
        ("Which celebrity stared in Degrassi: The Next Generation?", "Drake"),
        ("Which two Oscar-winning actresses with the same first name co-starred in Cruella?", "Emma Stone and Emma Thompson"),
        ("Who plays James Bond?", "Daniel Craig"),
        ("Angela Bassett was nominated for an Academy Award for Best Actress for her portrayal of which legendary singer?", "Tina Turner"),
        ("Who wrote the 2018 memoir 'Becoming'?", "Michelle Obama"),
        ("Which actor voiced both Darth Vader and The Lion King's Mufasa?", "James Earl Jones"),
        ("What are the names of Kim Kardashian and Kanye West's kids?", "North, Saint, Chicago and Psalm"),
        ("Which actress was nominated for an Academy Award for Best Actress for potraying Tina Turner?", "Angela Bassett"),
        ("Which blonde star and sex symbol was found dead in her L.A. home in 1962?", "Marilyn Monroe"),
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

# Dictionary to store the current level for each category
current_levels = {category: 1 for category in questions_answers.keys()}

# Dictionary to store the answered questions for each category and level
answered_questions = {category: {level: [] for level in range(1, 6)} for category in questions_answers.keys()}

# Function to check if the current level is completed
def is_level_completed(category):
    current_level = current_levels[category]
    answered_count = len(answered_questions[category][current_level])
    return answered_count >= 5

# This is the function to show a hint for the current question
def show_hint():
    hint = f"Hint: {correct_answer[0].upper()}"
    messagebox.showinfo("Hint", hint)

# This is the function to validate the user's answer
def check_answer():
    user_answer = entry.get().strip()
    if user_answer.lower() == correct_answer.lower():
        messagebox.showinfo("Correct!", "Your answer is correct!")
        answered_questions[current_category][current_level].append(current_question)
    else:
        messagebox.showerror("Incorrect!", f"Sorry, the correct answer is: {correct_answer}")
    next_question()

# This is the function to display the next question
def next_question():
    global current_category, current_question, correct_answer, current_level
    if is_level_completed(current_category):
        messagebox.showinfo("Level Completed", "Congratulations! You have completed this level.")
        current_levels[current_category] += 1
        if is_level_completed(current_category):
            messagebox.showinfo("Category Completed", "Congratulations! You have completed all levels in this category.")
            return
    current_level = current_levels[current_category]
    question_index = (current_level - 1) * 5 + len(answered_questions[current_category][current_level])
    current_question, correct_answer = questions_answers[current_category][question_index]
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
window.geometry("500x500")
window.configure(bg="#f0f0f0")

# Creating a frame for better organization
frame = tk.Frame(window, bg="#f0f0f0")
frame.pack(pady=20)

# Creating widgets
instruction_label = tk.Label(frame, text="Welcome to Trivia!", font=("Times New Roman", 35), bg="#f0f0f0")
instruction_label.grid(row=0, column=0, columnspan=2, pady=20)

category_label = tk.Label(frame, text="Choose a category:", font=("Times", 18), bg="#f0f0f0")
category_label.grid(row=1, column=0, padx=20)

category_var = tk.StringVar()
category_var.set('Categories')
categories = list(questions_answers.keys())  # Get all categories
category_dropdown = tk.OptionMenu(frame, category_var, *categories)
category_dropdown.config(font=("Bold italic", 14))
category_dropdown.grid(row=1, column=1, padx=10)

start_button = tk.Button(frame, text="Start Game", command=start_game, font=("Bold italic", 14))
start_button.grid(row=2, column=0, columnspan=2, pady=10)

label = tk.Label(window, text="", font=("Bold italic", 14), bg="#ffffff", padx=10, pady=10, relief="groove", wraplength=300)
label.pack(pady=10, padx=20, fill="both", expand=True)  # Adjust wraplength as needed

entry = tk.Entry(window, font=("Helvetica", 12))
entry.pack(pady=10, padx=20, fill="x")

submit_button = tk.Button(window, text="Submit Answer", command=check_answer, font=("Helvetica", 14))
submit_button.pack(pady=10, padx=20, fill="x")

hint_button = tk.Button(window, text="Hint", command=show_hint, font=("Helvetica", 14))
hint_button.pack(pady=10, padx=20, fill="x")

# Run the tkinter event loop
window.mainloop()
