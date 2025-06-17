import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    lambda_val: int = 1

    init = [-0.0824, 0.245, 0.508, -0.0408]
    time_vector = np.arange(0.0, 150.0, 0.01)

    font_size: int = 10
    title = f"Henon-Heiles\n$\\lambda$={lambda_val:d}, $x_{0}$={init[0]:.4f}, " \
            f"$y_{0}$={init[0]:.4f}, $Px$={init[0]:.4f}, $Py$={init[0]:.4f}"


def henon_heiles(x, __time__):
    _x = - x[0] - 2 * InputParams.lambda_val * x[0] * x[2]
    _y = - x[2] - InputParams.lambda_val * (x[0] ** 2 - x[2] ** 2)
    return x[1], _x, x[3], _y


if __name__ == '__main__':

    ModelOutput = odeint(henon_heiles, InputParams.init, InputParams.time_vector)

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
    plt.savefig("HenonHeiles_1.png", bbox_inches='tight', dpi=200)

    fig2 = plt.figure()
    fig2.suptitle(InputParams.title)

    plt1 = plt.subplot2grid((2, 2), (0, 0))
    plt1.plot(ModelOutput[:, 0], ModelOutput[:, 1], 'tab:green')
    plt1.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt1.set_ylabel('$Y$', fontsize=InputParams.font_size)
    plt1.set_title("$X-Y$ Plot", fontsize=InputParams.font_size)

    plt2 = plt.subplot2grid((2, 2), (0, 1))
    plt2.plot(ModelOutput[:, 2], ModelOutput[:, 3], 'tab:orange')
    plt2.set_xlabel('$P_{x}$', fontsize=InputParams.font_size)
    plt2.set_ylabel('$P_{y}$', fontsize=InputParams.font_size)
    plt2.set_title("$P_{x}-P_{y}$ Plot", fontsize=InputParams.font_size)

    plt3 = plt.subplot2grid((2, 2), (1, 0))
    plt3.plot(ModelOutput[:, 0], ModelOutput[:, 2], 'tab:red')
    plt3.set_xlabel('$X$', fontsize=InputParams.font_size)
    plt3.set_ylabel('$P_{x}$', fontsize=InputParams.font_size)
    plt3.set_title("$X-P_{x}$ Plot", fontsize=InputParams.font_size)

    plt4 = plt.subplot2grid((2, 2), (1, 1))
    plt4.plot(ModelOutput[:, 1], ModelOutput[:, 3], 'tab:blue')
    plt4.set_xlabel('$Y$', fontsize=InputParams.font_size)
    plt4.set_ylabel('$P_{y}$', fontsize=InputParams.font_size)
    plt4.set_title("$Y-P_{y}$ Plot", fontsize=InputParams.font_size)

    plt.tight_layout()
    plt.savefig("HenonHeiles_2.png", bbox_inches='tight', dpi=200)

    plt.show()
