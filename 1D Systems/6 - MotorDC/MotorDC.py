import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# DC motor model
def motor_dc(u, t, mt_in):
    u_in = U if t > 1 else 0
    mt_val = mt_in if t > 2 else 0
    
    return u[1], (-B * u[1] + km * u[3] - mt_val) / J, \
           u[3], (u_in - R * u[3] - ke * u[1]) / L


# Parameters
# Voltage
U = 400  # Input voltage [V]

# Electrical parameters
R = 0.7           # Winding Resistance [Ohm]
L = 0.05          # Winding inductance [H]
Mt = [0, 35, 50]  # Loading torque [Nm]

# Mechanical parameters
r1 = 0.1    # Rotor inner diameter [m]
r2 = 0.15   # Rotor outer diameter [m]
h = 0.1     # Rotor length [m]
rho = 8700  # Rotor material density [kg/m3]

B = 0.01  # Shaft bearings friction
J = (np.pi * rho * (r2 ** 4 - r1 ** 4) * h) / 2  # Rotor inertia

# Motor constants
kv = 130  # Kv rating
ke = (kv / 1000) * (60 / (2 * np.pi))  # Electrical constant [Vs/rad]
km = ke                                # Mechanical constant [Nm/A]

FONT_SIZE = 12

t = np.arange(0.0, 13.0, 0.001)
u0 = [0.0] * 4
out = [[0] * 4 for i in range(len(Mt))]

# Simulation
for i in range(len(Mt)):
    out[i] = odeint(motor_dc, u0, t, args=(Mt[i],))

# Calculate 2nd derivative
out_phi2 = []
out_q2 = []
for i in range(len(Mt)):
    out_phi2.append(np.append(np.diff(out[i][:, 1]), 0))
    out_q2.append(np.append(np.diff(out[i][:, 3]), 0))

# Plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(2, 1, 1)
for i in range(len(Mt)):
    ax1.plot(t, np.array(out[i][:, 1]) * 60 / (2 * np.pi), lw=2, label=f'$\\varphi$ at Mt={Mt[i]:.1f}Nm')
ax1.set_xlabel('Time [s]', fontsize=FONT_SIZE)
ax1.set_ylabel('Shaft RPM [$min^{-1}$]', fontsize=FONT_SIZE)
ax1.set_title(f'$\\varphi=f(M_t)$ for DC motor: R={R:.1f}$\\Omega$, L={L * 1000:.1f}mH')
ax1.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax1.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.grid()
ax2 = fig1.add_subplot(2, 1, 2)
for i in range(len(Mt)):
    ax2.plot(t, out[i][:, 3], lw=2, label=f'I at Mt={Mt[i]:.1f}Nm')
ax2.set_xlabel('Time [s]', fontsize=FONT_SIZE)
ax2.set_ylabel('Winding current [A]', fontsize=FONT_SIZE)
ax2.set_title(f'$I=f(M_t)$ for DC motor: R={R:.1f}$\\Omega$, L={L * 1000:.1f}mH')
ax2.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax2.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.grid()
plt.tight_layout()
plt.legend(fontsize=FONT_SIZE)
plt.show()

fig2 = plt.figure()
ax1 = fig2.add_subplot(2, 2, 1)
ax1.plot(out[0][:, 1], out_phi2[0], lw=2)
ax1.set_xlabel('$\\frac{d\\varphi}{dt}$', fontsize=FONT_SIZE)
ax1.set_ylabel('$\\frac{d^2\\varphi}{dt^2}$', fontsize=FONT_SIZE)
ax1.set_title('Mechanical - no load')
ax1.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax1.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.grid()

ax2 = fig2.add_subplot(2, 2, 2)
ax2.plot(out[0][:, 3], out_q2[0], lw=2)
ax2.set_xlabel('$I$', fontsize=FONT_SIZE)
ax2.set_ylabel('$\\frac{dI}{dt}$', fontsize=FONT_SIZE)
ax2.set_title('Electrical - no load')
ax2.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax2.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.grid()

ax3 = fig2.add_subplot(2, 2, 3)
ax3.plot(out[-1][:, 1], out_phi2[-1], lw=2)
ax3.set_xlabel('$\\frac{d\\varphi}{dt}$', fontsize=FONT_SIZE)
ax3.set_ylabel('$\\frac{d^2\\varphi}{dt^2}$', fontsize=FONT_SIZE)
ax3.set_title('Mechanical - under load')
ax3.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax3.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.grid()

ax4 = fig2.add_subplot(2, 2, 4)
ax4.plot(out[-1][:, 3], out_q2[-1], lw=2)
ax4.set_xlabel('$I$', fontsize=FONT_SIZE)
ax4.set_ylabel('$\\frac{dI}{dt}$', fontsize=FONT_SIZE)
ax4.set_title('Electrical - under load')
ax4.xaxis.set_tick_params(labelsize=FONT_SIZE)
ax4.yaxis.set_tick_params(labelsize=FONT_SIZE)
plt.grid()

plt.tight_layout()
plt.show()
