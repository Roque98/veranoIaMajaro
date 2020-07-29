#Importamos lsa librerias que vamos a utilizar 
import gym 
import random
import numpy as np 
from keras.models import Sequential 
from keras.layers import Dense
from keras.optimizers import Adam 

env = gym.make('CartPole-v1') #creamos nuestro entorno de trabajo 
env.reset()
goals_steps=500 #definimos el numero de pasos para el entrenamiento 
score_requirement= 60 #puntuacion requerida 
intial_games = 10000 #Entrenamiento inicial 

#Funcion que ejecuta un bucle para hacer varias acciones para jugar 
#Intentaremos con 500 pasos como maximo 
def play_a_random_game_first():
    try:
        for step_index in range(goals_steps):
            #env.render() #Para representar el juego 
            action = env.action_space.simple()
            #Elegimos la accion al azar 
            #Resultados del paso anterior 
            observation, reward, done, info = env.step(action)
            print("paso {}:".format(step_index))
            print("Accion: {}".format(action))
            print("Obseervacion: {}".format(observation))
            print("Recompensa: {}".format(reward))
            print("Done: {}".format(done))
            print("Info: {}".format(info))
            if done:#Si juego competado 
                break
    finally:
                env.reset()

def model_data_preparation():
	training_data= [] #inicializamos los arreglos con los datos de  
	acepted_scores= [] #Entrenamiento y las puntuaciones 
	#Jugamos 10000 veces para obtener unos datos representativos 
	for game_index in range(intial_games):
		score =0 #inicializamos variables 
		game_memory = []
		previous_observation = []
		#indicamos que se ejecute 500 veces 
		for step_index in range(goals_steps):
			action = random.randrange(0,2)  #Accion aleatoria 
			observation, reward, done, info = env.step(action)
			#almacenamos puntuacion
		if len(previous_observation)> 0:
			game_memory.append([previous_observation,action])

			previous_observation = observation
			score += reward
			if done:
				break
		if score >= score_requirement:
			acepted_scores.append(score)
			for data in game_memory:
				if data[1] ==1:
					output=[0,1]
				elif data[1]==0:
					output=[1,0]
					training_data.append([data[0],output])

	#reseteamos el entorno y lo mostramos en pantalla
	env.reset()
	print(acepted_scores)
	return training_data

#Con esta funcion cosntruimos nuestro modelo osea nuestra red neuronal
def build_model(input_size, output_size):
	model = Sequential()
	model.add(Dense(128,input_dim=input_size, activation='relu'))
	model.add(Dense(52,activation='linear'))
	model.compile(loss='mse', optimizer=Adam())
	return model

def train_model(training_data):
    x= np.array([i[0]for i in training_data]).reshape(-1,len (training_data[0][0]))
    y= np.array([1[1]for i in training_data]).reshape(-1, len (training_data[0][1]))
    model = build_model(input_size=len(x[0]),output_size=len(y[0]))
    
    model.fit(x, y, epochs=10)
    return model

scores = []#inicializamos puntuaciones y arreglos de elecciones 
choices = []

for each_game in range(100): #jugamos 100 partidas 
    
    env.render()
    if len(prev_obs)==0:
        action = random.randrange(0,2)#en el primer paso elegimos los movimientos 
    else:
        #a partir del segundo paso conocemos el estado del juego actual 
        #entonces tomamos esa observacion y se la damos a nuestro 
        #modelo para predecir que accion debemos tomar 
        action =np.argmax(trained_model.predict(prev_obs.reshape(-1, len)))