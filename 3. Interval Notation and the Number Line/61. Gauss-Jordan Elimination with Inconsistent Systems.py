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

def main():
  """
  Main function.
  """

  A = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
  print("Original matrix:")
  print(A)

  R = gauss_jordan(A)
  print("Reduced matrix:")
  print(R)

if __name__ == "__main__":
  main()
