import numpy as np
import tqdm as tqdm

td = np.array([1,2,3,4]) # TODO replace
tb = td*0.1 # TODO replace

alpha = 0.2
beta = 0.6
n_0 = 100
iterations = 1000

def model(iterations, n_0):
    n = [n_0] # Number of infected
    t = [0] # Time
    for _ in tqdm(range(iterations)):
        picks = [np.random.choice(td), np.random.choice(tb)]
        pick = np.min(picks)
        pick_index = picks.index(pick)
        if pick_index == 0: # Death
            n.append(n[-1]-1)
        elif pick_index == 1: # Birth
            n.append(n[-1]+1)
        t.append(pick)
    return n, t

