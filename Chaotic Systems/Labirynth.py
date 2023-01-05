import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

b = 0.19

def labirynth(state, t):
    x, y, z = state
    return np.sin(y) - b * x, np.sin(z) - b * y, np.sin(x) - b * z

init = [1.0, 0.8, 0.8]
t = np.arange(0.0, 500.0, 0.1)

out = odeint(labirynth, init, t)

fntsz = 10

fig1 = plt.figure()
ax = fig1.add_subplot(projection="3d")
N = len(t)
ax.plot(out[:, 0], out[:, 1], out[:, 2])
ax.set_xlabel('$X$', fontsize=fntsz)
ax.set_ylabel('$Y$', fontsize=fntsz)
ax.set_zlabel('$Z$', fontsize=fntsz)
ax.xaxis.set_tick_params(labelsize=fntsz)
ax.yaxis.set_tick_params(labelsize=fntsz)
ax.zaxis.set_tick_params(labelsize=fntsz)
ax.set_title("Labirynth\n$b$=%.3f" % (b))
plt.savefig("Labyrynth_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
ax = fig2.add_subplot(projection="3d")
N = len(t)

ax.scatter(out[:, 0], out[:, 1], out[:, 2], c = plt.cm.jet(np.linspace(0,1,len(t))))

ax.set_xlabel('$X$', fontsize=fntsz)
ax.set_ylabel('$Y$', fontsize=fntsz)
ax.set_zlabel('$Z$', fontsize=fntsz)
ax.xaxis.set_tick_params(labelsize=fntsz)
ax.yaxis.set_tick_params(labelsize=fntsz)
ax.zaxis.set_tick_params(labelsize=fntsz)
ax.set_title("Labirynth\n$b$=%.3f" % (b))
plt.savefig("Labyrynth_2.png", bbox_inches = 'tight', dpi = 200)

plt.show()