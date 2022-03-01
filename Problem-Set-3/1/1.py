import matplotlib.pyplot as plt
from random import random
from tqdm import tqdm
import numpy as np

# (b_n, d_n)
bd = [(0.1, 0.2), (1, 2), (10, 5)]
idx_case = 2
dt = 0.01
n = 10
n_samples = 1000000
td = []
tb = []

for i in tqdm(range(n_samples)):
    j = 0
    pb = 0
    pd = 0
    while True:
        if random() < 0.5:
            if random() < pb:
                tb.append(j)
                break
            elif random() < pd:
                td.append(j)
                break
        else:
            if random() < pd:
                td.append(j)
                break
            elif random() < pb:
                tb.append(j)
                break
            
        # Increase probs
        pb += bd[idx_case][0] * dt
        pd += bd[idx_case][1] * dt
        j += dt
        

fig, ax = plt.subplots(2, sharey=True, sharex=True)

ax[0].set_title(rf"$t_b$, $b_n$={bd[idx_case][0]}, n={n}")
freq, bins, patches = plt.hist(tb, density=True)
freq = np.log(freq)
new_bins = []
for i in range(1,len(bins)):
    new_bins.append((bins[i-1] + bins[i])/2)
ax[0].plot(new_bins, freq)
# todo: subsequent
ax[0].plot(np.linspace(min(new_bins),max(new_bins)), np.exp(-np.linspace(min(new_bins),max(new_bins))*bd[idx_case][0]))

ax[1].set_title(rf"$t_d$, $d_n$={bd[idx_case][1]}, n={n}")
freq, bins, patches = plt.hist(td, density=True)
freq = np.log(freq)
new_bins = []
for i in range(1,len(bins)):
    new_bins.append((bins[i-1] + bins[i])/2)
ax[1].plot(new_bins, freq)

fig.tight_layout()  
plt.show()
