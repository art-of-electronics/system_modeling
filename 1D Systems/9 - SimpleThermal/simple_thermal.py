import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Simple thermal model
def thermal(T, t):
    if t > t_start:
        step = Qin
    else:
        step = 0
 
    return (step - (T - Tw) * Kc) / Cv


# Parameters
FONT_SIZE = 14

Q = 4000  # Heater power [W]
#  Temperatures [deg C]
T0 = -10
Tfinal = 20
#  Room dimensionsimensions [m]
x = 5
y = 5
z = 3
# Air thermodynamic parameters
Cp = 1005  # Specific heat [J/kgK]
rho = 1.2  # Density [kg/m3]

V = np.prod([x, y, z])
Cv = Cp * rho * V

qN = [0.6*Q, 1.0 * Q, 1.4*Q, 2.0*Q]
Tw = T0

t_start = 600;
t = np.arange(0, 3600, 1)

out_T = [[0] for i in range(len(qN))]

# Simulation
for i in range(len(qN)):
    Qin = qN[i]
    Kc = qN[i] / (Tfinal - T0)
    out_T[i] = odeint(thermal, T0, t)

# Plot
fig1 = plt.figure()
ax = fig1.add_subplot()
for i in range(len(qN)):
    ax.plot(t / 60, out_T[i], lw=2, label=f'q{i}={(qN[i] / 1000):.1f}kW')
ax.set_title(f'$T_W=f(q)$, for $t_0$={T0:.1f}\u00B0C', fontsize=FONT_SIZE)
ax.set_xlabel('Time [min]', fontsize=FONT_SIZE)
ax.set_ylabel('Temperature [\u00B0C]', fontsize=FONT_SIZE)
ax.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.legend(fontsize=FONT_SIZE)
plt.grid()
plt.show()
