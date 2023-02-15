# model and parameters from https://www.chuacircuits.com/matlabsim.php

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    coupling = dict(C1=10*1e-9, C2=100*1e-9, R=1800)
    coupling['G'] = 1 / coupling['R']

    gyrator = dict(R7=100, R8=1000, R9=1000, R10=1800, C=100*1e-9)
    gyrator['L'] = gyrator['R7'] * gyrator['R9'] * gyrator['R10'] * gyrator['C'] / gyrator['R8']  # mH

    diode = dict(R1=220, R2=220, R3=2200, R4=22000, R5=22000, R6=3300)

    voltage = dict(U=18)
    voltage['E1'] = diode['R3'] / (diode['R2'] + diode['R3']) * voltage['U']
    voltage['E2'] = diode['R6'] / (diode['R5'] + diode['R6']) * voltage['U']

    m = [
        ['nan', 1 / diode['R1'], 1 / diode['R4']],
        ['nan', -1 / diode['R3'], -1 / diode['R6']]
    ]
    m1 = m[1][2] + m[1][1]
    mm1 = m[0][1] + m[0][2]

    init = [-0.5, -0.2, 0.004]
    time_vector = np.arange(0.0, 0.01, 0.000001)
    
    font_size: int = 10
    title = f"Chua\n$C_{1}$={coupling['C1']*1e9:.1f}nF, $C_{2}$={coupling['C2']*1e9:.1f}nF, " \
            f"$R$={coupling['R']/1e3:.1f}$k\\Omega$, $L$={gyrator['L']*1e3:.1f}mH"


def chua(states, __time__):
    x, y, z = states

    if InputParams.voltage['E1'] > InputParams.voltage['E2']:
        m0 = InputParams.m[1][1] + InputParams.m[0][2]
    else:
        m0 = InputParams.m[1][2] + InputParams.m[0][1]

    e_max = max([InputParams.voltage['E1'], InputParams.voltage['E2']])
    e_min = min([InputParams.voltage['E1'], InputParams.voltage['E2']])

    g = 0
    if abs(x) < e_min:
        g = x * InputParams.m1
    elif abs(x) < e_max:
        g = x * m0
        if x > 0:
            g = g + e_min * (InputParams.m1 - m0)
        else:
            g = g + e_min * (m0 - InputParams.m1)
    elif abs(x) >= e_max:
        g = x * InputParams.mm1
        if x > 0:
            g = g + e_max * (m0 - InputParams.mm1) + e_min * (InputParams.m1 - m0)
        else:
            g = g + e_max * (InputParams.mm1 - m0) + e_min * (m0 - InputParams.m1)

    return (1 / InputParams.coupling['C1']) * (InputParams.coupling['G'] * (y - x) - g), \
        (1 / InputParams.coupling['C2']) * (InputParams.coupling['G'] * (x - y) + z), \
        - (1 / InputParams.gyrator['L']) * y


if __name__ == '__main__':

    ModelOutput = odeint(chua, InputParams.init, InputParams.time_vector)

    fig1 = plt.figure()
    ax = fig1.add_subplot(projection='3d')
    ax.plot(ModelOutput[:, 0], ModelOutput[:, 1], ModelOutput[:, 2])  # , label='Chua')
    ax.set_xlabel('$X$', fontsize=InputParams.font_size)
    ax.set_ylabel('$Y$', fontsize=InputParams.font_size)
    ax.set_zlabel('$Z$', fontsize=InputParams.font_size)
    ax.xaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.yaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.zaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.zaxis.set_rotate_label(False)
    ax.set_title(InputParams.title)
    plt.savefig("ChuaR_1.png", bbox_inches='tight', dpi=200)

    fig2 = plt.figure()
    fig2.suptitle(InputParams.title)

    plt1 = plt.subplot2grid((2, 2), (0, 0))
    plt1.plot(ModelOutput[:, 0], ModelOutput[:, 1], 'tab:green')
    plt1.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt1.set_ylabel('$Y$', fontsize=InputParams.font_size)
    plt1.set_title("X-Y Plot", fontsize=InputParams.font_size)

    plt2 = plt.subplot2grid((2, 2), (0, 1))
    plt2.plot(ModelOutput[:, 1], ModelOutput[:, 2], 'tab:orange')
    plt2.set_xlabel('$Y$', fontsize=InputParams.font_size)
    plt2.set_ylabel('$Z$', fontsize=InputParams.font_size)
    plt2.set_title("Y-Z Plot", fontsize=InputParams.font_size)

    plt3 = plt.subplot2grid((2, 2), (1, 0))
    plt3.plot(ModelOutput[:, 0], ModelOutput[:, 2], 'tab:red')
    plt3.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt3.set_ylabel('$Z$', fontsize=InputParams.font_size)
    plt3.set_title("X-Z Plot", fontsize=InputParams.font_size)

    plt4 = plt.subplot2grid((2, 2), (1, 1))
    plt4.plot(InputParams.time_vector, ModelOutput[:, 0],
              InputParams.time_vector, ModelOutput[:, 1],
              InputParams.time_vector, ModelOutput[:, 2])
    plt4.legend(['X', 'Y', 'Z'], fontsize=InputParams.font_size)
    plt4.set_xlabel('$t$', fontsize=InputParams.font_size)
    plt4.set_ylabel('$X,Y,Z$', fontsize=InputParams.font_size)
    plt4.set_title("X,Y,Z = f(t)", fontsize=InputParams.font_size)

    plt.tight_layout()
    plt.savefig("ChuaR_2.png", bbox_inches='tight', dpi=200)

    plt.show()
