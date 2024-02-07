from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from tictactoe import TicTacToe
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'
game = TicTacToe()
selected_mark = None

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
@app.route('/home', methods=['GET','POST'])
def home():
    selected_mark = session.get('selected_mark', None)
    cell_id = session.get('cell_id',None)
    return render_template('index.html',board=game.board, cell_id=cell_id, selected_mark=selected_mark)


@app.route('/reset', methods=['POST'])
def reset_game():
    # Reset the game state
    game.reset()
    session.pop('selected_mark', None)
    return redirect(url_for('home'))


@app.route('/submit', methods=['POST'])
def submit():
    # Access the data from form
    player1_mark = request.form.get('player1')

    if player1_mark:
        session['selected_mark'] = player1_mark
        if player1_mark == 'O':
            corners = [(0,0),(0,2),(2,0),(2,2)]
            random_choice = random.choice(corners)
            game.mark(random_choice[0],random_choice[1])
            game.board[random_choice[0]][random_choice[1]] = 'X'
            game.player = 'X'
            print(game.board)

        elif player1_mark == 'X':
            game.player = 'O'
            print(game.board)

    return redirect(url_for('home'))
            
            
### mood to fix last move of game
@app.route('/player-move', methods=['POST'])
def player_move():
    data = request.get_json()
    cell_id = data.get('cell_id')
    selected_mark = game.player
    pc_cell,pc_mark = None, None

    if cell_id is not None:
        row, col = board_map(cell_id)
        game.mark(row, col)
        selected_mark=game.player
        game.board[row][col] = selected_mark

        # pc move
        if game.end_game() is False:
            game.update()
            move = game.last_move
            pc_cell = grid_map(move)
            pc_mark = game.player
                
    return jsonify(board=game.board,cell_id=cell_id,selected_mark=selected_mark,pc_cell=pc_cell,pc_mark=pc_mark)


if __name__ == '__main__':
    app.run(port=8000)