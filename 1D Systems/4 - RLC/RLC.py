import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from random import random


# RLC model
def rlc(u, t, R):
    w = np.cos((2 * np.pi * (k / 2) * t * t)
               + (2 * np.pi * fmin * t))
    return u[1], (U*w - R * C * u[1] - u[0]) / (L * C)


# Parameters
R = [1.0, 2.2, 3.3, 4.7, 10, 48]
L = round((random() * 10), 1) * 1e-3
C = round((random() * 10), 1) * 1e-6
U = 3.3

FONT_SIZE = 12

t = np.arange(0.0, 10.0, 0.0001)

f0 = 1 / (2 * np.pi * np.sqrt(L * C))
fmin = 0.6 * f0
fmax = 1.4 * f0
k = (fmax - fmin) / max(t)

u0 = [0.0] * 2
out = [[0] * 2 for i in range(len(R))]

# Simulation
for i in range(len(R)):
    out[i] = odeint(rlc, u0, t, args=(R[i],))

# Plot
fig1 = plt.figure()
ax = fig1.add_subplot()
for i in range(len(R)):
    ax.plot(t, out[i][:, 0], lw=2, label='{}\u03A9'.format(R[i]))
ax.set_xlabel('f [Hz]', fontsize=FONT_SIZE)
ax.set_ylabel('U [V]', fontsize=FONT_SIZE)
ax.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax.yaxis.set_tick_params(labelsize=FONT_SIZE)
ax.set_xticks([0, 2, 4, 5, 6, 8, 10])
ax.set_xticklabels(np.linspace(fmin, fmax, 7, dtype=int))
plt.legend(fontsize=FONT_SIZE)
plt.show()
