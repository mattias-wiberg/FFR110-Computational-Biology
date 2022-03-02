import matplotlib.pyplot as plt
from random import random
from tqdm import tqdm
import numpy as np

# (b_n, d_n)
bd = [(0.1, 0.2), (1, 2), (10, 5)]
idx_case = 0
dt = 0.01
n_samples = 1000000
td = []
tb = []

def run_sample_single():
    j = 0
    pb = 0
    pd = 0
    while True:
        r1, r2 = random(), random()
        if r1 < pb and r2 < pd:
            j = 0
            pb = 0
            pd = 0
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
        elif r2 < pd:
            if d_happened:
                td.append(j)
                break
            d_happened = True
            b_happened = False
        # Increase probs
        pb += bd[idx_case][0] * dt
        pd += bd[idx_case][1] * dt
        j += dt

def plot():
    fig, ax = plt.subplots(2, sharey=True, sharex=True)

    ax[0].set_title(rf"$t_b$, $b_n$={bd[idx_case][0]}")
    ax[0].hist(tb, density=True)
    """
    freq, bins, patches = plt.hist(tb, density=True)
    freq = np.log(freq)
    new_bins = []
    for i in range(1,len(bins)):
        new_bins.append((bins[i-1] + bins[i])/2)
    ax[0].plot(new_bins, freq)
    ax[0].plot(np.linspace(min(new_bins),max(new_bins)), np.exp(-np.linspace(min(new_bins),max(new_bins))*bd[idx_case][0]))
    """

    ax[1].set_title(rf"$t_d$, $d_n$={bd[idx_case][1]}")
    ax[1].hist(td, density=True)

    """
    freq, bins, patches = plt.hist(td, density=True)
    freq = np.log(freq)
    new_bins = []
    for i in range(1,len(bins)):
        new_bins.append((bins[i-1] + bins[i])/2)
    ax[1].plot(new_bins, freq)
    """

    fig.tight_layout()  
    plt.show()

for i in tqdm(range(n_samples)):
    run_sample_double()
#plot()
print(f"td: {np.round(100*len(td)/(len(td)+len(tb)),2)} % tb: {np.round(100*len(tb)/(len(td)+len(tb)),2)} %")
print(f"mean(tb): {np.round(np.mean(np.array(tb))*1000, 2)} ms")
print(f"mean(td): {np.round(np.mean(np.array(td))*1000, 2)} ms")


