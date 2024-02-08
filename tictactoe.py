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

    def mark(self, row, col): # player makes mark
        '''
        Put an X or O mark on the board at position (row,col) 
        for next player's turn.
        '''
        if self.end_game() is False:
            # if the position is already taken
            if self.board[row][col] != '':
                raise ValueError('Board position occupied') # show error on web
            
            # if the game is already over
            if self.end_game() is not False:
                raise ValueError('Game is already complete') # show on web

            # mark the position
            self.board[row][col] = self.player
            self.values[row][col] = None
            self.memory[(row,col)] =  self.player

            # turn based moves
            if self.player == 'X':
                self.player = 'O'
            else:
                self.player = 'X'
            
            self.last_move = (row,col)

    def update(self): # pc makes mark
        if self.end_game() is False:
            if self.player == 'X':
                pc = 'O'
            elif self.player == 'O':
                pc = 'X'

            # No immediate threats, go greedy
            rows, cols = set(), set()

            for coord in self.memory.keys():
                rows.add(coord[0])
                cols.add(coord[1])

            # update values for grids with goal of horz line
            for _rows in rows:
                for _elements in range(len(self.values)):
                    if self.values[_rows][_elements] is not None:
                        self.values[_rows][_elements] += 2

            # update values for grids with goal of vert line
            for _cols in cols:
                for _elements in range(len(self.values)):
                    if self.values[_elements][_cols] is not None:
                        self.values[_elements][_cols] += 2

            # Assuming 'game.values' is your list of lists
            max_value = -1
            max_pos = ()

            for i, row in enumerate(self.values):
                for j, value in enumerate(row):
                    if value is not None and value > max_value:
                        max_value = value
                        max_pos = (i, j)

            offensive_move = max_pos

            #### override answer if defensive move is required (prevent a loss)

            # Check diagonals for potential wins
            diag1 = [self.board[i][i] for i in range(3)]
            if diag1.count(pc) == 2:
                try:
                    max_pos = (diag1.index(''), diag1.index(''))
                except:
                    max_pos = offensive_move

            diag2 = [self.board[i][2-i] for i in range(3)]
            if diag2.count(pc) == 2:
                try:
                    max_pos = (diag2.index(''), 2-diag2.index(''))
                except:
                    max_pos = offensive_move

            # Check rows and columns for potential wins
            for i in range(3):
                # Check rows
                if self.board[i].count(pc) == 2:
                    try:
                        max_pos = (i, self.board[i].index(''))
                    except:
                        max_pos = offensive_move
                
                # Check columns
                col = [self.board[0][i], self.board[1][i], self.board[2][i]]
                if col.count(pc) == 2:
                    try:
                        max_pos = (col.index(''), i)
                    except:
                        max_pos = offensive_move
                        
            # mark the position
            self.board[max_pos[0]][max_pos[1]] = self.player
            self.values[max_pos[0]][max_pos[1]] = None
            self.memory[(max_pos[0],max_pos[1])] =  self.player

            # turn based moves
            if self.player == 'X':
                self.player = 'O'
            else:
                self.player = 'X'

            self.last_move = (max_pos[0],max_pos[1])


    def _is_win(self,mark):
        '''Check if the board configuration is a win for the given player'''
        board = self.board
        return ('X' == board[0][0] == board[0][1] == board[0][2] or # row 0
                'X' == board[1][0] == board[1][1] == board[1][2] or # row 1
                'X' == board[2][0] == board[2][1] == board[2][2] or # row 2
                'X' == board[0][0] == board[1][0] == board[2][0] or # column 0
                'X' == board[0][1] == board[1][1] == board[2][1] or # column 1
                'X' == board[0][2] == board[1][2] == board[2][2] or # column 2
                'X' == board[0][0] == board[1][1] == board[2][2] or # diagonals
                'X' == board[0][2] == board[1][1] == board[2][0] or # other mark
                'O' == board[0][0] == board[0][1] == board[0][2] or # row 0
                'O' == board[1][0] == board[1][1] == board[1][2] or # row 1
                'O' == board[2][0] == board[2][1] == board[2][2] or # row 2
                'O' == board[0][0] == board[1][0] == board[2][0] or # column 0
                'O' == board[0][1] == board[1][1] == board[2][1] or # column 1
                'O' == board[0][2] == board[1][2] == board[2][2] or # column 2
                'O' == board[0][0] == board[1][1] == board[2][2] or # diagonals
                'O' == board[0][2] == board[1][1] == board[2][0])
    
    def end_game(self):
        '''Return the True if game ended'''
        for mark in 'XO':
            if self._is_win(mark):
                return True
            
        empty_cells = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    empty_cells = empty_cells + 1
        if (empty_cells == 0):
            return True # tie
        else:
            return False