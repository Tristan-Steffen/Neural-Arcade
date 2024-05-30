from games import TicTacToe
from models.ticTacToe import DQNAgent
import keras
import os
import matplotlib.pyplot as plt

EPISODES = 1000
game = TicTacToe.TicTacToe()
agent = DQNAgent.DQNAgent()

# Tracking performance
win_history = []
draw_history = []
loss_history = []

for e in range(EPISODES):
    game.reset()
    state = [float(x) for x in game.board.tolist()] + [float(game.current_player)]
    done = False
    win, draw, loss = 0, 0, 0
    while not done:
        action = agent.act(state)
        valid_move = game.move(action)
        next_state = [float(x) for x in game.board.tolist()] + [float(game.current_player)]
        reward = 0
        if valid_move:
            winner = game.check_winner()
            if winner is not None:
                if winner == 0:
                    reward = 0.5  # Draw
                    draw += 1
                else:
                    reward = 1 if winner == game.current_player * -1 else -1
                    if reward == 1:
                        win += 1
                    else:
                        loss += 1
                done = True
            agent.remember(state, action, reward, next_state, done)
            state = next_state
        else:
            reward = -5
            loss += 1
            done = True
            agent.remember(state, action, reward, next_state, done)
    agent.replay(300)
    agent.update_target_model()
    win_history.append(win)
    draw_history.append(draw)
    loss_history.append(loss)
    if e % 25 == 0:
        print(f"Episode {e}/{EPISODES}, Wins: {sum(win_history)}, Draws: {sum(draw_history)}, Losses: {sum(loss_history)}, Epsilon: {agent.epsilon}")

# Save the model
keras.saving.save_model(agent.model, os.path.join("DQNtrainedModels", "DQNModell.h5"))

# Plotting the results
plt.plot(win_history, label="Wins")
plt.plot(draw_history, label="Draws")
plt.plot(loss_history, label="Losses")
plt.xlabel("Episodes")
plt.ylabel("Count")
plt.legend()
plt.show()