import matplotlib.pyplot as plt
from random import random
from tqdm import tqdm
import numpy as np
from collections import Counter
import pickle

# (b_n, d_n)
bd = [(0.1, 0.2), (1, 2), (10, 5)]
idx_case = 2
dt = 0.01
n_samples = 1000000
tb = []
td = []

def get_time(rate):
    time = dt
    while True:
        if random() < rate*dt:
            return time
        time += dt

def plot():
    fig, ax = plt.subplots(2, sharey=True, sharex=True)
    ax[0].set_yscale('log')
    ax[1].set_yscale('log')

    ax[0].set_title(rf"$P(t_b)$ vs. $t_b$ for $b_n$={bd[idx_case][0]}", fontsize=15)
    ax[0].set_ylabel(rf"$P(t_b)$", fontsize=15)
    ax[0].set_xlabel(rf"$t_b$ [s]", fontsize=15)
    tb_count = np.array(sorted(Counter(tb).items()))
    tb_count[:,1] = tb_count[:,1]/np.sum(tb_count[:,1])
    ax[0].plot(tb_count[:,0], tb_count[:,1], label=rf"$P(t_b)$")
    ax[0].plot(tb_count[:,0], np.exp(-bd[idx_case][0]*tb_count[:,0]), label=r"$e^{-%st}$" % bd[idx_case][0])

    ax[1].set_title(rf"$P(t_d)$ vs. $t_d$ for $d_n$={bd[idx_case][1]}", fontsize=15)
    ax[1].set_ylabel(rf"$P(t_d)$", fontsize=15)
    ax[1].set_xlabel(rf"$t_d$ [s]", fontsize=15)
    td_count = np.array(sorted(Counter(td).items()))
    td_count[:,1] = td_count[:,1]/np.sum(td_count[:,1])
    ax[1].plot(td_count[:,0], td_count[:,1], label=rf"$P(t_d)$")
    ax[1].plot(td_count[:,0], np.exp(-bd[idx_case][1]*td_count[:,0]), label=r"$e^{-%st}$" % bd[idx_case][1])

    ax[0].legend()
    ax[1].legend()
    plt.show()

for i in tqdm(range(n_samples)):
    tb.append(get_time(bd[idx_case][0]))
    td.append(get_time(bd[idx_case][1]))

print(f"mean(tb): {np.round(np.mean(np.array(tb)), 2)} s")
print(f"mean(td): {np.round(np.mean(np.array(td)), 2)} s")
plot()
#pickle.dump(tb, open(f"tb_{bd[idx_case][0]}.p", "wb"))
#pickle.dump(td, open(f"td_{bd[idx_case][1]}.p", "wb"))

