import numpy as np
import matplotlib.pyplot as plt

# from eqn a1x + a2y = b


def plot_lines(A, b):
    # get as many x values so we substitute to get as many y values
    x_values = np.linspace(-5, 5, 100)

    # get a1 and a2
    for i in range(A.shape[0]):  # only row in the matrix we need
        a1, a2 = A[i]

        # get y by making it standalone in the linear eqn
        if a2 != 0:
            y_values = (b[i] - a1 * x_values) / a2
            plt.plot(x_values, y_values, label=f"{a1}x + {a2}y = {b[i]}")
        else:
            # make a2 = 0  and x to standalone
            x_const = b[i] / a1
            plt.axvline(x=x_const, label=f"{a1}x = {b[i]}")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0)
    plt.axvline(0)
    plt.legend()
    plt.grid()
    plt.title("Linear Equations")
    plt.show()
