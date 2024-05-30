import numpy as np
from models.ticTacToe.DQNModell import DQNAgent

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
    
EPISODES = 1000
game = TicTacToe()
agent = DQNAgent()

for e in range(EPISODES):
    state = game.reset()
    done = False
    while not done:
        action = agent.act(state)
        if game.move(action):
            next_state = game.board.reshape((3, 3))
            winner = game.check_winner()
            reward = 0
            if winner is not None:
                if winner == 0:
                    reward = 0.5  # Draw
                else:
                    reward = 1 if winner == 1 else -1
                done = True
            agent.remember(state, action, reward, next_state, done)
            state = next_state
    agent.replay(32)
    agent.update_target_model()

    if e % 100 == 0:
        print(f"Episode {e}/{EPISODES}, Epsilon: {agent.epsilon}")

# Modell speichern
agent.model.save('tictactoe_dqn_model.h5')
