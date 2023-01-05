import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

a = 0.25
b = 2
c = 0.5
d = 0.05

def hyperroessler(state, t):
    x, y, z, w = state
    return - y - z, x + (a * y) + w, b + (x * z), - (c * z) + (d * w)

state0 = [-10, -6, 0, 10]
t = np.arange(0.0, 100.0, 0.01)

out = odeint(hyperroessler, state0, t)

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
ax.set_title("Hyperhaotic Roessler\na=%.2f, b=%.2f, c=%.2f, d=%.2f" % (a, b, c, d))
plt.savefig("Roessler4D_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
fig2.suptitle("Hyperhaotic Roessler\na=%.2f, b=%.2f, c=%.2f, d=%.2f" % (a, b, c, d))
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
plt4.plot(t,out)
plt4.legend(['$X$','$Y$', '$Z$', '$W$'])
plt4.set_xlabel('$X$')
plt4.set_ylabel('$Y$')
plt4.set_title("X, Y, Z, W = f(t)")

plt.tight_layout()
plt.savefig("Roessler4D_2.png", bbox_inches = 'tight', dpi = 200)

plt.show()