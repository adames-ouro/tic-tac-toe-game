class TicTacToe(object):
    '''Management of a Tic-Tac-Toe game (does not do strategy)'''

    def __init__(self):
        '''Start a new game'''
        self.board = [ ['']*3 for _ in range(3)] # 3x3 matrix
        self.player = '' # Player parameter
        self.memory = {}
        self.values = [ [0]*3 for _ in range(3)] # 3x3 matrix
        self.values[0][0] += 2
        self.values[0][2] += 2
        self.values[2][0] += 2
        self.values[2][2] += 2
        self.last_move = ()
        self.pc = ''

    def reset(self):
        '''Reset the game to the initial state'''
        self.board = [['']*3 for _ in range(3)]
        self.player = ''
        self.memory = {}
        self.values = [ [0]*3 for _ in range(3)] # 3x3 matrix
        self.values[0][0] += 2
        self.values[0][2] += 2
        self.values[2][0] += 2
        self.values[2][2] += 2
        self.last_move = ()
        self.pc = ''

    def player_mark(self, row, col): # player makes mark
        '''
        Put an X or O mark on the board at position (row,col) 
        for next player's turn.
        '''
        if self.end_game() is False:
            # mark the position
            self.board[row][col] = self.player
            self.values[row][col] = None
            self.memory[(row,col)] =  self.player
            self.last_move = (row,col)


    def pc_mark(self):
        '''
        Put an X or O mark on the board at position (row,col) 
        '''
        if self.end_game() is False:
            if self.player == 'X':
                self.pc = 'O'
            elif self.player == 'O':
                self.pc = 'X'

            best_score = -1
            best_move = None

            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '':
                        self.board[i][j] = self.pc
                        score = self.evaluate_move(i, j, self.pc)
                        self.board[i][j] = ''
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)

            if best_move:
                self.board[best_move[0]][best_move[1]] = self.pc
                self.values[best_move[0]][best_move[1]] = None
                self.memory[(best_move[0],best_move[1])] =  self.pc
                self.last_move = (best_move[0],best_move[1])
            else:
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == '':
                            self.board[i][j] = self.pc
                            self.values[i][j] = None
                            self.memory[(i,j)] =  self.pc
                            self.last_move = (i,j)
                            return

    def evaluate_move(self, row, col, mark):
        '''Eval move'''
        score = 0
        if self.check_potential_win(row, col, mark):
            score += 1
        return score

    def check_potential_win(self, row, col, mark):
        '''check if move adds to a win'''
        # Check row
        if all(self.board[row][c] == mark or c == col for c in range(3)):
            return True
        # Check column
        if all(self.board[r][col] == mark or r == row for r in range(3)):
            return True
        # Check diagonal (if applicable)
        if row == col and all(self.board[i][i] == mark or i == row for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2-i] == mark or i == row for i in range(3)):
            return True
        return False                
    
    def end_game(self):
        '''Return the True if game ended'''
        board = self.board
        for mark in 'XO':
            # check rows
            for row in board:
                if all(slot == mark for slot in row):
                    return True
            # check columns
            for col in range(len(board[0])):
                if all(row[col] == mark for row in board):
                    return True
            # check diagonals
            if all(board[i][i] == mark for i in range(len(board))):
                return True
            if all(board[i][len(board)-i-1] == mark for i in range(len(board))):
                return True
        return False