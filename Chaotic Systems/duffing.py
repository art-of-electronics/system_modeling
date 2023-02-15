import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    sigma = 0.3
    alpha = -1
    beta = 1
    gamma = 0.5
    omega = 1.21

    init = [0.0, 0.1]
    time_vector = np.arange(0.0, 100.0, 0.01)

    font_size: int = 10
    title = f"Duffing\n$\\sigma$={sigma:.2f}, $\\alpha$={alpha:.1f}, $\\beta$={beta:.1f}, " \
            f"$\\gamma$={gamma:.1f}, $\\omega$={omega:.1f}"


def duffing(x, time):
    return x[1], \
        InputParams.gamma * np.cos(InputParams.omega * time) - InputParams.sigma * x[1]\
        - InputParams.alpha * x[0] - InputParams.beta * x[0] ** 3


if __name__ == '__main__':

    ModelOutput = odeint(duffing, InputParams.init, InputParams.time_vector)
    ModelAcc = np.append(np.diff(ModelOutput[:, 1]), 0)

    fig1 = plt.figure()
    ax = fig1.add_subplot()
    ax.plot(ModelOutput[:, 0], ModelOutput[:, 1])
    ax.set_xlabel('X', fontsize=InputParams.font_size)
    ax.set_ylabel("X'", fontsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("Duffing_1.png", bbox_inches='tight', dpi=200)

    fig2 = plt.figure()
    ax = fig2.add_subplot()
    ax.plot(InputParams.time_vector, ModelOutput, InputParams.time_vector, ModelAcc)
    ax.set_xlabel('t [s]', fontsize=InputParams.font_size)
    ax.set_ylabel('X', fontsize=InputParams.font_size)
    ax.legend(['$x(t)$', "$x'(t)$", "$x''(t)$"], fontsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("Duffing_2.png", bbox_inches='tight', dpi=200)

    fig3 = plt.figure()
    ax = fig3.add_subplot(projection ='3d')
    ax.plot(ModelOutput[:, 0], ModelOutput[:, 1], ModelAcc)
    ax.set_xlabel('$X$', fontsize=InputParams.font_size)
    ax.set_ylabel("$X'$", fontsize=InputParams.font_size)
    ax.set_zlabel("$X''$", fontsize=InputParams.font_size)
    ax.xaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.yaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.zaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.set_title(InputParams.title)

    plt.tight_layout()
    plt.savefig("Duffing_3.png", bbox_inches='tight', dpi=200)

    plt.show()
