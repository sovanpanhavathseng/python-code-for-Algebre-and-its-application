import numpy as np

def least_squares_approximation(x, y):
  """
  Performs least squares approximation on the data points (x, y).

  Args:
    x: The x-coordinates of the data points.
    y: The y-coordinates of the data points.

  Returns:
    m: The slope of the least squares line.
    b: The y-intercept of the least squares line.
  """

  n = len(x)
  A = np.zeros((n, 2))
  b = np.zeros(n)

  for i in range(n):
    A[i, 0] = x[i]
    A[i, 1] = 1
    b[i] = y[i]

  m, b = np.linalg.lstsq(A, b)[0]

  return m, b

if name == "__main__":
  x = np.array([1, 2, 3, 4, 5])
  y = np.array([2, 4, 6, 8, 10])
  m, b = least_squares_approximation(x, y)
  print(m, b)