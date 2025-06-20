import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Pendulum model
def pendulum(phi, t, B):
    return phi[1], -B * phi[1] - g / l * np.sin(phi[0])


# Parameters
FONT_SIZE = 12

l = 0.247
g = 9.81
deg = 10
damping = [0.05, 0.1, 0.3]

rad = deg * np.pi / 180
w0 = np.sqrt(g / l)
B = [0, 2 * w0 * damping[0], 2 * w0 * damping[1], 2 * w0 * damping[2]]

t = np.arange(0.0, 10.0, 0.01)

phi0 = [rad, 0.0]
out = [[0] * 2 for i in range(len(B))]

# Simulation
for i in range(len(B)):
    out[i] = odeint(pendulum, phi0, t, args=(B[i],))

# Calculations
out_deg = [np.column_stack((arr[:, 0] * (180 / np.pi), arr[:, 1])) for arr in out]
legend = [f'Damping B={i:.2f}' for i in B]
legend[0] = 'No Damping'

# Plot
fig1 = plt.figure()
ax = fig1.add_subplot()
for i in range(len(B)):
    ax.plot(t, out_deg[i][:, 0], lw=2, label=legend[i])
ax.set_xlabel('Time [s]', fontsize=FONT_SIZE)
ax.set_ylabel('Pendulum swing [\u00B0]', fontsize=FONT_SIZE)
ax.set_title(f'Motion of a pendulum of length l={l:.3f}[m]')
plt.legend(fontsize=FONT_SIZE)
plt.tight_layout()

plt.figure(2)
for i in range(len(B)):
    plt.subplot(2, 2, i + 1)
    plt.plot(out[i][:, 0], out[i][:, 1], lw=2)
    plt.xlabel(r'$\varphi$', fontsize=FONT_SIZE)
    plt.ylabel(r'$\frac{d\varphi}{dt}$', fontsize=FONT_SIZE)
    plt.title(f'Phase portrait - {legend[i]}', fontsize=FONT_SIZE)
plt.tight_layout()

plt.show()
