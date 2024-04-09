import random
import tkinter as tk
from tkinter import messagebox
from html import unescape
import requests

class TriviaGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Trivia")
        self.window.geometry("900x800")
        self.window.configure(bg="#0096FF")
        self.current_question = ""
        self.correct_answer = ""
        self.current_level = 1
        self.questions = []
        self.answered_questions = {level: [] for level in range(1, 6)}

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.window, bg="#0096FF")
        frame.pack(pady=20)

        instruction_label = tk.Label(frame, text="Welcome to Trivia!", font=("Times New Roman", 35), bg="#00FF00")
        instruction_label.grid(row=0, column=0, columnspan=2, pady=20)

        category_label = tk.Label(frame, text="Choose categories:", font=("Times", 18), bg="#00FF00")
        category_label.grid(row=1, column=0, padx=20)

        self.categories = [
            {"id": 9, "name": "General Knowledge"},
            {"id": 10, "name": "Books"},
            {"id": 11, "name": "Film"},
            {"id": 12, "name": "Music"},
            {"id": 13, "name": "Musicals & Theatres"},
            {"id": 14, "name": "Television"},
            {"id": 15, "name": "Video Games"},
            {"id": 16, "name": "Board Games"},
            {"id": 17, "name": "Science & Nature"},
            {"id": 18, "name": "Computers"},
            {"id": 19, "name": "Mathematics"},
            {"id": 20, "name": "Mythology"},
            {"id": 21, "name": "Sports"},
            {"id": 22, "name": "Geography"},
            {"id": 23, "name": "History"},
            {"id": 24, "name": "Politics"},
            {"id": 25, "name": "Art"},
            {"id": 26, "name": "Celebrities"},
            {"id": 27, "name": "Animals"},
            {"id": 28, "name": "Vehicles"},
            {"id": 29, "name": "Comics"},
            {"id": 30, "name": "Gadgets"},
            {"id": 31, "name": "Japanese Anime & Manga"},
            {"id": 32, "name": "Cartoon & Animations"}
        ] 
            

        self.selected_categories = tk.StringVar()
        self.selected_categories.set("")

        category_dropdown = tk.OptionMenu(frame, self.selected_categories, *[category["name"] for category in self.categories])
        category_dropdown.config(font=("Bold italic", 14), width=20, bg="#00FF00")
        category_dropdown.grid(row=1, column=1, padx=20)

        start_button = tk.Button(frame, text="Start Game", command=self.start_game, font=("Bold italic", 14), bg="#00FF00")
        start_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.label = tk.Label(self.window, text="", font=("Bold italic", 15), bg="#FFFFFF", padx=10, pady=10, relief="groove", wraplength=800)
        self.label.pack(pady=10, padx=20, fill="both", expand=True) 

        self.entry = tk.Entry(self.window, font=("Helvetica", 30))
        self.entry.pack(pady=10, padx=20, fill="x")

        submit_button = tk.Button(self.window, text="Submit Answer", command=self.check_answer, font=("Helvetica", 14), bg="#00FF00")
        submit_button.pack(pady=10, padx=20, fill="x")

        hint_button = tk.Button(self.window, text="Hint", command=self.show_hint, font=("Helvetica", 14), bg="#00FF00")
        hint_button.pack(pady=10, padx=20, fill="x")

    def fetch_questions(self, category_id):
        try:
            API_URL = f"https://opentdb.com/api.php?amount=10&type=boolean"
            response = requests.get(API_URL)
            response.raise_for_status()
            data = response.json()
            self.questions = data['results']
            self.next_question()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch questions: {e}")


    def show_hint(self):
        if self.correct_answer:
            hint = f"Hint: {self.correct_answer[0].upper()}"
            messagebox.showinfo("Hint", hint)
        else:
            messagebox.showerror("Error", "No question has been loaded yet.")

    def check_answer(self):
        if self.current_question:
            user_answer = self.entry.get().strip()
            if user_answer.lower() == self.correct_answer.lower():
                messagebox.showinfo("Correct!", "Your answer is correct!")
                self.answered_questions[self.current_level].append(self.current_question)
            else:
                messagebox.showerror("Incorrect!", f"Sorry wrong answer, the correct answer is: {self.correct_answer}")
            self.next_question()
        else:
            messagebox.showerror("Error", "No question has been loaded yet.")

    def next_question(self):
        if self.questions:
            rand_question = random.choice(self.questions)
            self.current_question = unescape(rand_question['question'])
            self.correct_answer = rand_question['correct_answer']
            self.label.config(text=self.current_question)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Level Completed", "Congratulations! You have completed this level.")
            self.current_level += 1
            if self.current_level > 5:
                messagebox.showinfo("Game Over", "Congratulations! You have completed all levels.")
                return
            else:
                self.start_game()

    def start_game(self):
        category_name = self.selected_categories.get()
        category_id = next((category["id"] for category in self.categories if category["name"] == category_name), None)
        if category_id:
            self.fetch_questions(category_id)

        else:
            messagebox.showerror("Error", "Invalid category selected.")

if __name__ == "__main__":
    game = TriviaGame()
    game.window.mainloop()
