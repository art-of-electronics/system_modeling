import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class InputParams:
    a = 0.7
    b = 0.8
    e = 0.1
    
    A = 0.8
    f = 0.7

    init = [1.0, 1.0]
    time_vector = np.arange(0.0, 300.0, 0.01)

    n = len(time_vector)

    font_size: int = 10
    title = f"FitzHugh-Nagumo\na={a:.1f}, b={b:.1f}, $\\epsilon$={e:.1f}"


def fitzhugh_nagumo(state, time):
    v, w = state
    return v - v ** 3 / 3 - w + (InputParams.A * np.sin(InputParams.f * time)), \
        InputParams.e * (v + InputParams.a - InputParams.b * w)


if __name__ == '__main__':

    ModelOutput = odeint(fitzhugh_nagumo, InputParams.init, InputParams.time_vector)
    
    fig1 = plt.figure()
    ax = fig1.add_subplot()
    ax.plot(ModelOutput[:, 0], ModelOutput[:, 1])
    ax.set_xlabel('v', fontsize=InputParams.font_size)
    ax.set_ylabel("w", fontsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("FitzHugh-Nagumo_1.png", bbox_inches='tight', dpi=200)
    
    fig2 = plt.figure()
    ax = fig2.add_subplot()
    ax.plot(InputParams.time_vector, ModelOutput[:, 0], InputParams.time_vector, ModelOutput[:, 1])
    ax.set_xlabel('t [s]', fontsize=InputParams.font_size)
    ax.set_ylabel('v, w', fontsize=InputParams.font_size)
    ax.legend(['$v$', "$w$"], fontsize=InputParams.font_size)
    ax.set_title(InputParams.title)
    plt.savefig("FitzHugh-Nagumo_2.png", bbox_inches='tight', dpi=200)

    plt.show()
