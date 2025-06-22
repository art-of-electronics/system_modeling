import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    q = 8*1e-4
    e = 0.3
    f = 1.05
    d = 4*1e-3

    init = [0.05, 0.05, 0.05]
    time_vector = np.arange(0.0, 50.0, 0.01)

    font_size: int = 10
    title = f"Belousov-Zhabotinsky\nq={q:.4f}, f={f:.2f}, $\\epsilon$={e:.2f}, $\\delta$={d:.4f}"


def belousov_zhabotinsky(state, __time__):
    x, y, z = state
    return (x + InputParams.q * y - x ** 2 - x * y) / InputParams.e, \
        (-InputParams.q * y + InputParams.f * z - x * y) / InputParams.d, \
        x - z


if __name__ == '__main__':

    ModelOutput = odeint(belousov_zhabotinsky, InputParams.init, InputParams.time_vector)

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
    plt.savefig("BelousovZhabotinsky_1.png", bbox_inches='tight', dpi=200)

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
    plt4.plot(InputParams.time_vector, ModelOutput)
    plt4.legend(['$X$', '$Y$', '$Z$'], fontsize=InputParams.font_size)
    plt4.set_xlabel('$X, Y, Z$', fontsize=InputParams.font_size)
    plt4.set_ylabel('$t (s)$', fontsize=InputParams.font_size)
    plt4.set_title("X,Y,Z = f(t)", fontsize=InputParams.font_size)

    plt.tight_layout()
    plt.savefig("BelousovZhabotinsky_2.png", bbox_inches='tight', dpi=200)

    plt.show()
