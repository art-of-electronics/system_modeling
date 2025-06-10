import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    mu = 5

    init = [0.0, 0.1, 0.0, 0.1]
    time_vector = np.arange(0.0, 100.0, 0.01)

    font_size: int = 10
    title = f"Hyper chaotic Van der Pol\n$\\mu$={mu:.1f}"


def hyper_van_der_pol(y, __time__):
    r1 = InputParams.mu * (y[2] - (y[2] ** 3) / 3 - y[0])
    r2 = y[2] / InputParams.mu
    return y[3], r1, y[1], r2


if __name__ == '__main__':

    ModelOutput = odeint(hyper_van_der_pol, InputParams.init, InputParams.time_vector)

    fig1 = plt.figure()
    ax = fig1.add_subplot(projection='3d')
    ax.plot(ModelOutput[:, 0], ModelOutput[:, 2], ModelOutput[:, 1], 'tab:olive')
    ax.plot(ModelOutput[:, 0], ModelOutput[:, 2], ModelOutput[:, 3], 'tab:red')
    ax.legend(['$P_{x}$', '$P_{y}$'], fontsize=InputParams.font_size)
    ax.set_xlabel('$X$', fontsize=InputParams.font_size)
    ax.set_ylabel('$Y$', fontsize=InputParams.font_size)
    ax.set_zlabel('$P_{x}, P_{y}$', fontsize=InputParams.font_size)
    ax.xaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.yaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.zaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("VanderPol4D_1.png", bbox_inches='tight', dpi=200)

    fig2 = plt.figure()
    fig2.suptitle(InputParams.title)

    plt1 = plt.subplot2grid((2, 2), (0, 0))
    plt1.plot(ModelOutput[:, 2], ModelOutput[:, 0], 'tab:green')
    plt1.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt1.set_ylabel('$Y$', fontsize=InputParams.font_size)
    plt1.set_title("$X-Y$ Plot", fontsize=InputParams.font_size)

    plt2 = plt.subplot2grid((2, 2), (0, 1))
    plt2.plot(ModelOutput[:, 3], ModelOutput[:, 1], 'tab:orange')
    plt2.set_xlabel("$X'$", fontsize=InputParams.font_size)
    plt2.set_ylabel("$Y'$", fontsize=InputParams.font_size)
    plt2.set_title("$X'-Y'$ Plot", fontsize=InputParams.font_size)

    plt3 = plt.subplot2grid((2, 2), (1, 0))
    plt3.plot(ModelOutput[:, 2], ModelOutput[:, 3], 'tab:red')
    plt3.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt3.set_ylabel("$X'$", fontsize=InputParams.font_size)
    plt3.set_title("$X-X'$ Plot", fontsize=InputParams.font_size)

    plt4 = plt.subplot2grid((2, 2), (1, 1))
    plt4.plot(ModelOutput[:, 0], ModelOutput[:, 1], 'tab:blue')
    plt4.set_xlabel('$Y$', fontsize=InputParams.font_size)
    plt4.set_ylabel("$Y'$", fontsize=InputParams.font_size)
    plt4.set_title("$Y-Y'$ Plot", fontsize=InputParams.font_size)

    plt.tight_layout()
    plt.savefig("VanderPol4D_2.png", bbox_inches='tight', dpi=200)

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
    plt.savefig("VanderPol4D_3.png", bbox_inches='tight', dpi=200)

    plt.show()
