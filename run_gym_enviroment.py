import gym
import sys

def run_gym_enviroment(argv):
	## Inicia el entorno elegido con el primer parametro
	env = gym.make(argv[1])
	observation = env.reset()
	for _ in range(1000):
		env.render()
		action = env.action_space.sample() # your agent here (this takes random actions)
		observation, reward, done, info = env.step(action)

		if done:
			observation = env.reset()
	env.close()

if __name__ == "__main__":
	run_gym_enviroment(sys.argv)