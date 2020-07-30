# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import gym
environment=gym.make("MountainCar-v0") #cargar el entorno
MAX_NUM_EPISODES=1000 #numero maximo de episodios
STEPS_PER_EPISODE=200

for episode in range(MAX_NUM_EPISODES): 
    done=False
    obs=environment.reset() 
    total_reward=0.0 ## variable para guardar la recompensa total obtenida en cada episodio
    step=0
    while not done:
        environment.render()
        action=environment.action_space.sample()#accion aleatorio, que posteriormente reemplazaremos por la decision de nuestro agente inteligente
        next_state, reward, done, info=environment.step(action)
        total_reward +=reward
        step +=1
        obs=next_state
        
        print("\n Episodio número {} finalizado con {} iteraciones, Recompensa final={}".format(episode, step+1, total_reward)) 
  
    environment.close()
  
  
 
    
  
  
  
    
    
    
    
    
EPSILON_MIN=0.05
max_num_steps=MAX_NUM_EPISODES*STEPS_PER_EPISODE
EPSILON_DECAY=500*EPSILON_MIN/max_num_steps
ALPHA=0.05
GAMMA=0.98
NUM_DISCRETE_BINS=30
  
import numpy as np
  
class QLearner(objets):
       def __init__(self, environment):# self es suna referencia del propio objeto
         self.obs_shape=environment.observation_space.shape
         self.obs_high=enviroment.observation_space.high
         self.obs_low=enviroment.observation_space.low
         self.obs_bins=NUM_DISCRETE_BINS
         self.obs_width=(self.obs_high-self.obs_low)/self.obs_bins
         
         self.action_shape=environment.action_space.n
         self.Q=np, zeros((self.obs_bins+1, self.obs_bins+1, self.action_shape)) #matriz de 31 x 31 x 3
         self.alpha=ALPHA
         self.gamma=GAMMA
         self.epsilon=1.0
         
         
         
         
         def discretize(self, obs) : #metodo de discretizacion 
          return tuple (((obs-self.obs_low)/self.bin_width).astype(int))
             
             
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
    monitor_path = "./monitor_output"
    environment = gym.wrappers.Monitor(environment, monitor_path, force = True)
    learned_policy = train(agent, environment)
    for _ in range(1000):
        test(agent, environment, learned_policy)
    environment.close()
         
         
         
         
          
          
          
          
          
          
          
  
  
       
       
       
       
        
        