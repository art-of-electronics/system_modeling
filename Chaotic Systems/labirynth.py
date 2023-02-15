import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    b = 0.19

    init = [1.0, 0.8, 0.8]
    time_vector = np.arange(0.0, 500.0, 0.1)

    n = len(time_vector)

    font_size: int = 10
    title = f"Labirynth\n$b$={b:.2f}"


def labyrinth(state, __time__):
    x, y, z = state
    return np.sin(y) - InputParams.b * x, np.sin(z) - InputParams.b * y, np.sin(x) - InputParams.b * z


if __name__ == '__main__':

    ModelOutput = odeint(labyrinth, InputParams.init, InputParams.time_vector)

    fig1 = plt.figure()
    ax = fig1.add_subplot(projection="3d")
    ax.plot(ModelOutput[:, 0], ModelOutput[:, 1], ModelOutput[:, 2])
    ax.set_xlabel('$X$', fontsize=InputParams.font_size)
    ax.set_ylabel('$Y$', fontsize=InputParams.font_size)
    ax.set_zlabel('$Z$', fontsize=InputParams.font_size)
    ax.xaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.yaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.zaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("Labyrinth_1.png", bbox_inches='tight', dpi=200)

    fig2 = plt.figure()
    ax = fig2.add_subplot(projection="3d")

    ax.scatter(ModelOutput[:, 0], ModelOutput[:, 1], ModelOutput[:, 2],
               c=np.linspace(0, 1, InputParams.n), cmap=plt.jet())

    ax.set_xlabel('$X$', fontsize=InputParams.font_size)
    ax.set_ylabel('$Y$', fontsize=InputParams.font_size)
    ax.set_zlabel('$Z$', fontsize=InputParams.font_size)
    ax.xaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.yaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.zaxis.set_tick_params(labelsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("Labyrinth_2.png", bbox_inches='tight', dpi=200)

    plt.show()
