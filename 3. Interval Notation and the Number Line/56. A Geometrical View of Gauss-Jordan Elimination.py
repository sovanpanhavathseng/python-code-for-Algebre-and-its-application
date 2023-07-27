import numpy as np
import matplotlib.pyplot as plt

def gauss_jordan_elimination(A, b):
  """Performs Gauss-Jordan elimination on the matrix A and vector b.

  Args:
    A: The coefficient matrix.
    b: The right-hand side vector.

  Returns:
    The solution vector x.
  """

  n = A.shape[0]
  for i in range(n):
    # Find the row with the largest leading entry in the current column.
    max_row = i
    for j in range(i + 1, n):
      if abs(A[j, i]) > abs(A[max_row, i]):
        max_row = j

    # Swap rows i and max_row.
    A[[i, max_row]] = A[[max_row, i]]
    b[[i, max_row]] = b[[max_row, i]]

    # Scale the row so that the leading entry is 1.
    if A[i, i] != 0:
      A[i, :] = A[i, :] / A[i, i]
    b[i] = b[i] / A[i, i]

    # Subtract multiples of the leading row from the other rows.
    for j in range(i + 1, n):
      if A[j, i] != 0:
        factor = A[j, i] / A[i, i]
        A[j, :] -= factor * A[i, :]
        b[j] -= factor * b[i]

  return b

def main():
  """Runs the Gauss-Jordan elimination algorithm."""

  A = np.array([[1, 2, -3], [-2, 1, 4], [3, -1, -2]])
  b = np.array([1, 2, 3])

  x = gauss_jordan_elimination(A, b)
  print(x)

if __name__ == "__main__":
  main()