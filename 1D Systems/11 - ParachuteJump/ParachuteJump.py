import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Parachute jump model
def parachutes(t, y):
    altitude = H - y[0]

    if altitude > h0:
        _c = c[0]
        _A = A[0]
    else:
        _c = c[1]
        _A = A[1]

    g_y = g0 - 3.086e-5 * altitude
    rho_y = rho0 * ((p0 - 13 * altitude) / p0)

    return y[1], g_y - (_c * _A * rho_y * y[1] ** 2) / (2 * m)


# Event: hit ground (altitude = 0)
def hit_ground(t, y):
    return H - y[0]


# Parameters
FONT_SIZE = 12

m = 110          # Mass of skydiver
c = [0.5, 1.42]  # Drag coefficient (before and after parachute)
A = [1.5, 28]    # Area (before and after parachute)
H = 5000         # Initial altitude [m]
h0 = 2000        # Parachute opening altitude [m]

g0 = 9.81
rho0 = 1.2
p0 = 1.01e5

hit_ground.terminal = True
hit_ground.direction = -1

y0 = [0.0, 0.0]
t_span = (0.0, 700.0)

# Simulation
sol = solve_ivp(parachutes, t_span, y0, method='RK45', events=hit_ground, max_step=0.1, dense_output=True)

# Calculations
t = sol.t
out = sol.y.T
acc = np.append(np.diff(out[:, 1]), 0)
out = np.column_stack((out, acc))

out[:, 0] = H - out[:, 0]          # Altitude
out[:, 1] = 3.6 * out[:, 1]        # Velocity [km/h]
out[:, 2] = (g0 - out[:, 2]) / g0  # Normalized G-force

# Plotting
ylabel = ["Altitude [m]", "Velocity [km/h]", "Normalized G-force"]
title = f"Parachute jump, skydiver m={m}kg"

fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(10, 8))
fig.suptitle(title, fontsize=FONT_SIZE)

for i in range(3):
    ax[i].plot(t, out[:, i], lw=2)
    ax[i].set_ylabel(ylabel[i], fontsize=FONT_SIZE)
    ax[i].grid(True)

ax[-1].set_xlabel("Time [s]", fontsize=FONT_SIZE)
plt.tight_layout()

plt.show()
