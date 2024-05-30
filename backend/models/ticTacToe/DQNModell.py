import numpy as np
import tensorflow as tf
from tensorflow. import Sequential 
from keras.layers import Dense, Flatten 
from collections import deque
import random

class DQNAgent:
    def __init__(self):
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self.build_model()
        self.target_model = self.build_model()
        self.target_model.set_weights(self.model.get_weights())
        self.memory = deque(maxlen=2000)

    def build_model(self):
        model = Sequential([
            Flatten(input_shape=(3, 3)),
            Dense(128, activation='relu'),
            Dense(64, activation='relu'),
            Dense(9, activation='linear')
        ])
        model.compile(optimizer=tf.keras.optimizers.Adam(self.learning_rate), 
                      loss='mse')
        return model

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.choice(np.where(state.flatten() == 0)[0])
        act_values = self.model.predict(state.reshape(1, 3, 3))
        return np.argmax(act_values[0])

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target += self.gamma * np.amax(self.target_model.predict(next_state.reshape(1, 3, 3))[0])
            target_f = self.model.predict(state.reshape(1, 3, 3))
            target_f[0][action] = target
            self.model.fit(state.reshape(1, 3, 3), target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())
