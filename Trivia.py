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
        self.question_number = 1
        self.answered_questions = {level: [] for level in range(1, 6)}
        self.right_answers = 0
        self.wrong_answers = 0

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.window, bg="#0096FF")
        frame.pack(pady=20)

        instruction_label = tk.Label(frame, text="Welcome to Trivia!", font=("Times New Roman", 35), bg="#00FF00")
        instruction_label.grid(row=0, column=0, columnspan=2, pady=20)

        start_button = tk.Button(frame, text="Start Game", command=self.start_game, font=("Bold italic", 14), bg="#00FF00")
        start_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.label = tk.Label(self.window, text="", font=("Bold italic", 15), bg="#FFFFFF", padx=10, pady=10, relief="groove", wraplength=800)
        self.label.pack(pady=10, padx=20, fill="both", expand=True) 

        true_button = tk.Button(self.window, text="True", command=lambda: self.check_answer(True), font=("Helvetica", 14), bg="#00FF00")
        true_button.pack(pady=10, padx=20, fill="x")

        false_button = tk.Button(self.window, text="False", command=lambda: self.check_answer(False), font=("Helvetica", 14), bg="#00FF00")
        false_button.pack(pady=10, padx=20, fill="x")

        self.score_label = tk.Label(self.window, text="Score: Right Answers: 0, Wrong Answers: 0", font=("Helvetica", 14), bg="#FFFFFF")
        self.score_label.pack(pady=10, padx=20, fill="x")

    def fetch_questions(self):
        try:
            API_URL = f"https://opentdb.com/api.php?amount=50&type=boolean"
            response = requests.get(API_URL)
            response.raise_for_status()
            data = response.json()
            self.questions = data['results']
            self.next_question()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch questions: {e}")

    def check_answer(self, user_answer):
        if self.current_question:
            correct_answer = self.correct_answer.lower()
            user_answer = "true" if user_answer else "false"
            if user_answer == correct_answer:
                messagebox.showinfo("Correct!", "Your answer is correct!")
                self.right_answers += 1
            else:
                messagebox.showerror("Incorrect!", "Sorry wrong answer!")
                self.wrong_answers += 1
            self.update_score()
            self.next_question()
        else:
            messagebox.showerror("Error", "No question has been loaded yet.")

    def update_score(self):
        self.score_label.config(text=f"Score: Right Answers: {self.right_answers}, Wrong Answers: {self.wrong_answers}")

    def next_question(self):
        if self.questions:
            rand_question = random.choice(self.questions)
            self.current_question = unescape(rand_question['question'])
            self.correct_answer = rand_question['correct_answer']
            self.label.config(text=f"Question {self.question_number}: {self.current_question}")
            self.question_number += 1
        else:
            messagebox.showinfo("Level Completed", "Congratulations! You have completed this level.")
            self.current_level += 1
            if self.current_level > 5:
                messagebox.showinfo("Game Over", "Congratulations! You have completed all levels.")
                return
            else:
                self.start_game()

    def start_game(self):
        self.question_number = 1
        self.right_answers = 0
        self.wrong_answers = 0
        self.update_score()
        self.fetch_questions()

if __name__ == "__main__":
    game = TriviaGame()
    game.window.mainloop()
