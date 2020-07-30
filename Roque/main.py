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

class Qlearner(object):
    def __init__(self, environment):
        self.obs_shape = environment.observation_space.shape
        self.obs_high = environment.observation_space.high
        self.obs_low = environment.observation_space.low
        self.obs_bins = NUM_DISCRETE_BINS
        self.bin_width = (self.obs_high-self.obs_low)/self.obs_bins
        
        self.action_shape = environment.action_space.n
        self.Q = np.zeros((self.obs_bins+1, self.obs_bins+1, self.action_shape))
        self.alpha = ALPHA
        self.gamma = GAMMA
        self.epsilon = 1.0
        
    def discretize(self, obs):
        return tuple(((obs-self.obs_low)/self.bin_width).astype(int))
    
    def get_action(self, obs):
        discrete_obs = self.discretize(obs)
        if self.epsilon > EPSILON_MIN:
            self.epsilon -= EPSILON_DECAY
        if np.random.random() > self.epsilon:
            return np.argmax(self.Q[discrete_obs])
        else:
            return np.random.choice([a for a in range(self.action_shape)])
                
    def learn(self, obs, action, reward, next_obs):
        discrete_obs = self.discretize(obs)
        discrete_next_obs = self.discretize(next_obs)
        td_target = reward + self.gamma * np.max(self.Q[discrete_next_obs])
        td_error = td_target - self.Q[discrete_obs][action]
        print(f'td_rror: {td_error}')
        self.Q[discrete_obs][action] += self.alpha*td_error
               
def train(agent, environment):
    best_reward = -float('inf')
    for episode in range(MAX_NUM_EPISODES):
        done  = False
        obs = environment.reset()
        total_reward = 0.0
        while not done:
            action = agent.get_action(obs)
            next_obs, reward, done, info = environment.step(action)
            agent.learn(obs, action, reward, next_obs)
            obs = next_obs
            total_reward += reward
        if total_reward > best_reward:
            best_reward = total_reward
        print("Episodio número {} con recompensa: {}, mejor recompensa: {}, epsilon: {}".format(episode, total_reward, best_reward, agent.epsilon))
        
        
    return np.argmax(agent.Q, axis = 2)

def test(agent, environment, policy):
    done = False
    obs = environment.reset()
    total_reward = 0.0
    while not done:
        action = policy[agent.discretize(obs)]
        next_obs, reward, done, info = environment.step(action)
        total_reward += reward
    return total_reward


if __name__ == "__main__":
    environment = gym.make("MountainCar-v0")
    agent = Qlearner(environment)
    monitor_path = "./monitor_output2"
    environment = gym.wrappers.Monitor(environment, monitor_path, force = True)
    learned_policy = train(agent, environment)
    for _ in range(1000):
        test(agent, environment, learned_policy)
    environment.close()