import matplotlib.pyplot as plt
import numpy as np


def graph_polynomial(coefficients, x_min, x_max, y_min, y_max):
  """Graphs a polynomial function.

  Args:
    coefficients: A list of the coefficients of the polynomial.
    x_min: The minimum value of x.
    x_max: The maximum value of x.
    y_min: The minimum value of y.
    y_max: The maximum value of y.
  """

  x_values = np.linspace(x_min, x_max, 100)
  y_values = [polynomial.evaluate(x) for x in x_values]

  plt.plot(x_values, y_values)
  plt.ylim(y_min, y_max)
  plt.show()


if __name__ == "__main__":
  coefficients = [1, 2, 3]

  graph_polynomial(coefficients, -1, 4, -5, 10)
