# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:59:22 2020

@author: 
"""


#Qlearnerclass 
# __init__(self, environment)
#discretize(self, obs) dividir en rangos de valores [-2,2] -> [-2,-1],[-1,0],[0,1],[1,2]
#get_action(self, obs)
#learn(self, obs, reward, next_obs)
#train
#test

import gym # se carga o importa la libreria de OpenAI Gym
import numpy as np # se carga o importa la libreria numpy

#Hiperparametros
MAX_NUM_EPISODES = 30000 # Es el número máximo de iteraciones que estamos dispuestos a realizar
STEPS_PER_EPISODE = 200 # Numero máximo de pasos a realizar en cada episodio (es el objetivo a batir)
EPSILON_MIN = 0.005 # Es el valor mas pequeño que se utiliza para llevar a cabo el aprendizaje.
max_num_steps = MAX_NUM_EPISODES * STEPS_PER_EPISODE #Calcula el decremento del epsilon de un paso al otro
EPSILON_DECAY = 500 * EPSILON_MIN / max_num_steps #Caida de epsilon de un paso al siguiente
ALPHA = 0.05 # Es el ratio de aprendizaje del agente 
GAMMA = 0.98 # Es el factor de descuento del agente lo que vamos perdiendo de un paso a otro para incentivar al agente a llegar al objetivo
NUM_DISCRETE_BINS = 30 # Numero de divisiones o etapas en el caso de discretizar el espacio de estados continuo

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
        
    # CREACIÓN DE MÉTODO PARA APRENDER

    # Se define la función que permitirá al agente poder añadir el conocimiento
    # a esta función se le pasan los parametros 'self', 'obs', 'action', 'reward', 'next_obs'
    # los cuales se definen en las funciones anteriores ya creadas 
    def learn(self, obs, action, reward, next_obs):
        # Se inicializa una variable para almacenar un nuevo valor creado 
        discrete_obs = self.discretize(obs)
        discrete_next_obs = self.discretize(next_obs)
         # Se inicializa una nueva variable la cual almacenará la recompenza obtenida hasta el momento 
        td_target = reward + self.gamma * np.max(self.Q[discrete_next_obs])
        # Si se encuentra con algún error se guardará en una variable para indicar dónde se generó
        td_error = td_target - self.Q[discrete_obs][action]
        # Se guardará la acción o el error
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

#queremos ser capaces de medir como ha ido todo lo que ha aprendido sometiendolo a una prueba, un test
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
    environment = gym.make("MountainCar-v0") # Aqui el usuario debe llenar al script con el nombre del entorno como parametro
    agent = Qlearner(environment) # Objeto de la clase Qlearner
    monitor_path = "./monitor_output" # Es el metodo que se utiliza para entrenar al agente y luego guardar esos archivos de video para luego ver el resultado final
    environment = gym.wrappers.Monitor(environment, monitor_path, force = True) # Realiza el monitoreo mediante el entorno y asi guarde todos los clips
    learned_policy = train(agent, environment) #Se encarga de devolver el resultado del entrenamiento del agente
    for _ in range(1000): # Se testea ese numero de veces para ver si el agente es capaz de llegar a la banderita 
        test(agent, environment, learned_policy) # y asi lo guardara
    environment.close() # fin del metodo de cargar y guardar
    