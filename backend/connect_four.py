import numpy as np

class ConnectFour:
    ROWS = 6
    COLUMNS = 7
    EMPTY = 0
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    def __init__(self):
        self.board = np.zeros((self.ROWS, self.COLUMNS), dtype=int)
        self.current_player = self.PLAYER_ONE

    def reset(self):
        self.board = np.zeros((self.ROWS, self.COLUMNS), dtype=int)
        self.current_player = self.PLAYER_ONE
        return {'board': self.board.tolist(), 'currentPlayer': self.current_player}

    def is_valid_location(self, col):
        return self.board[self.ROWS-1][col] == self.EMPTY

    def get_next_open_row(self, col):
        for r in range(self.ROWS):
            if self.board[r][col] == self.EMPTY:
                return r

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def check_winner(self, piece):
        # Check horizontal locations
        for c in range(self.COLUMNS-3):
            for r in range(self.ROWS):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True

        # Check vertical locations
        for c in range(self.COLUMNS):
            for r in range(self.ROWS-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(self.COLUMNS-3):
            for r in range(self.ROWS-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(self.COLUMNS-3):
            for r in range(3, self.ROWS):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True

        return False
