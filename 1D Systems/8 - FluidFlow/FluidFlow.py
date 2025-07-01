import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Fluid flow model
def fluid_flow(t, h):
    
    return [-(d / D) ** 2 * np.sqrt((2 * g * h[0]) / (1 + ksiVal))]

# Event: no water in tank (water level = 0)


def empty_tank(t, h):
    return np.real(h[0])


# Parameters
g = 9.81
# Tank diameters [m]
d = 0.03
D = 1
h0 = [5]
# Valve losses
ksi = [0.01, 0.5]

FONT_SIZE = 12

empty_tank.terminal = True
empty_tank.direction = -1

t_span = (0.0, 1000.0)

t = [[0] * 2 for i in range(len(ksi))]
out = [[0] * 2 for i in range(len(ksi))]

# Simulation
for i in range(len(ksi)):
    ksiVal = ksi[i]
    sol = solve_ivp(fluid_flow, t_span, h0, method='RK45', events=empty_tank, max_step=0.1, dense_output=True)
    t[i] = sol.t
    out[i] = sol.y.T

# Plot
fig1 = plt.figure()
ax = fig1.add_subplot()
for i in range(len(ksi)):
    ax.plot(t[i], out[i][:, 0], lw=2, label='loss={}'.format(ksi[i]))
ax.set_xlabel('Time [s]', fontsize=FONT_SIZE)
ax.set_ylabel('Water level [m]', fontsize=FONT_SIZE)
ax.set_title(f'h=f(t), for $h_{0}$={h0[0]}m', fontsize=FONT_SIZE)
ax.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.legend(fontsize=FONT_SIZE)
plt.show()
