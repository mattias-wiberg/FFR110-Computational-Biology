import numpy as np
import matplotlib.pyplot as plt

N = 100
K = 5
O = np.random.uniform(-np.pi/2, np.pi/2, N)
w = np.random.standard_cauchy(N)
T = 1000
dt = 0.01
r = []

"""
def g(w, gamma=1):
    return gamma/(np.pi*(w*w+gamma**2))
"""

def dOidt(i):
    return w[i] + K*np.mean(np.sin(O-O[i]))

for t in np.arange(0, T, dt):
    Otmp = np.copy(O)
    for i in range(N):
        Otmp[i] += dt*dOidt(i)
    O = np.copy(Otmp) 
    # Sum vectors
    r_vec = np.sum([np.sin(O),np.cos(O)], axis=1)/N
    r.append(np.linalg.norm(r_vec))
    if(t*100)%1000==0:
        print(t, np.linalg.norm(r_vec))

plt.plot(np.arange(0,T,dt),r)