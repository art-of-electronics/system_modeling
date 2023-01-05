import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

alpha = 30
beta = 50
gamma = 0.32
a = 0.03
c = -1.2
s = 0.75

def hyperchua(state, t):
    x, y, z, w = state
    return alpha * (y - a * (x ** 3) - x * (1 + c)), x - y + z, - beta * y - gamma * z + w, - s * x + y * z

init = [0, 0.1, 0.3, 0]
t = np.arange(0.0, 30.0, 0.01)

out = odeint(hyperchua, init, t)

fntsz = 10

fig1 = plt.figure()
ax = fig1.add_subplot(projection ='3d')
ax.plot(out[:, 0], out[:, 1], out[:, 2], 'tab:blue')
ax.plot(out[:,0], out[:,2], out[:,3], 'tab:red')
ax.set_xlabel('$X$', fontsize=fntsz)
ax.set_ylabel('$Y$', fontsize=fntsz)
ax.set_zlabel('$Z$', fontsize=fntsz)
ax.xaxis.set_tick_params(labelsize=fntsz)
ax.yaxis.set_tick_params(labelsize=fntsz)
ax.zaxis.set_tick_params(labelsize=fntsz)
ax.set_title("Hyperchaotic Chua\n$\\alpha$=%d, $\\beta$=%d, $a$=%.2f, $c$=%.2f, $s$=%.2f" % (alpha, beta, a, c, s))
plt.savefig("Chua4D_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
fig2.suptitle("Hyperchaotic Chua\n$\\alpha$=%d, $\\beta$=%d, $a$=%.2f, $c$=%.2f, $s$=%.2f" % (alpha, beta, a, c, s))

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
plt4.plot(t,out[:, 0], t,out[:, 1], t,out[:, 2], t,out[:, 3])
plt4.legend(['X','Y','Z','W'])
plt4.set_xlabel('$t$')
plt4.set_ylabel('$X,Y,Z$')
plt4.set_title("X,Y,Z,W = f(t)")

plt.tight_layout()
plt.savefig("Chua4D_2.png", bbox_inches = 'tight', dpi = 200)

fig3 = plt.figure()
fig3.suptitle("Hyperchaotic Chua\n$\\alpha$=%d, $\\beta$=%d, $a$=%.2f, $c$=%.2f, $s$=%.2f" % (alpha, beta, a, c, s))

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
plt4.plot(out[:, 3], out[:, 3])
#plt4.legend(['X','Y','Z','W'])
plt4.set_xlabel('$W$')
plt4.set_ylabel('$W$')
plt4.set_title("W-W Plot")


plt.tight_layout()
plt.savefig("Chua4D_3.png", bbox_inches = 'tight', dpi = 200)
plt.show()