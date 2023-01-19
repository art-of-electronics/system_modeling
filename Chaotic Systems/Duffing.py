import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

sigma = 0.3
alpha = -1
beta = 1
gamma = 0.5
omega = 1.21

def duffing(x, t):
    return x[1], gamma * np.cos(omega * t) - sigma * x[1] - alpha * x[0] - beta * x[0] ** 3

init = [0.0, 0.1]
t = np.arange(0.0, 100.0, 0.01)

out = odeint(duffing, init, t)
outx2 = np.append(np.diff(out[:,1]),0)

fntsz = 10

fig1 = plt.figure()
ax = fig1.add_subplot()
ax.plot(out[:,0], out[:,1])
ax.set_xlabel('X')
ax.set_ylabel("X'")
ax.set_title("Duffing\n$\\sigma$=%.2f, $\\alpha$=%.1f, $\\beta$=%.1f, $\\gamma$=%.1f, $\\omega$=%.1f" % (sigma, alpha, beta, gamma, omega))
plt.savefig("Duffing_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
ax = fig2.add_subplot()
ax.plot(t,out, t,outx2)
ax.set_xlabel('t [s]')
ax.set_ylabel('X')
ax.legend(['$x(t)$', "$x'(t)$", "$x''(t)$"])
ax.set_title("Duffing\n$\\sigma$=%.2f, $\\alpha$=%.1f, $\\beta$=%.1f, $\\gamma$=%.1f, $\\omega$=%.1f" % (sigma, alpha, beta, gamma, omega))
plt.savefig("Duffing_2.png", bbox_inches = 'tight', dpi = 200)

fig3 = plt.figure()
ax = fig3.add_subplot(projection ='3d')
ax.plot(out[:, 0], out[:, 1], outx2)
ax.set_xlabel('$X$', fontsize=fntsz)
ax.set_ylabel("$X'$", fontsize=fntsz)
ax.set_zlabel("$X''$", fontsize=fntsz)
ax.xaxis.set_tick_params(labelsize=fntsz)
ax.yaxis.set_tick_params(labelsize=fntsz)
ax.zaxis.set_tick_params(labelsize=fntsz)
ax.set_title("Duffing\n$\\sigma$=%.2f, $\\alpha$=%.1f, $\\beta$=%.1f, $\\gamma$=%.1f, $\\omega$=%.1f" % (sigma, alpha, beta, gamma, omega))
plt.tight_layout()
plt.savefig("Duffing_3.png", bbox_inches = 'tight', dpi = 200)

plt.show()