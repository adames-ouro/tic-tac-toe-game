class TicTacToe(object):
    '''Management of a Tic-Tac-Toe game'''
    def __init__(self):
        '''Start a new game'''
        self.board = [ ['']*3 for _ in range(3)] # 3x3 matrix
        self.player = '' # Player parameter
        self.last_move = ()
        self.pc = ''

    def reset(self):
        '''Reset the game to the initial state'''
        self.board = [['']*3 for _ in range(3)]
        self.player = ''
        self.last_move = ()
        self.pc = ''

    def player_mark(self, row, col): # player makes mark
        '''
        Put an X or O mark on the board at position (row,col) 
        for next player's turn.
        '''
        if self.end_game():
            raise Exception("The game has already ended.")

        if self.board[row][col] != '':
            raise Exception("This cell is already taken. Please choose another.")
        
        if self.end_game() is False:
            # mark the position
            self.board[row][col] = self.player
            self.last_move = (row,col)

    def pc_mark(self):
        '''
        Put an X or O mark on the board at position (row,col) using Minimax algo
        '''
        if self.end_game() is False:
            if self.player == 'X':
                self.pc = 'O'
            elif self.player == 'O':
                self.pc = 'X'

            best_score = -float('inf')
            best_move = None

            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '':
                        self.board[i][j] = self.pc
                        score = self.minimax(0, False)  # Start with depth 0, minimizing
                        self.board[i][j] = ''  # Undo the move
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)

            if best_move:
                self.board[best_move[0]][best_move[1]] = self.pc
                self.last_move = (best_move[0],best_move[1])
            else:
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == '':
                            self.board[i][j] = self.pc
                            self.last_move = (i,j)
                            return
   
    def minimax(self, depth, isMaximizing):
        if self.check_win(self.pc):
            return 1
        elif self.check_win(self.player):
            return -1
        elif self.is_board_full():
            return 0

        if isMaximizing:
            bestScore = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '':
                        self.board[i][j] = self.pc
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = ''
                        bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '':
                        self.board[i][j] = self.player
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = ''
                        bestScore = min(score, bestScore)
            return bestScore

    def check_win(self, mark):
        # Check rows, columns, and diagonals for a win
        for row in self.board:
            if all(s == mark for s in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == mark for row in range(3)):
                return True
        if all(self.board[i][i] == mark for i in range(3)) or all(self.board[i][2-i] == mark for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(all(cell != '' for cell in row) for row in self.board)

    def end_game(self):
        '''Return True if the game has ended due to a win or a draw.'''
        # Check for a win for both 'X' and 'O'
        for mark in 'XO':
            if self.check_win(mark):
                return True
        # Use the existing method to check if the board is full
        if self.is_board_full():
            return True
        # If there's no win and the board is not full, the game hasn't ended
        return False
