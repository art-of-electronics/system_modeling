import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

_lambda = 1

def hhs(x, t):
    X = - x[0] - 2 * _lambda * x[0] * x[2]
    Y = - x[2] - _lambda * (x[0] ** 2 - x[2] ** 2)
    return x[1], X, x[3], Y

init = [-0.0824, 0.245, 0.508, -0.0408]
t = np.arange(0.0, 150.0, 0.01)

out = odeint(hhs, init, t)

fntsz = 10

fig1 = plt.figure()
ax = fig1.add_subplot(projection ='3d')
ax.plot(out[:,0], out[:,2], out[:,1], 'tab:olive')
ax.plot(out[:,0], out[:,2], out[:,3], 'tab:red')
ax.legend(['$P_{x}$','$P_{y}$'], fontsize=fntsz)
ax.set_xlabel('$X$', fontsize=fntsz)
ax.set_ylabel('$Y$', fontsize=fntsz)
ax.set_zlabel('$P_{x}, P_{y}$', fontsize=fntsz)
ax.xaxis.set_tick_params(labelsize=fntsz)
ax.yaxis.set_tick_params(labelsize=fntsz)
ax.zaxis.set_tick_params(labelsize=fntsz)
ax.set_title("Henon-Heiles\n$\\lambda$=%.1f, $x_{0}$=%.4f, $y_{0}$=%.4f, $Px$=%.4f, $Py$=%.4f" % (_lambda, *init))
plt.savefig("HenonHeiles_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
fig2.suptitle("Henon-Heiles\n$\\lambda$=%.1f, $x_{0}$=%.4f, $y_{0}$=%.4f, $Px$=%.4f, $Py$=%.4f" % (_lambda, *init))

plt1 = plt.subplot2grid((2,2), (0,0))
plt1.plot(out[:, 0], out[:, 1],'tab:green')
plt1.set_xlabel('$X$', fontsize=fntsz)
plt1.set_ylabel('$Y$', fontsize=fntsz)
plt1.set_title("$X-Y$ Plot")

plt2 = plt.subplot2grid((2,2), (0,1))
plt2.plot(out[:, 2], out[:, 3],'tab:orange')
plt2.set_xlabel('$P_{x}$', fontsize=fntsz)
plt2.set_ylabel('$P_{y}$', fontsize=fntsz)
plt2.set_title("$P_{x}-P_{y}$ Plot")

plt3 = plt.subplot2grid((2,2), (1,0))
plt3.plot(out[:, 0], out[:, 2],'tab:red')
plt3.set_xlabel('$X$', fontsize=fntsz)
plt3.set_ylabel('$P_{x}$', fontsize=fntsz)
plt3.set_title("$X-P_{x}$ Plot")

plt4 = plt.subplot2grid((2,2), (1,1))
plt4.plot(out[:, 1], out[:, 3],'tab:blue')
plt4.set_xlabel('$Y$', fontsize=fntsz)
plt4.set_ylabel('$P_{y}$', fontsize=fntsz)
plt4.set_title("$Y-P_{y}$ Plot")

plt.tight_layout()
plt.savefig("HenonHeiles_2.png", bbox_inches = 'tight', dpi = 200)

plt.show()