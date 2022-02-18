# %%
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
plt.ion()

# Define parameters
p = 0.5 # rho dimless
q = 8 # dimless
t = 0.1 # Tau step size dimless
h = 1 # Step size
L = 100 # Habitat size
tau_max = 3000


def pop_init_ramp(u0, x0, L):
    return u0/(1+np.exp(np.arange(L)+1-x0))

def pop_init_smooth(u0, x0, L):
    return u0*np.exp(-((np.arange(L)+1-x0)**2))

def diffusion(u, L, h):
    # u = Rabits at all positions at tau
    ret = np.zeros(len(u)) 
    for i in np.arange(h,L-h):
        ret[i] = (u[i+h]+u[i-h]-2*u[i])/h**2
    return ret

def derivative(u, L, h):
    # u = Rabits at all positions at tau
    ret = np.zeros(len(u)) 
    for i in np.arange(h,L-h):
        ret[i] = (u[i-h]-u[i+h])/(2*h)
    return ret

# Returns next population at all positions
def euler_method(u, t, p, q, L, h):
    return u + t*((p*u*(1-u/q))-(u/(1+u))+diffusion(u, L, h))

def run_solver(pop_matrix, tau_max, t, p, q, L, h):
    for tau in range(tau_max):
        pop_matrix[tau+1, :] = euler_method(pop_matrix[tau,:], t, p, q, L, h)

fig, (ax1, ax2) = plt.subplots(1, 2)
def plot_pop(tau, pop_matrix):
    ax2.plot(pop_matrix[tau,:],derivative(pop_matrix[tau,:],L,h))
    ax2.set(xlabel=r"u($\xi$, $\tau$)", ylabel=r"$\partial u/ \partial \xi$")

    ax1.plot(pop_matrix[tau,:])
    ax1.set(xlabel=r"$\xi$", ylabel=r"u($\xi$, $\tau$)")
    plt.draw()
    plt.pause(0.1)

def get_c(pop_matrix, tau, dtau, epsilon=0.25):
    pop = pop_matrix[tau,]
    half = max(pop)/2
    b = half-epsilon<pop
    a = half+epsilon>pop
    pos1 = np.where(a & b)[0][0]
    print(pop[a & b][0],"Xi: ", pos1)

    stick = pop[a & b]
    pop2 = pop_matrix[tau+dtau,]
    b = stick-epsilon<pop2
    a = stick+epsilon>pop2
    pos2 = np.where(a & b)[0][0]
    print(pop2[a & b][0],"Xi: ", pos2)
    print("c =",(pos2-pos1)/dtau/t)
    return((pos2-pos1)/dtau/t)

#%% i)  
fp = [5.56155, 1.43845, 0]
u0 = 3*fp[0] # ramp upper bound stable
x0 = 50 # ramp location
pop_matrix = np.zeros([tau_max+1, L]) # rows tau, cols position, value pop
#pop_matrix[0,:] = pop_init_ramp(u0, x0, L)
pop_matrix[0,:] = pop_init_smooth(u0, x0, L)
run_solver(pop_matrix, tau_max, t, p, q, L, h)
#get_c(pop_matrix, 400, 100, 0.25)

#plot_pop(1000, pop_matrix)
#plot_pop(2000, pop_matrix)
#%% plotter
for tau in range(tau_max):
    if tau % 50== 0:
        plot_pop(tau, pop_matrix)

input("Press Enter to continue...")