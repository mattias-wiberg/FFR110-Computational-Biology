import numpy as np
import matplotlib.pyplot as plt

def laplace(X, h=1):
    # For 2d cartesian coordinates:
    # delta f = d^2f/dx^2 + d^2f/dy^2
    # Discrete Laplace operator:
    # d^2f/dx^2 = (f(x-h) + f(x+h) - 2f(x))/h^2
    d2fdx2 = (np.roll(X, 1, axis=1) + np.roll(X, -1, axis=1) - 2*X)/h**2
    d2fdy2 = (np.roll(X, 1, axis=0) + np.roll(X, -1, axis=0) - 2*X)/h**2
    return d2fdx2 + d2fdy2

L = 128; a = 3; b = 8; Du = 1; u_star = a; v_star = b/a
Dv = [2.3, 3, 5, 9]; Dv = Dv[0]
pertubation = 0.1
tmax = 10000
dt = 0.01
u = np.random.uniform(u_star*(1-pertubation), u_star*(1+pertubation), size=(L,L))
v = np.random.uniform(v_star*(1-pertubation), v_star*(1+pertubation), size=(L,L))

plt.ion()
for t in np.arange(0,tmax,dt):
    u += dt*(a-(b+1)*u+u*u*v+Du*laplace(u))
    v += dt*(b*u-u*u*v+Dv*laplace(v))
    if t == 1000:
        plt.imshow(u, vmin=0, vmax=12, cmap="binary")
        plt.title("t="+str(t)+" Dv="+str(Dv))
        plt.colorbar()
        plt.show()
        input("Done")
    if int(t*100)%1000==0:
        progress = round((t/tmax)*100,2)
        print(f"Simulating: {progress} %")

plt.imshow(u, vmin=0, vmax=12, cmap="binary")
plt.title("t="+str(t)+" Dv="+str(Dv))
plt.colorbar()
plt.show()
input("Done")