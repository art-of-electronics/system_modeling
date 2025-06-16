from scipy.signal import StateSpace, chirp, lsim
import matplotlib.pyplot as plt
import numpy as np
from random import random


# Parameters
R = 2.2 # [1, 2.2, 3.3]
L = round((random() * 10), 1) * 1e-3
C = round((random() * 10), 1) * 1e-6
U = 3.3

FONT_SIZE = 12

f0 = 1 / (2 * np.pi * np.sqrt(L * C))
fmin = 0.6*f0
fmax = 1.4*f0

# System
A = [[-R/L, -1/L], [1/C, 0]]
B = [[1/L], [0]]
C = [[0, 1]]
D = [[0]]

sys = StateSpace(A, B, C, D)

# Simulation
t = np.linspace(0, 10, 100000)
u = U * chirp(t, f0=fmin, f1=fmax, t1=10, method='linear')

t, out, x = lsim(sys, u, t)

# Plot
fig1 = plt.figure()
ax = fig1.add_subplot()
ax.plot(t, out, lw=2, label=f'{R}\u03A9')
ax.set_xlabel('f [Hz]', fontsize=FONT_SIZE)
ax.set_ylabel('U [V]', fontsize=FONT_SIZE)
ax.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax.yaxis.set_tick_params(labelsize=FONT_SIZE)
ax.set_xticks([0, 2, 4, 5, 6, 8, 10])
ax.set_xticklabels(np.linspace(fmin, fmax, 7, dtype=int))
plt.legend(fontsize=FONT_SIZE)
plt.show()