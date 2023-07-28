import numpy as np

def gauss_jordan(A):
  """
  Performs Gauss-Jordan Elimination on the matrix A.

  Args:
    A: The matrix to be reduced.

  Returns:
    The reduced matrix.
  """

  n = A.shape[0]

  for i in range(n):
    max_row = i
    for j in range(i + 1, n):
      if abs(A[j][i]) > abs(A[max_row][i]):
        max_row = j

    if max_row != i:
      A[[i, max_row]] = A[[max_row, i]]

    for j in range(i + 1, n):
      A[j] -= A[i] * A[j][i] / A[i][i]

  return A

def curve_fitting(x, y):
  """
  Performs curve fitting using Gauss-Jordan Elimination.

  Args:
    x: The independent variable.
    y: The dependent variable.

  Returns:
    The coefficients of the fitted curve.
  """

  n = len(x)
  A = np.zeros((n, n + 1))

  for i in range(n):
    for j in range(n + 1):
      if j == 0:
        A[i][j] = 1
      elif j == i:
        A[i][j] = x[i]
      else:
        A[i][j] = x[i] ** j

  R = gauss_jordan(A)
  coefficients = R[0, 1:]

  return coefficients

def main():
  """
  Main function.
  """

  x = np.array([1, 2, 3, 4, 5])
  y = np.array([2, 4, 6, 8, 10])

  coefficients = curve_fitting(x, y)
  print("Coefficients:")
  print(coefficients)

if __name__ == "__main__":
  main()