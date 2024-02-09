# Tic Tac Toe Game

This Tic Tac Toe game is a web application built with Flask, allowing players to play against a computer opponent. It uses HTML, CSS, and JavaScript for the frontend, with Flask serving the backend logic. The game features a simple, user-friendly interface and provides an engaging Tic Tac Toe experience.

## Features

- Play Tic Tac Toe against an intelligent computer opponent.
- Choose your mark ('X' or 'O') at the beginning of the game.
- The game state is managed through a Flask backend, with player and computer moves processed server-side.
- Responsive design for enjoyable gameplay on both desktop and mobile devices.
- A reset button to start a new game anytime.

## Installation

To run this Tic Tac Toe game, you will need Python and Flask installed on your system. Follow these steps to set up and run the game:

1. Clone or download this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install Flask if you haven't already: `pip install Flask`
4. Run the Flask application: `python main.py`
5. Open your web browser and go to `http://127.0.0.1:8000/` to start playing.

## Files and Directories

- `main.py`: The Flask backend file that handles routing and game logic.
- `tictactoe.py`: Contains the `TicTacToe` class, managing the game state and bot strategy.
- `static/css/style.css`: CSS file for styling the web pages.
- `static/js/script.js`: JavaScript file for handling user interactions and AJAX requests.
- `templates/index.html`: The HTML template for the game interface.

## How to Play

- Upon visiting the website, choose your mark ('X' or 'O') by selecting the corresponding radio button and clicking the "Submit" button.
- Click on any cell in the grid to make your move.
- The computer opponent will automatically make its move after you.
- The game ends when one player wins by aligning three of their marks vertically, horizontally, or diagonally, or when all cells are filled, resulting in a draw.
- Click the "Reset Game" button to start a new game at any time.

## Technologies Used

- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Game Logic:** Python

## Contribution

Feel free to fork this project, submit pull requests, or report bugs and suggestions in the issues section.

Enjoy playing Tic Tac Toe!
