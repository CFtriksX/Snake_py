import gym
import random
import numpy as np
import tensorflow as tf
from tensorflow import keras

env = gym.make('LunarLander-v2')
env.reset()
goal_steps = 200
score_requirement = 50
initial_games = 1000

def model_data_preparation():
    training_data = []
    accepted_scores = []
    for game_index in range(initial_games):
        score = 0
        game_memory = []
        previous_observation = []
        for step_index in range(goal_steps):
            action = random.randrange(0, 4)
            observation, reward, done, info = env.step(action)
            if len(previous_observation) > 0:
                game_memory.append([previous_observation, action])

            previous_observation = observation
            score += reward
            if done:
                break

        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1] == 0:
                    output = [1, 0, 0, 0]
                elif data[1] == 1:
                    output = [0, 1, 0, 0]
                elif data[1] == 2:
                    output = [0, 0, 1, 0]
                elif data[1] == 3:
                    output = [0, 0, 0, 1]
                training_data.append([data[0], output])

        env.reset()

    print(accepted_scores)
    return training_data

def build_model(input_size, output_size):
    model = keras.Sequential([
    keras.layers.Dense(512, input_dim = input_size, activation = 'relu'),
    keras.layers.Dense(256, activation = 'relu'),
    keras.layers.Dense(256, activation = 'relu'),
    keras.layers.Dense(output_size, activation = 'softmax')
    ])
    model.compile(loss = 'mse', optimizer = 'Adam')
    return model

def train_model(training_data):
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]))
    y = np.array([i[1] for i in training_data]).reshape(-1, len(training_data[0][1]))
    model = build_model(input_size=len(X[0]), output_size = len(y[0]))
    model.fit(X, y, epochs = 500)
    return model

training_data = model_data_preparation()
trained_model = train_model(training_data)


scores = []
choices = []
for each_game in range(100):
    score = 0
    prev_obs = []
    for step_index in range(goal_steps):
        env.render()
        if len(prev_obs) == 0:
            action = random.randrange(0,2)
        else:
            action = np.argmax(trained_model.predict(prev_obs.reshape(-1, len(prev_obs)))[0])

        choices.append(action)
        new_observation, reward, done, info = env.step(action)
        prev_obs = new_observation
        score += reward
        if done:
            break

    env.reset()
    scores.append(score)

print(scores)
print('Average Score:', sum(scores)/len(scores))
print('choice 1:{}  choice 0:{}'.format(choices.count(1)/len(choices),choices.count(0)/len(choices)))


# for step_index in range(1000):
#     env.render()
#     action = env.action_space.sample()
#     observation, reward, done, info = env.step(action)
#     print("Step {}:".format(step_index))
#     print("action: {}".format(action))
#     print("observation: {}".format(observation))
#     print("reward: {}".format(reward))
#     print("done: {}".format(done))
#     print("info: {}".format(info))
#     if done:
#         env.close()
#         break
