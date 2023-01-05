#model and parameters from https://www.chuacircuits.com/matlabsim.php

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

a = 15.6
b = 28

m0 = -1.143
m1 = -0.714

def chua(state, t):
    x, y, z = state
    diode = (m1 * x) + ((m0 - m1) * (abs(x + 1) - abs(x - 1)) / 2)
    return a * (y - x - diode), x - y + z, - y * b

init = [0.7, 0, 0]
t = np.arange(0.0, 30.0, 0.01)

out = odeint(chua, init, t)

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
ax.set_title("Chua\n$a$=%.1f, $b$=%.1f, $m_{0}$=%.3f, $m_{1}$=%.3f" % (a, b, m0, m1))
plt.savefig("Chua_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
fig2.suptitle("Chua\n$a$=%.1f, $b$=%.1f, $m_{0}$=%.3f, $m_{1}$=%.3f" % (a, b, m0, m1))

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
plt.savefig("Chua_2.png", bbox_inches = 'tight', dpi = 200)
plt.show()