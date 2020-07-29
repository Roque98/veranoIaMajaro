import gym
import numpy as np
import tkinter as tk
import threading

## https://github.com/openai/gym
## https://gym.openai.com/docs/

## https://gym.openai.com/envs/MountainCarContinuous-v0/
## https://github.com/openai/gym/wiki/MountainCar-v0

silent = False
def printif(string):
    if not silent: print(string)

def saveQ(name='_Checkpoint', txtCopy=False):
    # Saves a copy of the Q-table in numpy's .npy format, and optionally in .txt format.
    # path = r"D:\\Coding\\Machine Learning\\OpenAI Gym\\MountainCar\\"
    path = r"C:\\Users\\LUIS\\ReposValla\\veranoIaMajaro\\Valladares\\"
    np.save(path + "MC_Qtable" + name + ".npy", Q)
    np.savetxt(path + "MC_Qtable" + name + ".txt", Q)

def loadQ(name='_Checkpoint'):
    # Loads a saved Q-table
    path = r"C:\\Users\\LUIS\\ReposValla\\veranoIaMajaro\\Valladares\\"
    # path = r"D:\\Coding\\Machine Learning\\OpenAI Gym\\MountainCar\\"
    return np.load(path + "MC_Qtable" + name + ".npy")



# Load environment
env = gym.make('MountainCar-v0')
#env = gym.make('MountainCarContinuous-v0')


## Environment Notes ##
# obsvs come in a two-dim vector (p, v)
# p = Car position: -1.2 <= p <= 0.6
# v = Car velocity: -0.07 <= v <= 0.07
#
# Action space is [0, 1, 2] where 0=left, 1=nothing, 2=right
# In the non-continuous MountainCar environment, the car is given a fixed impulse in the chosen direction.

# Action space variables
a_N = env.action_space.n

# State space variables
s_velocitybins = [round(-0.07 + 0.01*i, 2) for i in range(0, 14)]
s_positionbins = [round(-1.2 + 0.1*i, 1) for i in range(0, 18)]
s_N = len(s_velocitybins) * len(s_positionbins)

# Initialize Q-table
Q = np.zeros((s_N, a_N))

# Load a Q-table here if needed
#Q = loadQ()
ep_offset = 0

# Set hyperparameters
episodes = 10000
alpha = 0.8   # learning rate
gamma = 0.95  # discount factor

#############################

def getRowIndex(state):
    s_positionbins_ext = s_positionbins + [0.60001]  # add right endpoint to bins to help loop indexing
    s_velocitybins_ext = s_velocitybins + [0.070001]
    # States are indexed by position first, then velocity. So all states with position -1.2 <= p < -1.1 would occupy the first k indices.
    for i in range(len(s_positionbins)):
        if (state[0] >= s_positionbins_ext[i]) and (state[0] < s_positionbins_ext[i+1]):  # Position

            # Once the position bin is found and stored in i, move on to find velocity bin.
            for j in range(len(s_velocitybins)):
                if (state[1] >= s_velocitybins_ext[j]) and (state[1] < s_velocitybins_ext[j+1]):  # Velocity
                    return i*len(s_velocitybins) + j

            raise RuntimeError("Velocity state outside bounds of s_velocitybins.")
            return -1

    raise RuntimeError("Position state outside bounds of s_positionbins.")
    return -1

def mapToColor(x):
    # Takes a Q-table value in [-20, 0] and maps it to a BLUE color value in [0, 255].
    # R and G channels are fixed:
    R = '52'
    G = '0C'

    # If the input is 0, maps to X.
    x = int(x)
    if (x == 0):
        RGB = '#b0b0b0'
    else:
        B = round( (255/20)*x + 255 )
        RGB = '#' + R + G + '{:0>2}'.format(hex(B)[2:])

    return RGB


tableUpdated = False

def QTableRedraw(Q, W, H, W_scale, H_scale, s_N, a_N):
    image = tk.PhotoImage(width=W, height=H)
    # Get current Q-table, transpose it, and use it to color pixels
    Q_t = Q.transpose()

    for s in range(s_N):
        for a in range(a_N):

            for x in range(W_scale):
                for y in range(H_scale):
                    color = mapToColor(Q_t[a][s])  # Generate color for Q-table value

                    image.put(color, (s*W_scale + x, a*H_scale + y))
    return image


# Create a separate thread to handle Q-table visualization UI
def QTableUI():
    # Load global update flag and Q-table
    global tableUpdated
    global Q

    # Create Tkinter Window
    master = tk.Tk()
    W_scale = 4
    H_scale = 30
    W = s_N * W_scale    # 'W_scale' horizontal pixels for each row of Q
    H = a_N * H_scale    # 'H_scale' vertical pixels for each column of Q
    # Create window and canvas
    canvas = tk.Canvas(master, width=W, height=H, bg="#000000")
    canvas.pack()

    # Create image to fill with pixels
    tableImg = QTableRedraw(Q, W, H, W_scale, H_scale, s_N, a_N)
    tableImgCanvas = canvas.create_image((W/2, H/2), image=tableImg, state="normal")


    while True:
        if tableUpdated:
            tableImg = QTableRedraw(Q, W, H, W_scale, H_scale, s_N, a_N)
            canvas.delete(tableImgCanvas)
            tableImgCanvas = canvas.create_image((W/2, H/2), image=tableImg, state="normal")
            tableUpdated = False

        # Draw lines to break up action segments
        canvas.create_line(0, 1*H_scale, W, 1*H_scale, fill='#b0b0b0', width=2)
        canvas.create_line(0, 2*H_scale, W, 2*H_scale, fill='#b0b0b0', width=2)

        # Update tk window (replaces tk.mainloop())
        master.update_idletasks()
        master.update()

try:
    QTableThread = threading.Thread(target=QTableUI)
    QTableThread.start()
except:
	print("Error: Unable to start UI thread.")

#############################


### Q-Learning Algorithm ###

for ep in range(ep_offset, episodes + ep_offset):

    ## Episode start ##
    obsv = env.reset()  # reset the environment and store initial state
    printif ("====+====+====+====+====+====+====+====+====")
    printif ("|-- Episode {} starting.".format(ep+1))

    t = 0
    total_reward = 0

    while True:
        env.render()

        ## Choose an action (with noise) ##
        noise = np.random.randn(1, a_N)*(1./(ep+1))**(0.75)  # Generate a random noise distribution for the 3-dim action vector that attenuates as episodes go on
        action = np.argmax( Q[getRowIndex(obsv), :] + noise )  # This noise causes exploration, so our algorithm will explore less over time

        last_obsv = obsv
        obsv, reward, done, _ = env.step(action)  # Feed action into env and observe result
        t += 1
        total_reward += reward

        # Update Q-table
        Q[getRowIndex(last_obsv), action] = (1 - alpha)*Q[getRowIndex(last_obsv), action] + alpha*(reward + gamma*np.max( Q[getRowIndex(obsv), :] ))
        tableUpdated = True


        if ((t % 50 == 0 and t>1) or done):
            printif ("| [t = {}]\tReward = {:.4f}".format(t, total_reward))

        if done:
            if (t < 200): success="\t\t< Success! >"
            else: success=""

            printif ("|-- Episode {} finished after {} timesteps.".format(ep+1, t) + success)
            break

    if ((ep+1) % 25 == 0):
        saveQ(txtCopy=True)
        printif ("|-- Q-table checkpoint saved.".format(t, total_reward))