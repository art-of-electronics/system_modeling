import numpy as np
import matplotlib.pyplot as plt
from pylab import array
from ddeint import ddeint
from scipy.ndimage import shift


class InputParams:
    gamma = 1
    beta = 2
    tau = 5
    n = 10

    k = 100.0
    delay = k * tau

    @staticmethod
    def g(self): return array([0.2, 0.2])

    init = [0.7, 0, 0]
    time_vector = np.arange(0.0, 50, 1 / k)

    font_size: int = 10
    title = f"Mackey-Glass\n$\\gamma$={gamma:.2f}, $\\beta$={beta:.1f}, $\\tau$={tau:.1f}, $n$={n:d}"


def mackey_glass(x, time, d):
    _x = x(time)
    _xt = x(time - d)
    return InputParams.beta * _xt / (1 + _xt ** InputParams.n) - _x * InputParams.gamma


if __name__ == '__main__':

    ModelOutput = ddeint(mackey_glass, InputParams.g, InputParams.time_vector, fargs=(InputParams.tau,))

    ModelOutput[:, 1] = shift(ModelOutput[:, 1], InputParams.delay, cval=0.2)

    fig1 = plt.figure()
    ax = fig1.add_subplot()
    ax.plot(ModelOutput[:, 1], ModelOutput[:, 0])
    ax.set_xlabel('$x(t)$', fontsize=InputParams.font_size)
    ax.set_ylabel('$x(t-\\tau)$', fontsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("MackeyGlass_1.png", bbox_inches='tight', dpi=200)

    fig2 = plt.figure()
    ax = fig2.add_subplot()
    ax.plot(InputParams.time_vector, ModelOutput)
    ax.set_xlabel('t [s]', fontsize=InputParams.font_size)
    ax.set_ylabel('Y', fontsize=InputParams.font_size)
    ax.legend(['$x(t)$', '$x(t-\\tau)$'], fontsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("MackeyGlass_2.png", bbox_inches='tight', dpi=200)

    plt.show()
