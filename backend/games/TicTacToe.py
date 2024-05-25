import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros(9)
        self.current_player = 1

    def reset(self):
        self.board = np.zeros(9)
        self.current_player = 1
        return self.board.tolist()

    def move(self, position):
        if self.board[position] != 0:
            return False
        self.board[position] = self.current_player
        self.current_player = 3 - self.current_player  # switch player
        return True

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != 0:
                return int(self.board[combo[0]])
        if 0 not in self.board:
            return 0  # Draw
        return None  # No winner yet
