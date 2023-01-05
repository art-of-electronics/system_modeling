import numpy as np
#from matplotlib import cm
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

mu = 7

def vdp(y, t):
    return y[1], mu * (1 - y[0] ** 2) * y[1] - y[0]

init = [0.0, 0.1]
t = np.arange(0.0, 100.0, 0.01)

out = odeint(vdp, init, t)

fntsz = 10

fig1 = plt.figure()
ax = fig1.add_subplot()
ax.plot(out[:,1], out[:,0])
ax.set_xlabel('Y1', fontsize=fntsz)
ax.set_ylabel('Y2', fontsize=fntsz)
ax.set_title("Van der Pol\n$\\mu$=%.1f" % (mu))
plt.savefig("VanderPol_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
ax = fig2.add_subplot()
ax.plot(t, out)
ax.set_xlabel('t [s]', fontsize=fntsz)
ax.set_ylabel('Y', fontsize=fntsz)
ax.set_title("y = f(t)", fontsize=fntsz)
ax.set_title("Van der Pol\n$\\mu$=%.1f" % (mu))
plt.savefig("VanderPol_2.png", bbox_inches = 'tight', dpi = 200)

plt.show()