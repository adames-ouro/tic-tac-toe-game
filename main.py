from flask import Flask, request, jsonify, render_template
from tictactoe import TicTacToe

app = Flask(__name__)
game = TicTacToe()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main.py', methods=['POST'])
def main():
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
        
    # Get JSON data from request
    data = request.get_json()

    # Get board data from request
    board_data = data.get('board')
    if board_data:
        row = board_data.get('row')
        col = board_data.get('col')
        value = board_data.get('value')
        game.board[row][col] = value

    # Get cell id and mark from data
    cell_id = data.get('id')
    mark = data.get('mark')

    row, col = board_map(cell_id)
    mark = game.player
    game.mark(row, col)

    return jsonify({'mark': mark})

if __name__ == '__main__':
    app.run(port=7000)
