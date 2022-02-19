import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

N = 3000
gamma = 1
K = [1,2.1,10]*gamma
K = K[2]
O = np.random.uniform(-np.pi/2, np.pi/2, N)
w = np.random.standard_cauchy(N)
T = 50
dt = 0.01
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
plt.xlabel("t")
plt.ylabel("r")
plt.show()