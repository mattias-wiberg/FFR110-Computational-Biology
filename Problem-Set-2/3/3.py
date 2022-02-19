import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

N = 300
gamma = 1
K = 2*gamma
O = np.random.uniform(-np.pi/2, np.pi/2, N)
w = np.random.standard_cauchy(N)
T = 0.5
dt = 0.0001
r = []


d0dt = np.zeros(N)
for t in tqdm(np.arange(0, T, dt)):
    for i in range(N):
        d0dt[i] = w[i] + K*np.mean(np.sin(O-O[i]))
    O += dt*d0dt
    # Sum vectors
    r_vec = np.mean([np.sin(O),np.cos(O)], axis=1)
    r.append(np.linalg.norm(r_vec))
    #print(t, np.linalg.norm(r_vec))

plt.plot(np.arange(0,T,dt),r)
plt.show()