
import gym #cargamos la librería de openAIgym
#BipedalWalker-v3
#MountainCar-v0
environment = gym.make("CarRacing-v0") #lanzamos una instancia del videojuego de la montaña rusa 
environment.reset() #limpiamos y preparamos el enterno para tomar decisiones
for _ in range(2000): #durante 2000 iteraciones 
   environment.render() #pintamos en pantalla la acción
   environment.step(environment.action_space.sample())  #tomamos una decision aleatoria del conjunto de las disponibles
#print(environment.o