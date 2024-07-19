Trivia Game

Welcome to the Trivia Game! This is a simple trivia game built using Python's tkinter library and the Open Trivia Database API.

How to Play:

    Start the Game: Click on the "Start Game" button to begin.
    Answer Questions: Read the question presented and click either "True" or "False" to answer.
    Score Keeping: Your score is tracked with each correct or incorrect answer.
    Level Up: Complete all questions in a level to advance to the next level.
    Game Over: Complete all 5 levels to finish the game.

Features:

    Random Questions: Each game session fetches random true/false questions from the Open Trivia Database API.
    Levels: Progress through 5 levels of increasing difficulty.
    Score Tracking: See your current score displayed on the screen.
    Feedback: Immediate feedback on whether your answer was correct or incorrect.
    Responsive GUI: Built using tkinter, ensuring a user-friendly interface.

Requirements:

    Python 3.x
    tkinter library (usually included in standard Python distributions)
    requests library (install via pip install requests if not already installed)

Installation:

    Clone the repository:

    bash

git clone <repository_url>

Navigate into the directory:

bash

cd trivia-game

Run the game:

    python trivia_game.py

Notes:

    Ensure you have an active internet connection to fetch questions from the API.
    Questions are fetched in batches of 50 from the Open Trivia Database API.
    Enjoy the game and test your trivia knowledge!
    
