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

def grid_map(cell_id):
    if cell_id == (0,0):
        return "cell-0"
    elif cell_id == (0,1):
        return "cell-1"
    elif cell_id == (0,2):
        return "cell-2"
    elif cell_id == (1,0):
        return "cell-3"
    elif cell_id == (1,1):
        return "cell-4"
    elif cell_id == (1,2):
        return "cell-5"
    elif cell_id == (2,0):
        return "cell-6"
    elif cell_id == (2,1):
        return "cell-7"
    elif cell_id == (2,2):
        return "cell-8"
    
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

@app.route('/computer_move', methods=['GET'])
def automatic_move():
    def pc_move():
        # get filled cell positions
        rows, cols = set(), set()
        for coord in game.memory.keys():
            rows.add(coord[0])
            cols.add(coord[1])

        # update values for grids with goal of horz line
        for _rows in rows:
            for _elements in range(len(game.values)):
                if game.values[_rows][_elements] is not None:
                    game.values[_rows][_elements] += 2

        # update values for grids with goal of vert line
        for _cols in cols:
            for _elements in range(len(game.values)):
                if game.values[_elements][_cols] is not None:
                    game.values[_elements][_cols] += 2

        # Assuming 'game.values' is your list of lists
        max_value = 2
        max_pos = ()

        for i, row in enumerate(game.values):
            for j, value in enumerate(row):
                if value is not None and value > max_value:
                    max_value = value
                    max_pos = (i, j)

        if game.player == 'X':
            game.player = 'O'
        else:
            game.player = 'X'

        return max_pos
    
    # implement stratergy using the board
    pc_mark = pc_move()
    html_id = grid_map(pc_mark)
    game.mark(pc_mark[0], pc_mark[1])
    return jsonify({'mark': game.player, 'html_id': html_id})

@app.route('/usrmove', methods=['POST'])
def player_move():
    # Get JSON data from request
    data = request.get_json()

    # Get cell id and mark from data
    cell_id = data.get('id')
    mark = data.get('mark')
    row, col = board_map(cell_id)
    mark = game.player
    game.mark(row, col)
    return jsonify({'mark': mark})


if __name__ == '__main__':
    app.run(port=8000)