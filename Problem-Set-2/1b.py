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
tau_max = 10000


def pop_init(u0, x0, L):
    return u0/(1+np.exp(np.arange(L)+1-x0))

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
        ret[i] = (u[i+h]-u[i])/h
    return ret

# Returns next population at all positions
def euler_method(u, t, p, q, L, h):
    return u + t*((p*u*(1-u/q))-(u/(1+u))+diffusion(u, L, h))

def run_solver(pop_matrix, tau_max, t, p, q, L, h):
    for tau in range(tau_max):
        pop_matrix[tau+1, :] = euler_method(pop_matrix[tau,:], t, p, q, L, h)

def plot_pop(tau, pop_matrix):
    plt.plot(pop_matrix[tau,:])
    plt.xlabel(r"$\xi$")
    plt.ylabel(r"u($\xi$, "+str(tau)+")")
    plt.draw()
    plt.pause(0.1)

#%% i)  
u0 = 5.56155 # ramp upper bound stable
x0 = 20  # ramp location
pop_matrix = np.zeros([tau_max+1, L]) # rows tau, cols position, value pop
pop_matrix[0,:] = pop_init(u0, x0, L)
run_solver(pop_matrix, tau_max, t, p, q, L, h)
#plot_pop(1500, pop_matrix)
#plt.plot(pop_matrix[1500,:],derivative(pop_matrix[1500,:],L,h))
tau = 1000
epsilon = 0.25
pop = pop_matrix[tau,]
half = max(pop)/2
b = half-epsilon<pop
a = half+epsilon>pop
print(pop[a & b][0],"Xi: ",np.where(a & b)[0][0])

stick = pop[a & b]
pop2 = pop_matrix[tau+1000,]
b = stick-epsilon<pop2
a = stick+epsilon>pop2
print(pop2[a & b],"Xi: ",np.where(a & b)[0][0])
plot_pop(1000, pop_matrix)
plot_pop(2000, pop_matrix)
#%% ii)  
u0 = 1.43845 # ramp upper bound unstable
x0 = 50  # ramp location
pop_matrix = np.zeros([tau_max+1, L]) # rows tau, cols position, value pop
pop_matrix[0,:] = pop_init(u0, x0, L)
run_solver(pop_matrix, tau_max, t, p, q, L, h)
plot_pop(500, pop_matrix)
#%% iii)  
u0 = 0 # ramp upper bound stable
x0 = 50  # ramp location
pop_matrix = np.zeros([tau_max+1, L]) # rows tau, cols position, value pop
pop_matrix[0,:] = pop_init(u0, x0, L)
run_solver(pop_matrix, tau_max, t, p, q, L, h)
plot_pop(500, pop_matrix)
#%% plotter
for tau in range(tau_max):
    if tau % 50== 0:
        plot_pop(tau, pop_matrix)


#%%













# Explicit Euler Method
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])

plt.figure(figsize = (12, 8))
plt.plot(t, s, 'bo--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()