from flask import Flask, request, jsonify, render_template


class TicTacToe(object):
    '''Management of a Tic-Tac-Toe game (does not do strategy)'''

    def __init__(self):
        '''Start a new game'''
        self.board =[ [' ']*3 for _ in range(3)] # 3x3 matrix
        self.player = 'X' # Player with X always starts

    def mark(self, row, col):
        '''
        Put an X or O mark on the board at position (row,col) 
        for next player's turn.
        '''
        # out of bounds error
        if not (0 <= row <= 2 and 0 <= col <= 2):
            raise ValueError('Invalid board position')
        
        # if the position is already taken
        if self.board[row][col] != ' ':
            raise ValueError('Board position occupied')
        
        # if the game is already over
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        
        # mark the position
        self.board[row][col] = self.player

        # turn based moves
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def _is_win(self,mark):
        '''Check if the board configuration is a win for the given player'''
        board = self.board
        return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or # row 2
                mark == board[0][0] == board[1][0] == board[2][0] or # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or # diagonals
                mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):
        '''Return the mark of the winning player'''
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None
    
    def __str__(self):
        '''Return the string representation of the current game'''
        #rows = ['|'.join(self.board[r]) for r in range(3)]
        return self.board
    

app = Flask(__name__)
game = TicTacToe()

@app.route('/')
def home():
    return render_template('index.html')

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


@app.route('/main.py', methods=['POST'])
def main():

    # Get JSON data from request
    data = request.get_json()

    # Get cell id from data
    cell_id = data['id']

    # show cell id 
    row,col = board_map(cell_id)

    # mark the cell
    mark = game.player
    game.mark(row,col)

    return jsonify({'mark': mark})

if __name__ == '__main__':
    app.run(port=5000)
