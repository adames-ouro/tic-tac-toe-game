from flask import Flask, request, jsonify, render_template
from tictactoe import TicTacToe

app = Flask(__name__)
game = TicTacToe()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/usr', methods=['POST'])
def player_mark():
    # Get JSON data from request to choose mark
    data = request.get_json()
    mark = data.get('mark')

    if mark == 'O':
        game.player = 'X'
        game.player = mark

    else:
        game.player = mark

    return jsonify({'mark': mark})

@app.route('/reset', methods=['POST'])
def reset_game():
    # Reset the game state
    game.reset()
    return jsonify({'status': 'Game reset'})

if __name__ == '__main__':
    app.run(port=8000)
