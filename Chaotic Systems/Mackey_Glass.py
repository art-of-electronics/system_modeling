import numpy as np
import matplotlib.pyplot as plt
from pylab import array
from ddeint import ddeint
from scipy.ndimage import shift
from mpl_toolkits.mplot3d import Axes3D

gamma = 1
beta = 2
tau = 5
n = 10

k = 100.0

def mackey_glass(x, t, d):
    X = x(t)
    Xt = x(t - d)
    return beta * Xt / (1 + Xt ** n) - X * gamma

g = lambda t: array([0.2, 0.2])
t = np.arange(0.0, 50, 1/k)

out = ddeint(mackey_glass, g, t, fargs=(tau,))
z = k*tau
out[:,1] = shift(out[:,1], z, cval=0.2)

fig1 = plt.figure()
ax = fig1.add_subplot()
ax.plot(out[:,1], out[:,0])
ax.set_xlabel('$x(t)$')
ax.set_ylabel('$x(t-\\tau)$')
ax.set_title("Mackey-Glass\n$\\gamma$=%.2f, $\\beta$=%.1f, $\\tau$=%.1f, $n$=%.1f" % (gamma, beta, tau, n))
plt.savefig("MackeyGlass_1.png", bbox_inches = 'tight', dpi = 200)

fig2 = plt.figure()
ax = fig2.add_subplot()
ax.plot(t, out)
ax.set_xlabel('t [s]')
ax.set_ylabel('Y')
ax.legend(['$x(t)$', '$x(t-\\tau)$'])
ax.set_title("Mackey-Glass\n$\\gamma$=%.2f, $\\beta$=%.1f, $\\tau$=%.1f, $n$=%.1f" % (gamma, beta, tau, n))
plt.savefig("MackeyGlass_2.png", bbox_inches = 'tight', dpi = 200)

plt.show()