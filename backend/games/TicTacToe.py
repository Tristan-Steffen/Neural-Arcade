import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.current_player = 1

    def reset(self):
        self.board = np.zeros((3, 3))
        self.current_player = 1
        return self.board.tolist()

    def move(self, position):
        if self.board[position[0]][position[1]] != 0:
            return False
        self.board[position[0]][position[1]] = self.current_player
        self.current_player = self.current_player * -1  # switch player
        return True

    def check_winner(self):
        print(self.board)
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
        for i in range(len(self.board[0])):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        if 0 not in self.board:
            return 0  # Draw
        return None  # No winner yet
