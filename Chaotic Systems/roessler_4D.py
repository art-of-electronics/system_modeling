import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    a = 0.25
    b = 2
    c = 0.5
    d = 0.05

    init = [-10, -6, 0, 10]
    time_vector = np.arange(0.0, 100.0, 0.01)

    font_size: int = 10
    title = f"Hyper chaotic Roessler\na={a:.2f}, b={b:.2f}, c={c:.2f}, d={d:.2f}"


def hyper_roessler(state, __time__):
    x, y, z, w = state
    return - y - z, x + (InputParams.a * y) + w, InputParams.b + (x * z), - (InputParams.c * z) + (InputParams.d * w)


if __name__ == '__main__':

    ModelOutput = odeint(hyper_roessler, InputParams.init, InputParams.time_vector)

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
    plt.savefig("Roessler4D_1.png", bbox_inches='tight', dpi=200)

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
    plt4.legend(['$X$', '$Y$', '$Z$', '$W$'], fontsize=InputParams.font_size)
    plt4.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt4.set_ylabel('$Y$', fontsize=InputParams.font_size)
    plt4.set_title("X, Y, Z, W = f(t)", fontsize=InputParams.font_size)

    plt.tight_layout()
    plt.savefig("Roessler4D_2.png", bbox_inches='tight', dpi=200)

    fig3 = plt.figure()
    fig3.suptitle(InputParams.title)

    plt1 = plt.subplot2grid((2, 2), (0, 0))
    plt1.plot(ModelOutput[:, 0], ModelOutput[:, 3], 'tab:green')
    plt1.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt1.set_ylabel('$W$', fontsize=InputParams.font_size)
    plt1.set_title("X-W Plot", fontsize=InputParams.font_size)

    plt2 = plt.subplot2grid((2, 2), (0, 1))
    plt2.plot(ModelOutput[:, 1], ModelOutput[:, 3], 'tab:orange')
    plt2.set_xlabel('$Y$', fontsize=InputParams.font_size)
    plt2.set_ylabel('$W$', fontsize=InputParams.font_size)
    plt2.set_title("Y-W Plot", fontsize=InputParams.font_size)

    plt3 = plt.subplot2grid((2, 2), (1, 0))
    plt3.plot(ModelOutput[:, 3], ModelOutput[:, 2], 'tab:red')
    plt3.set_xlabel('$W$', fontsize=InputParams.font_size)
    plt3.set_ylabel('$Z$', fontsize=InputParams.font_size)
    plt3.set_title("W-Z Plot", fontsize=InputParams.font_size)

    plt4 = plt.subplot2grid((2, 2), (1, 1))
    plt4.plot(InputParams.time_vector, ModelOutput[:, 3])
    plt4.set_xlabel('$t$', fontsize=InputParams.font_size)
    plt4.set_ylabel('$W$', fontsize=InputParams.font_size)
    plt4.set_title("W = f(t)", fontsize=InputParams.font_size)

    plt.tight_layout()
    plt.savefig("Roessler4D_3.png", bbox_inches='tight', dpi=200)

    plt.show()
