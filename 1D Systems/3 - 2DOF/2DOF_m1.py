import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# 2DoF model
def dual_dof(x, t):
    f_t = F * np.sin(2 * np.pi * t)
    subsystem1 = (f_t - B[0]*x[1] - k[0]*x[0] + B[0]*x[3] + k[0]*x[2]) / m[0]
    subsystem2 = (0 - sum(B)*x[3] - sum(k)*x[2] + B[0]*x[1] + k[0]*x[0]) / m[1]
    return x[1], subsystem1, x[3], subsystem2


# Parameters
FONT_SIZE = 14

m = [5, 25]
B = [2, 8.4]
k = [2, 8.4]
F = 20

x0 = [0.0, 0.0, 0.0, 0.0]
t = np.arange(0.0, 50.0, 0.01)

# Simulation
out_x = odeint(dual_dof, x0, t)

# Plot
fig1 = plt.figure()
ax = fig1.add_subplot()
ax.plot(t, out_x[:, 0], label="m1 x")
ax.plot(t, out_x[:, 2], label="m2 x")
ax.set_xlabel('t [s]', fontsize=FONT_SIZE)
ax.set_ylabel("x", fontsize=FONT_SIZE)
ax.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.legend(fontsize=FONT_SIZE)
plt.tight_layout()

fig2 = plt.figure()
ax = fig2.add_subplot()
ax.plot(t, out_x[:, 1], label="m1 x'")
ax.plot(t, out_x[:, 3], label="m2 x'")
ax.set_xlabel('t [s]', fontsize=FONT_SIZE)
ax.set_ylabel("x'", fontsize=FONT_SIZE)
ax.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.legend(fontsize=FONT_SIZE)
plt.tight_layout()

plt.show()
