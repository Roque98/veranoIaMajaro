import gym
import sys

def run_gym_enviroment(argv):
	## 
	enviroment = gym.make(argv[1])
	enviroment.reset()
	for _ in range(int(argv[2])):
		enviroment.render()
		enviroment.step(enviroment.action_space.sample())
	enviroment.close()

if __name__ == "__main__":
	run_gym_enviroment(sys.argv)