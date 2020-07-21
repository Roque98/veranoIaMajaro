
import gym
env = gym.make("Taxi-v3")

state = env.reset()
counter = 0
reward = None

while reward != 20:
    state, reward, done, info = env.step(env.action_space.sample())
    counter += 1

print(counter)