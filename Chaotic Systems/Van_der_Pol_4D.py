import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

mu = 5

def hypervdp(y, t):
    R1 = mu * (y[2] - (y[2] * y[2] * y[2]) / 3 - y[0])
    R2 = y[2] / mu
    return y[3], R1, y[1], R2

init = [0.0, 0.1, 0.0, 0.1]
t = np.arange(0.0, 100.0, 0.01)

out = odeint(hypervdp, init, t)

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
ax.set_title("Hyperchaotic Van der Pol\n$\\mu$=%.1f" % (mu))
plt.savefig("VanderPol4D_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
fig2.suptitle("Hyperchaotic Van der Pol\n$\\mu$=%.1f" % (mu))

plt1 = plt.subplot2grid((2,2), (0,0))
plt1.plot(out[:, 2], out[:, 0],'tab:green')
plt1.set_xlabel('$X$', fontsize=fntsz)
plt1.set_ylabel('$Y$', fontsize=fntsz)
plt1.set_title("$X-Y$ Plot")

plt2 = plt.subplot2grid((2,2), (0,1))
plt2.plot(out[:, 3], out[:, 1],'tab:orange')
plt2.set_xlabel("$X'$", fontsize=fntsz)
plt2.set_ylabel("$Y'$", fontsize=fntsz)
plt2.set_title("$X'-Y'$ Plot")

plt3 = plt.subplot2grid((2,2), (1,0))
plt3.plot(out[:, 2], out[:, 3],'tab:red')
plt3.set_xlabel('$X$', fontsize=fntsz)
plt3.set_ylabel("$X'$", fontsize=fntsz)
plt3.set_title("$X-X'$ Plot")

plt4 = plt.subplot2grid((2,2), (1,1))
plt4.plot(out[:, 0], out[:, 1],'tab:blue')
plt4.set_xlabel('$Y$', fontsize=fntsz)
plt4.set_ylabel("$Y'$", fontsize=fntsz)
plt4.set_title("$Y-Y'$ Plot")

plt.tight_layout()
plt.savefig("VanderPol4D_2.png", bbox_inches = 'tight', dpi = 200)

fig3 = plt.figure()
fig3.suptitle("Hyperchaotic Van der Pol\n$\\mu$=%.1f" % (mu))

plt1 = plt.subplot2grid((2,2), (0,0))
plt1.plot(out[:, 0], out[:, 3],'tab:green')
plt1.set_xlabel('$X$', fontsize=fntsz)
plt1.set_ylabel('$W$', fontsize=fntsz)
plt1.set_title("X-W Plot")

plt2 = plt.subplot2grid((2,2), (0,1))
plt2.plot(out[:, 1], out[:, 3],'tab:orange')
plt2.set_xlabel('$Y$', fontsize=fntsz)
plt2.set_ylabel('$W$', fontsize=fntsz)
plt2.set_title("Y-W Plot")

plt3 = plt.subplot2grid((2,2), (1,0))
plt3.plot(out[:, 3], out[:, 2],'tab:red')
plt3.set_xlabel('$W$', fontsize=fntsz)
plt3.set_ylabel('$Z$', fontsize=fntsz)
plt3.set_title("W-Z Plot")

plt4 = plt.subplot2grid((2,2), (1,1))
plt4.plot(t, out[:, 3])
plt4.set_xlabel('$t$')
plt4.set_ylabel('$W$')
plt4.set_title("W = f(t)")

plt.tight_layout()
plt.savefig("VanderPol4D_3.png", bbox_inches = 'tight', dpi = 200)

plt.show()