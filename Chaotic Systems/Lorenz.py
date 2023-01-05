import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

sigma = 10.0
rho = 26
beta = 8/3 

def lorenz(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

init = [1.0, 1.0, 1.0]
t = np.arange(0.0, 40.0, 0.01)

out = odeint(lorenz, init, t)

fntsz = 10

fig1 = plt.figure()
ax = fig1.add_subplot(projection ='3d')
ax.plot(out[:, 0], out[:, 1], out[:, 2])
ax.set_xlabel('$X$', fontsize=fntsz)
ax.set_ylabel('$Y$', fontsize=fntsz)
ax.set_zlabel('$Z$', fontsize=fntsz)
ax.xaxis.set_tick_params(labelsize=fntsz)
ax.yaxis.set_tick_params(labelsize=fntsz)
ax.zaxis.set_tick_params(labelsize=fntsz)
ax.set_title("Lorenz\n$\sigma$=%i, $\\rho=%i$, $\\beta=%.2f$" % (sigma, rho, beta))
plt.savefig("Lorenz_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
fig2.suptitle("Lorenz\n$\sigma$=%i, $\\rho=%i$, $\\beta=%.2f$" % (sigma, rho, beta))

plt1 = plt.subplot2grid((2,2), (0,0))
plt1.plot(out[:, 0], out[:, 1],'tab:green')
plt1.set_xlabel('$X$', fontsize=fntsz)
plt1.set_ylabel('$Y$', fontsize=fntsz)
plt1.set_title("X-Y Plot")

plt2 = plt.subplot2grid((2,2), (0,1))
plt2.plot(out[:, 1], out[:, 2],'tab:orange')
plt2.set_xlabel('$Y$', fontsize=fntsz)
plt2.set_ylabel('$Z$', fontsize=fntsz)
plt2.set_title("Y-Z Plot")

plt3 = plt.subplot2grid((2,2), (1,0))
plt3.plot(out[:, 0], out[:, 2],'tab:red')
plt3.set_xlabel('$X$', fontsize=fntsz)
plt3.set_ylabel('$Z$', fontsize=fntsz)
plt3.set_title("X-Z Plot")

plt4 = plt.subplot2grid((2,2), (1,1))
plt4.plot(t,out[:, 0], t,out[:, 1], t,out[:, 2])
plt4.legend(['X','Y','Z'])
plt4.set_xlabel('$t$')
plt4.set_ylabel('$X,Y,Z$')
plt4.set_title("X,Y,Z = f(t)")
plt.tight_layout()
plt.savefig("Lorenz_2.png", bbox_inches = 'tight', dpi = 200)

plt.show()