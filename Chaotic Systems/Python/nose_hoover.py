import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    init = [0.1, 0.1, 0.1]
    time_vector = np.arange(0.0, 70.0, 0.01)

    n = len(time_vector)

    font_size: int = 10
    title = "Nose-Hoover"


def nose_hoover(state, __time__):
    x, y, z = state
    return y, -x + y * z, 1 - y ** 2


if __name__ == '__main__':

    ModelOutput = odeint(nose_hoover, InputParams.init, InputParams.time_vector)

    fig1 = plt.figure()
    ax = fig1.add_subplot(projection='3d')
    ax.plot(ModelOutput[:, 0], ModelOutput[:, 1], ModelOutput[:, 2])
    ax.set_xlabel('$X$', fontsize=InputParams.font_size)
    ax.set_ylabel('$Y$', fontsize=InputParams.font_size)
    ax.set_zlabel('$Z$', fontsize=InputParams.font_size)
    ax.xaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.yaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.zaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("Nose_Hoover_1.png", bbox_inches='tight', dpi=200)

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
    plt.savefig("Nose_Hoover_2.png", bbox_inches='tight', dpi=200)

    plt.show()
