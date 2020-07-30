# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:23:46 2020

@author: Toshiba Elvira
"""

 #METODO PARA ENTRENAR AL AGENTE     
def train(agent, environment):   # aqui definimos el metodo train en la cual tendremos un agente y un enrtorno que es enviroment
       best_reward = -float('inf')   # definimos la mejor recompensa que sera menos float infinito 
       for episode in range(MAX_NUM_EPISODES):   # definimos los episodios 
        done  = False     #definimos la variable done por defecto es false
        obs = environment.reset() #
        total_reward = 0.0 # recompensa total acomulado en 0
    while not done:   # definimos un bucle la cual mientras no hayamos finalizado la ejecusion 
            action = agent.get_action(obs)   # accion elegida segun la ecuacion de Q-learning
            next_obs, reward, done, info = environment.step(action)  # definimos los parametros y hara que el enviroment ejecute el .step
            agent.learn(obs, action, reward, next_obs)   #con esta accion hacemos que el agente aprenda en base a la observacion
            obs = next_obs   # esta es la siguiente observacion para ejecutar el siguiente paso
            total_reward += reward  # la recompensa se incrementa
    if total_reward > best_reward: #fijamos si la recompensa total supera a la actual
            best_reward = total_reward  # entonces sera recompensa anterior es igual a la recompensa actual.
print("Episodio número {} con recompensa: {}, mejor recompensa: {}, epsilon: {}".format(episode, total_reward, best_reward, agent.epsilon)) #aqui imprimimos el episodio y el epsilon para ver con que valor termina
        
## de todas las politicas de entrenamiento que se han obtenido se devuelve laa mejor de todas
return np.argmax(agent.Q, axis = 2) 