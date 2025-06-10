import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    mu = 7

    init = [0.0, 0.1]
    time_vector = np.arange(0.0, 100.0, 0.01)

    font_size: int = 10
    title = f"Van der Pol\n$\\mu$={mu:.1f}"


def van_der_pol(y, __time__):
    return y[1], InputParams.mu * (1 - y[0] ** 2) * y[1] - y[0]


if __name__ == '__main__':

    ModelOutput = odeint(van_der_pol, InputParams.init, InputParams.time_vector)
    ModelAcc = np.append(np.diff(ModelOutput[:, 1]), 0)

    fig1 = plt.figure()
    ax = fig1.add_subplot()
    ax.plot(ModelOutput[:, 1], ModelOutput[:, 0])
    ax.set_xlabel('Y', fontsize=InputParams.font_size)
    ax.set_ylabel("Y'", fontsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("VanderPol_1.png", bbox_inches='tight', dpi=200)

    fig2 = plt.figure()
    ax = fig2.add_subplot()

    ax.plot(InputParams.time_vector, ModelOutput)
    ax.set_xlabel('t [s]', fontsize=InputParams.font_size)
    ax.set_ylabel('Y', fontsize=InputParams.font_size)
    ax.set_title("y = f(t)", fontsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("VanderPol_2.png", bbox_inches='tight', dpi=200)

    fig3 = plt.figure()
    ax = fig3.add_subplot(projection='3d')
    ax.plot(ModelOutput[:, 0], ModelOutput[:, 1], ModelAcc)
    ax.set_xlabel('$Y$', fontsize=InputParams.font_size)
    ax.set_ylabel("$Y'$", fontsize=InputParams.font_size)
    ax.set_zlabel("$Y''$", fontsize=InputParams.font_size)
    ax.xaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.yaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.zaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.set_title(InputParams.title)

    plt.tight_layout()
    plt.savefig("VanderPol_3.png", bbox_inches='tight', dpi=200)

    plt.show()
