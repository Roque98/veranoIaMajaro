import gym 
import numpy as np

MAX_NUM_EPISODES = 50000
STEPS_PER_EPISODE = 200
EPSILON_MIN = 0.005
max_num_steps = MAX_NUM_EPISODES * STEPS_PER_EPISODE
EPSILON_DECAY = 500 * EPSILON_MIN / max_num_steps
ALPHA = 0.05
GAMMA = 0.98
NUM_DISCRETE_BINS = 30

import numpy as np

if __name__ == "__main__":
    environment = gym.make("MountainCar-v0")
    agent = Qlearner(environment)
    monitor_path = "./monitor_output"
    environment = gym.wrappers.Monitor(environment, monitor_path, force = True)
    learned_policy = train(agent, environment)
    for _ in range(1000):
        test(agent, environment, learned_policy)
    environment.close()