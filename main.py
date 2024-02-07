from flask import Flask, request, jsonify, render_template, redirect, url_for #, session
from tictactoe import TicTacToe
import random

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
@app.route('/home', methods=['GET','POST'])
def home():
    selected_mark = request.args.get('selected_mark', None)
    return render_template('index.html', selected_mark=selected_mark,game_board=game.board)


@app.route('/reset', methods=['POST'])
def reset_game():
    # Reset the game state
    game.reset()
    return jsonify({'status': 'Game reset'})


@app.route('/submit', methods=['POST'])
def submit():
    # Access the data from form
    player1_mark = request.form.get('player1')
    if player1_mark:
        if player1_mark == 'O':
            corners = [(0,0),(0,2),(2,0),(2,2)]
            random_choice = random.choice(corners)
            game.mark(random_choice[0],random_choice[1])
            game.board[random_choice[0]][random_choice[1]] = 'X'
            game.player = 'O'
            #session['game_board'] = game.board
            #session['selected_mark'] = player1_mark
            # Redirect to the home route after setting the player's mark
            return redirect(url_for('home'))

        elif player1_mark == 'X':
            game.player = 'X'
            #session['game_board'] = game.board
            #session['selected_mark'] = player1_mark
            # Redirect to the home route after setting the player's mark
            return redirect(url_for('home'))
    
    else:
        # Handle the case where no mark was selected
        # Redirect back to the home page or show an error message
        return redirect(url_for('home'))




#@app.route('/usr', methods=['POST'])
#def player_mark():
    # Get JSON data from request to choose mark
#    data = request.get_json()
#    mark = data.get('mark')
#    slot = data.get('cell')
#    row, col = board_map(slot)
#    game.mark(row, col)
#    return jsonify({'mark': mark})

#@app.route('/usrmove', methods=['POST'])
#def player_move():
    # Get JSON data from request to choose mark
#    data = request.get_json()
#    mark = data.get('mark')
#    slot = data.get('cell')
#    row, col = board_map(slot)
#    game.mark(row, col)
#    return jsonify({'mark': mark})

#@app.route('/pcmove', methods=['GET'])
#def pc_move():
#    game.update()
#    pc_move = grid_map(game.last_move)
#    pc_mark = game.player
#    return jsonify({'pc_mark':pc_mark, 'pc_move':pc_move})



if __name__ == '__main__':
    app.run(port=8000)