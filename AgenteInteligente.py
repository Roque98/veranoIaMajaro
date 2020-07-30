# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:59:22 2020

@author: Martin
"""


#Qlearnerclass 
# __init__(self, environment)
#discretize(self, obs) dividir en rangos de valores [-2,2] -> [-2,-1],[-1,0],[0,1],[1,2]
#get_action(self, obs)
#learn(self, obs, reward, next_obs)
#train
#test

#Hiperparámetros
#EPSILON_MIN vamos aprendiendo mienttras el incremento de aprendizaje sea superior a dicho valor 
#MAX_NUM_EPISODES número máximo de iteraciones que estamos dispuestos a realizar
#STEPS_PER_EPISODE numero máximo de pasos a realizar en cada episodio
#max_num_steps = MAX_NUM_EPISODES * STEPS_PER_EPISODE
#EPSILON_DECAY = 500 * EPSILON_MIN / max_num_steps caida de epsilon de un paso al siguiente
#ALPHA ratio de aprendizaje del agente 
#GAMMA factor de descuento del agente lo que vamos perdiendo para incentivar al agente a llegar al objetivo
#NUM_DISCRETE_BINS npumero de divisiones en el caso de discretizar el espacio de estados continuo


import gym 
import numpy as np

MAX_NUM_EPISODES = 30000
STEPS_PER_EPISODE = 200
EPSILON_MIN = 0.005
max_num_steps = MAX_NUM_EPISODES * STEPS_PER_EPISODE
EPSILON_DECAY = 500 * EPSILON_MIN / max_num_steps
ALPHA = 0.05
GAMMA = 0.98
NUM_DISCRETE_BINS = 30

import numpy as np

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
        self.Q[discrete_obs][action] += self.alpha*td_error
        
        
        
        
def train(agent, environment):
    best_reward = -float('inf')
    for episode in range(MAX_NUM_EPISODES):
        done  = False
        obs = environment.reset()
        total_reward = 0.0
        while not done:
            #environment.render()
            action = agent.get_action(obs)
            next_obs, reward, done, info = environment.step(action)
            agent.learn(obs, action, reward, next_obs)
            obs = next_obs
            total_reward += reward
        if total_reward > best_reward:
            best_reward = total_reward
        print("Episodio número {} con recompensa: {}, mejor recompensa: {}, epsilon: {}".format(episode, total_reward, best_reward, agent.epsilon))
        
        
    return np.argmax(agent.Q, axis = 2)

#queremos ser capacez de medir como ha ido todo lo que ha aprendido sometiendolo a una prueba, un test
def test(agent, environment, policy): #dado el agente, dado el entorno y dada la política de actuación ver como la ha ido
    #devolver la recompensa global del episodio
    #en este caso no le dejamos que actualice el valor de qlearning
    done = False 
    obs = environment.reset()
    total_reward = 0.0
    while not done:
        action = policy[agent.discretize(obs)] #la acció no la hacemos ni aleatoria ni con el ratio de aprendizaje sino con la política
        #acción que dictamina la política que hemos entrenado
        #parecido al get_action mediante una observación con la política de acuerdo al lugar dónde se encuentra
        next_obs, reward, done, info = environment.step(action) #los psrámetros con el entorno con los pasos de esa acción
        total_reward += reward #concatenamos la recompensa total anterior mas la recompensa nueva actual
    return total_reward #regresamos nuestra recompensa total

if __name__ == "__main__":
    environment = gym.make("MountainCar-v0")
    agent = Qlearner(environment)
    monitor_path = "./monitor_output"
    environment = gym.wrappers.Monitor(environment, monitor_path, force = True)
    learned_policy = train(agent, environment)
    for _ in range(1000):
        test(agent, environment, learned_policy)
    environment.close()

