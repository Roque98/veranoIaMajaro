# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import gym
environment=gym.make("MountainCar-v0")
MAX_NUM_EPISODES=1000

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
      def_init_(self, environment):
         self.obs_shape=environment.observation_space.shape
         self.obs_high=enviroment.observation_space.high
         self.obs_low=enviroment.observation_space.low
         self.obs_bins=NUM_DISCRETE_BINS
         self.obs_width=(self.obs_high-self.obs_low)/self.obs_bins
         
         self.action_shape=environment.action_space.n
         self.Q=np, zeros((self.obs_bins+1, self.obs_bins+1,))
         
          
          
          
          
          
          
          
  
  
       
       
       
       
        
        