import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    alpha = 30
    beta = 50
    gamma = 0.32
    a = 0.03
    c = -1.2
    s = 0.75

    init = [0, 0.1, 0.3, 0]
    time_vector = np.arange(0.0, 30.0, 0.01)

    font_size: int = 10
    title = f"Hyper chaotic Chua\n$\\alpha$={alpha:d}, $\\beta$={beta:d}, $\\gamma$={gamma:.2f}, " \
            f"$a$={a:.2f}, $c$={c:.2f}, $s$={s:.2f}"


def hyper_chua(state, __time__):
    x, y, z, w = state
    return InputParams.alpha * (y - InputParams.a * (x ** 3) - x * (1 + InputParams.c)), \
        x - y + z, \
        - InputParams.beta * y - InputParams.gamma * z + w, - InputParams.s * x + y * z


if __name__ == '__main__':

    ModelOut = odeint(hyper_chua, InputParams.init, InputParams.time_vector)

    fig1 = plt.figure()
    ax = fig1.add_subplot(projection='3d')
    ax.plot(ModelOut[:, 0], ModelOut[:, 1], ModelOut[:, 2], 'tab:blue')
    ax.plot(ModelOut[:, 0], ModelOut[:, 2], ModelOut[:, 3], 'tab:red')
    ax.set_xlabel('$X$', fontsize=InputParams.font_size)
    ax.set_ylabel('$Y$', fontsize=InputParams.font_size)
    ax.set_zlabel('$Z$', fontsize=InputParams.font_size)
    ax.xaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.yaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.zaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("Chua4D_1.png", bbox_inches='tight', dpi=200)

    fig2 = plt.figure()
    fig2.suptitle(InputParams.title)

    plt1 = plt.subplot2grid((2, 2), (0, 0))
    plt1.plot(ModelOut[:, 0], ModelOut[:, 1], 'tab:green')
    plt1.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt1.set_ylabel('$Y$', fontsize=InputParams.font_size)
    plt1.set_title("X-Y Plot", fontsize=InputParams.font_size)

    plt2 = plt.subplot2grid((2, 2), (0, 1))
    plt2.plot(ModelOut[:, 1], ModelOut[:, 2], 'tab:orange')
    plt2.set_xlabel('$Y$', fontsize=InputParams.font_size)
    plt2.set_ylabel('$Z$', fontsize=InputParams.font_size)
    plt2.set_title("Y-Z Plot", fontsize=InputParams.font_size)

    plt3 = plt.subplot2grid((2, 2), (1, 0))
    plt3.plot(ModelOut[:, 0], ModelOut[:, 2], 'tab:red')
    plt3.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt3.set_ylabel('$Z$', fontsize=InputParams.font_size)
    plt3.set_title("X-Z Plot", fontsize=InputParams.font_size)

    plt4 = plt.subplot2grid((2, 2), (1, 1))
    plt4.plot(InputParams.time_vector, ModelOut[:, 0],
              InputParams.time_vector, ModelOut[:, 1],
              InputParams.time_vector, ModelOut[:, 2],
              InputParams.time_vector, ModelOut[:, 3])
    plt4.legend(['X', 'Y', 'Z', 'W'], fontsize=InputParams.font_size)
    plt4.set_xlabel('$t$', fontsize=InputParams.font_size)
    plt4.set_ylabel('$X,Y,Z$', fontsize=InputParams.font_size)
    plt4.set_title("X,Y,Z,W = f(t)", fontsize=InputParams.font_size)

    plt.tight_layout()
    plt.savefig("Chua4D_2.png", bbox_inches='tight', dpi=200)

    fig3 = plt.figure()
    fig3.suptitle(InputParams.title)

    plt1 = plt.subplot2grid((2, 2), (0, 0))
    plt1.plot(ModelOut[:, 0], ModelOut[:, 3], 'tab:green')
    plt1.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt1.set_ylabel('$W$', fontsize=InputParams.font_size)
    plt1.set_title("X-W Plot", fontsize=InputParams.font_size)

    plt2 = plt.subplot2grid((2, 2), (0, 1))
    plt2.plot(ModelOut[:, 1], ModelOut[:, 3], 'tab:orange')
    plt2.set_xlabel('$Y$', fontsize=InputParams.font_size)
    plt2.set_ylabel('$W$', fontsize=InputParams.font_size)
    plt2.set_title("Y-W Plot", fontsize=InputParams.font_size)

    plt3 = plt.subplot2grid((2, 2), (1, 0))
    plt3.plot(ModelOut[:, 3], ModelOut[:, 2], 'tab:red')
    plt3.set_xlabel('$W$', fontsize=InputParams.font_size)
    plt3.set_ylabel('$Z$', fontsize=InputParams.font_size)
    plt3.set_title("W-Z Plot", fontsize=InputParams.font_size)

    plt4 = plt.subplot2grid((2, 2), (1, 1))
    plt4.plot(InputParams.time_vector, ModelOut[:, 3])
    plt4.set_xlabel('$t$', fontsize=InputParams.font_size)
    plt4.set_ylabel('$W$', fontsize=InputParams.font_size)
    plt4.set_title("W = f(t)", fontsize=InputParams.font_size)

    plt.tight_layout()
    plt.savefig("Chua4D_3.png", bbox_inches='tight', dpi=200)

    plt.show()
