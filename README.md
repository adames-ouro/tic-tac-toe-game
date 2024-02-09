# Tic Tac Toe Game

![Game Image](static/img/game.png)

This Tic Tac Toe game is a web application built with Flask, allowing players to play against a computer opponent. It uses HTML, CSS, and JavaScript for the frontend, with Flask serving the backend logic. The AI opponent is constructed using the Minimax Algorithm.

## Features

- Play Tic Tac Toe against an AI opponent.
- Choose your mark ('X' or 'O') at the beginning of the game.
- The game state is managed through a Flask backend, with player and computer moves processed server-side.
- A reset button to start a new game anytime.


## Files and Directories

- `main.py`: The Flask backend file.
- `tictactoe.py`: Contains the `TicTacToe` class, managing the game state and AI bot strategy.
- `static/css/style.css`: CSS file for styling the web pages.
- `static/js/script.js`: JavaScript file for handling user interactions and AJAX requests.
- `templates/index.html`: The HTML template for the game interface.

## How to Play

- Upon visiting the website, choose your mark ('X' or 'O') by selecting the corresponding radio button and clicking the "Submit" button.
- Click on any cell in the grid to make your move.
- The AI opponent will automatically make its move after you.
- The game ends when one player wins by aligning three of their marks vertically, horizontally, or diagonally, or when all cells are filled, resulting in a draw.
- Click the "Reset Game" button to start a new game at any time.

## Technologies Used

- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Game Logic:** Minimax Algorithm using Python

## Minimax Algorithm for AI bot

The Tic Tac Toe AI opponent runs thanks to the Minimax algorithm to determine the best move optimally.

The Minimax algorithm works by exploring all possible moves in the game, predicting the opponent's responses to those moves, and choosing the move that maximizes the player's chance of winning while minimizing the AI's chance. Here's a simplified explanation of the algorithm:

1. **Base Case**: The recursion ends when the function encounters a terminal state:
   - If the AI (`self.pc`) wins, return `1`.
   - If the player wins, return `-1`.
   - If the board is full (draw), return `0`.

2. **Recursive Case**: For each potential move, the algorithm recursively simulates playing that move, then:
   - If it's the AI's turn (maximizing player), it tries to maximize the score.
   - If it's the player's turn (minimizing player), it tries to minimize the score.


## Installation

To run this Tic Tac Toe game, you will need Python and Flask installed on your system. Follow these steps to set up and run the game:

1. Clone or download this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install Flask if you haven't already: `pip install Flask`
4. Run the Flask application: `python main.py`
5. Open your web browser and go to `http://127.0.0.1:8000/` to start playing.