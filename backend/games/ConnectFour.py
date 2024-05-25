import numpy as np

class ConnectFour:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((self.rows, self.columns))
        self.current_player = 1

    def reset(self):
        self.board = np.zeros((self.rows, self.columns))
        self.current_player = 1
        return {'board': self.board.tolist(), 'currentPlayer': self.current_player}

    def move(self, column):
        if not 0 <= column < self.columns:
            return False
        row = next((r for r in range(self.rows - 1, -1, -1) if self.board[r, column] == 0), None)
        if row is None:
            return False
        self.board[row, column] = self.current_player
        self.current_player = 3 - self.current_player  # Switch player
        return True

    def check_winner(self):
        # Check for a win in horizontal, vertical, and both diagonal directions
        for r in range(self.rows):
            for c in range(self.columns - 3):
                if self.board[r, c] == self.board[r, c + 1] == self.board[r, c + 2] == self.board[r, c + 3] != 0:
                    return int(self.board[r, c])

        for r in range(self.rows - 3):
            for c in range(self.columns):
                if self.board[r, c] == self.board[r + 1, c] == self.board[r + 2, c] == self.board[r + 3, c] != 0:
                    return int(self.board[r, c])

        for r in range(self.rows - 3):
            for c in range(self.columns - 3):
                if self.board[r, c] == self.board[r + 1, c + 1] == self.board[r + 2, c + 2] == self.board[r + 3, c + 3] != 0:
                    return int(self.board[r, c])

        for r in range(3, self.rows):
            for c in range(self.columns - 3):
                if self.board[r, c] == self.board[r - 1, c + 1] == self.board[r - 2, c + 2] == self.board[r - 3, c + 3] != 0:
                    return int(self.board[r, c])

        if np.all(self.board != 0):
            return 0  # Draw
        return None  # No winner yet
