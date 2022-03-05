import matplotlib.pyplot as plt
from random import random
import numpy as np
from collections import Counter
import pickle
import scipy.stats as stats
import math

n = pickle.load(open("n0_3_N_6_Text_8.44_b_10_d_5.p", "rb" ))
dt = 0.01
seconds_to_plot = [10, 14.71, 20]
index_to_plot = list(map(lambda i:int(i/dt), seconds_to_plot))

def plot():
    fig, ax = plt.subplots(3, sharey=True, sharex=True)

    ax[0].set_title(r"$n_0=3, N=6, T_{ext}\approx 14.71, b_n=10, d_n=5$", fontsize=15)
    ax[0].set_xlabel("n infected", fontsize=13)
    count = np.array(sorted(Counter(n[:,index_to_plot[0]]).items()))
    count[:,1] = count[:,1]/np.sum(count[:,1])
    ax[0].plot(count[:,0], -np.log(count[:,1]), label=r"$-n \log P(n_{%s})$" % seconds_to_plot[0])
    #gauss = np.log(stats.norm.pdf(count[:,0], np.mean(count[:,0]), np.std(count[:,0])))
    #gauss = np.log(stats.norm.pdf(n[:,index_to_plot[0]], np.mean(n[:,index_to_plot[0]]), np.std(n[:,index_to_plot[0]])))
    #diff = -np.log(count[0,1]) - gauss[0]
    gauss = stats.norm.pdf(np.sort(n[:,index_to_plot[0]]), np.mean(np.sort(n[:,index_to_plot[0]])), np.std(np.sort(n[:,index_to_plot[0]])))
    gauss = np.log(gauss)
    diff = -np.log(count[0,1]) - gauss[0]
    ax[0].plot(np.sort(n[:,index_to_plot[0]]), gauss + diff, label=rf"Gaussian $\mu={np.mean(np.sort(n[:,index_to_plot[0]]))}$")

    ax[1].set_xlabel("n infected", fontsize=13)
    count = np.array(sorted(Counter(n[:,index_to_plot[1]]).items()))
    count[:,1] = count[:,1]/np.sum(count[:,1])
    ax[1].plot(count[:,0], -np.log(count[:,1]), label=r"$-n \log P(n_{%s})$" % seconds_to_plot[1])
    #gauss = np.log(stats.norm.pdf(count[:,0], np.mean(count[:,0]), np.std(count[:,0])))
    #diff = -np.log(count[0,1]) - gauss[0]
    gauss = stats.norm.pdf(np.sort(n[:,index_to_plot[1]]), np.mean(np.sort(n[:,index_to_plot[1]])), np.std(np.sort(n[:,index_to_plot[1]])))
    gauss = np.log(gauss)
    diff = -np.log(count[0,1]) - gauss[0]
    ax[1].plot(np.sort(n[:,index_to_plot[1]]), gauss + diff, label=rf"Gaussian $\mu={np.mean(np.sort(n[:,index_to_plot[1]]))}$")
    #ax[1].plot(count[:,0], gauss + diff, label="Gaussian")

    ax[2].set_xlabel("n infected", fontsize=13)
    count = np.array(sorted(Counter(n[:,index_to_plot[2]]).items()))
    count[:,1] = count[:,1]/np.sum(count[:,1])
    ax[2].plot(count[:,0], -np.log(count[:,1]), label=r"$-n \log P(n_{%s})$" % seconds_to_plot[2])
    #gauss = np.log(stats.norm.pdf(count[:,0], np.mean(count[:,0]), np.std(count[:,0])))
    #diff = -np.log(count[0,1]) - gauss[0]
    #ax[2].plot(count[:,0], gauss + diff, label="Gaussian")
    gauss = stats.norm.pdf(np.sort(n[:,index_to_plot[2]]), np.mean(np.sort(n[:,index_to_plot[2]])), np.std(np.sort(n[:,index_to_plot[2]])))
    gauss = np.log(gauss)
    diff = -np.log(count[0,1]) - gauss[0]
    ax[2].plot(np.sort(n[:,index_to_plot[2]]), gauss + diff, label=rf"Gaussian $\mu={np.mean(np.sort(n[:,index_to_plot[2]]))}$")

    ax[0].legend()
    ax[1].legend()
    ax[2].legend()
    plt.show()

plot()

x = 5

