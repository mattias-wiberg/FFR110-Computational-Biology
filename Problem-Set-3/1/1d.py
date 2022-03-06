import numpy as np
from tqdm import tqdm
import pickle

bd = [(0.1, 0.2), (1, 2), (10, 5)]
idx_case = 2
tb = pickle.load(open(f"tb_{bd[idx_case][0]}.p", "rb" ))
td = pickle.load(open(f"td_{bd[idx_case][1]}.p", "rb" ))

# beta = alpha/2
n0 = 3
N = 6
R = 100
dt = 0.01
Tmax = 50
max_index = int(Tmax/dt)

n = np.zeros((R,max_index))
n[:,0] = n0
T_ext = []

for real in tqdm(range(R)):
    index = 0
    while index < max_index:
        picks = [np.random.choice(td), np.random.choice(tb)]
        pick = np.min(picks)
        pick_index = picks.index(pick)
        pick = int(pick/dt)
        if index+pick > max_index - 1:
            break
        if pick_index == 0: # Death
            n[real,index:index+pick] = n[real,index]
            new_n = n[real,index] - 1
            n[real,index+pick] = new_n
            if new_n == 0:
                # Extinction
                index += pick
                T_ext.append(index*dt)
                break
        elif pick_index == 1: # Birth
            n[real,index:index+pick] = n[real,index]
            new_n = n[real,index] + 1
            if new_n > N:
                n[real,index+pick] = n[real,index]
            else:
                n[real,index+pick] = new_n
        index += pick
    n[real,index:] = n[real,index]

avg_t_ext = round(sum(T_ext)/len(T_ext),2)
print(f"Avgerage Text: {avg_t_ext} ({len(T_ext)} entries)")

pickle.dump(n, open(f"n0_{n0}_N_{N}_Text_{avg_t_ext}_b_{bd[idx_case][0]}_d_{bd[idx_case][1]}.p", "wb" ) )

