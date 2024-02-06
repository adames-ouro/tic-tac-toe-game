from flask import Flask, request, jsonify, render_template
from tictactoe import TicTacToe

app = Flask(__name__)
game = TicTacToe()

def board_map(cell_id):
    if cell_id == "cell-0":
        return (0,0)
    elif cell_id == "cell-1":
        return (0,1)
    elif cell_id == "cell-2":
        return (0,2)
    elif cell_id == "cell-3":
        return (1,0)
    elif cell_id == "cell-4":
        return (1,1)
    elif cell_id == "cell-5":
        return (1,2)
    elif cell_id == "cell-6":
        return (2,0)
    elif cell_id == "cell-7":
        return (2,1)
    elif cell_id == "cell-8":
        return (2,2)
        
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/usr', methods=['POST'])
def player_mark():
    # Get JSON data from request to choose mark
    data = request.get_json()
    mark = data.get('mark')
    slot = data.get('cell')

    if mark == 'O':
        game.player = 'X'
        row, col = board_map(slot)
        game.mark(row, col)
        game.player = mark

    else:
        game.player = mark
    return jsonify({'mark': mark})

@app.route('/reset', methods=['POST'])
def reset_game():
    # Reset the game state
    game.reset()
    return jsonify({'status': 'Game reset'})

@app.route('/main.py', methods=['POST'])
def main():
    # Get JSON data from request
    data = request.get_json()

    # Get cell id and mark from data
    cell_id = data.get('id')
    mark = data.get('mark')
    row, col = board_map(cell_id)
    mark = game.player
    game.mark(row, col)
    
    # implement stratergy using the board
    return jsonify({'mark': mark})

if __name__ == '__main__':
    app.run(port=5000)
