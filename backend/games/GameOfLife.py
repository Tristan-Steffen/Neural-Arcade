import numpy as np

class GameOfLife:
    def __init__(self, rows=10, columns=10):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((self.rows, self.columns), dtype=int)

    def reset(self, rows=None, columns=None):
        if rows is not None:
            self.rows = rows
        if columns is not None:
            self.columns = columns
        self.board = np.zeros((self.rows, self.columns), dtype=int)
        return {'board': self.board.tolist()}

    def set_cell(self, row, column, state):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.board[row, column] = state
            return True
        return False

    def step(self):
        new_board = np.zeros((self.rows, self.columns), dtype=int)
        for row in range(self.rows):
            for column in range(self.columns):
                live_neighbors = self._count_live_neighbors(row, column)
                if self.board[row, column] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_board[row, column] = 0
                    else:
                        new_board[row, column] = 1
                else:
                    if live_neighbors == 3:
                        new_board[row, column] = 1
        self.board = new_board
        return {'board': self.board.tolist()}

    def _count_live_neighbors(self, row, column):
        neighbors = [
            (row-1, column-1), (row-1, column), (row-1, column+1),
            (row, column-1),                 (row, column+1),
            (row+1, column-1), (row+1, column), (row+1, column+1)
        ]
        count = 0
        for r, c in neighbors:
            if 0 <= r < self.rows and 0 <= c < self.columns:
                count += self.board[r, c]
        return count
