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





if __name__ == "__main__":  
    environment = gym.make("MountainCar-v0") # Aqui el usuario debe llenar al script con el nombre del entorno como parametro
    agent = Qlearner(environment) # Objeto de la clase Qlearner
    monitor_path = "./monitor_output" # Es el metodo que se utiliza para entrenar al agente y luego guardar esos archivos de video para luego ver el resultado final
    environment = gym.wrappers.Monitor(environment, monitor_path, force = True) # Realiza el monitoreo mediante el entorno y asi guarde todos los clips
    learned_policy = train(agent, environment) #Se encarga de devolver el resultado del entrenamiento del agente
    for _ in range(1000): # Se testea ese numero de veces para ver si el agente es capaz de llegar a la banderita 
        test(agent, environment, learned_policy) # y asi lo guardara
    environment.close() # fin del metodo de cargar y guardar