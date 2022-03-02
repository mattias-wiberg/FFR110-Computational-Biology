import matplotlib.pyplot as plt
from random import random
from tqdm import tqdm
import numpy as np
from collections import Counter

# (b_n, d_n)
bd = [(0.1, 0.2), (1, 2), (10, 5)]
idx_case = 2
dt = 0.01
n_samples = 1000000
td = []
tb = []

def get_t(rate, double = False):
    j = 0
    p = 0
    happened = False
    while True:
        if random() < p:
            if not double:
                return j
            elif happened and double:
                return j
            elif not happened and double:
                happened = True
                p = 0
        p += rate * dt
        j += dt

def run_sample_single():
    j = 0
    pb = 0
    pd = 0
    while True:
        r1, r2 = random(), random()
        if r1 < pb and r2 < pd:
            run_sample_single()
            return
        elif r1 < pb:
            tb.append(j)
            break
        elif r2 < pd:
            td.append(j)
            break
        # Increase probs
        pb += bd[idx_case][0] * dt
        pd += bd[idx_case][1] * dt
        j += dt

def run_sample_double():
    j = 0
    pb = 0
    pd = 0
    b_happened = False
    d_happened = False
    while True:
        r1, r2 = random(), random()
        if r1 < pb and r2 < pd:
            j = 0
            pb = 0
            pd = 0
            b_happened = False
            d_happened = False
        elif r1 < pb:
            if b_happened:
                tb.append(j)
                break
            b_happened = True
            d_happened = False
            pb = 0
        elif r2 < pd:
            if d_happened:
                td.append(j)
                break
            d_happened = True
            b_happened = False
            pd = 0
        # Increase probs
        pb += bd[idx_case][0] * dt
        pd += bd[idx_case][1] * dt
        j += dt

def plot():
    fig, ax = plt.subplots(2, sharey=True, sharex=True)

    ax[0].set_title(rf"$t_b$, $b_n$={bd[idx_case][0]}")
    tb_count = np.array(sorted(Counter(tb).items()))
    tb_count[:,1] = np.log(tb_count[:,1]/np.sum(tb_count[:,1]))
    ax[0].plot(tb_count[:,0], tb_count[:,1])
    ax[0].plot(tb_count[:,0], np.log(np.exp(-bd[idx_case][0]*tb_count[:,0]))+tb_count[0,1])
    ax[0].plot(tb_count[:,0], np.log(np.exp(bd[idx_case][0]*tb_count[:,0]))+tb_count[0,1])
    ax[0].plot(tb_count[:,0], np.exp(bd[idx_case][0]*tb_count[:,0])+tb_count[0,1])
    ax[0].plot(tb_count[:,0], np.exp(-bd[idx_case][0]*tb_count[:,0])+tb_count[0,1])
    ax[0].plot(tb_count[:,0], -np.exp(bd[idx_case][0]*tb_count[:,0])+tb_count[0,1])
    ax[0].plot(tb_count[:,0], -np.exp(-bd[idx_case][0]*tb_count[:,0])+tb_count[0,1])

    
    ax[1].set_title(rf"$t_d$, $d_n$={bd[idx_case][1]}")
    td_count = np.array(sorted(Counter(td).items()))
    td_count[:,1] = np.log(td_count[:,1]/np.sum(td_count[:,1]))
    ax[1].plot(td_count[:,0], td_count[:,1])

    fig.tight_layout()  
    plt.show()

#tb_2 = []
#td_2 = []
for i in tqdm(range(n_samples)):
    #run_sample_single()
    #run_sample_double()
    tb.append(get_t(bd[idx_case][0], True))
    td.append(get_t(bd[idx_case][1], True))

plot()
print(f"td: {np.round(100*len(td)/(len(td)+len(tb)),2)} % tb: {np.round(100*len(tb)/(len(td)+len(tb)),2)} %")
print(f"mean(tb): {np.round(np.mean(np.array(tb))*1000, 2)} ms")
print(f"mean(td): {np.round(np.mean(np.array(td))*1000, 2)} ms")


