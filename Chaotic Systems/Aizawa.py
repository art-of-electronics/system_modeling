import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

alpha = 0.95
beta = 0.7
gamma = 0.65
sigma = 3.5
epsilon = 0.15

def aizawa(state, t):
    x, y, z = state
    return x * (z - beta) - sigma * y, sigma * x + y * (z - beta), gamma + alpha * z - (z ** 3) / 3 - x ** 2 + epsilon * z * x ** 3

init = [-1, -1, -1]
t = np.arange(0.0, 200.0, 0.01)

out = odeint(aizawa, init, t)

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
ax.set_title("Aizawa\n$\\alpha$=%.2f, $\\beta$=%.2f, $\\gamma$=%.2f, $\\sigma$=%.2f, $\\epsilon$=%.2f" % (alpha, beta, gamma, sigma, epsilon))
plt.savefig("Aizawa_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
fig2.suptitle("Aizawa\n$\\alpha$=%.2f, $\\beta$=%.2f, $\\gamma$=%.2f, $\\sigma$=%.2f, $\\epsilon$=%.2f" % (alpha, beta, gamma, sigma, epsilon))

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
plt.savefig("Aizawa_2.png", bbox_inches = 'tight', dpi = 200)

plt.show()