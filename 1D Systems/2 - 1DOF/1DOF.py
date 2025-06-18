import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# 1DoF model
def single_dof(x, t):
    friction = Mu * m * g * np.sign(x[1]) + c * x[1]
    return x[1], (F - B * x[1] - k * x[0] - friction) / m


# Parameters
FONT_SIZE = 14

m = 25  # Mass
B = 5   # Damping
k = 5   # Spring stiffness
F = 20  # Force

Mu = 0.004  # Dry friction
c = 0.2     # Viscous friction
g = 9.81    # Gravitational force

x0 = [0.0, 0.0]
t = np.arange(0.0, 70.0, 0.01)

# Simulation
out_x = odeint(single_dof, x0, t)
out_a = np.append(np.diff(out_x[:, 1]), 0)

# Plot
fig1 = plt.figure()
ax = fig1.add_subplot()
ax.plot(t, out_x[:, 0], label="x")
ax.plot(t, out_x[:, 1], label="x'")
ax.set_xlabel('t [s]', fontsize=FONT_SIZE)
ax.set_ylabel("x", fontsize=FONT_SIZE)
ax.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.legend(fontsize=FONT_SIZE)
plt.tight_layout()

fig2 = plt.figure()
ax = fig2.add_subplot()
ax.plot(t, out_a, label="x''")
ax.set_xlabel('t [s]', fontsize=FONT_SIZE)
ax.set_ylabel("x'", fontsize=FONT_SIZE)
ax.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.legend(fontsize=FONT_SIZE)
plt.tight_layout()

plt.show()
