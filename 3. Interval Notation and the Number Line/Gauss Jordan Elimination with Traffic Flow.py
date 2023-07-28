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

def traffic_flow(A):
  """
  Solves a traffic flow problem using Gauss-Jordan Elimination.

  Args:
    A: The traffic flow matrix.

  Returns:
    The flow rates.
  """

  n = A.shape[0]
  flows = np.zeros(n)

  for i in range(n - 1, -1, -1):
    flows[i] = (A[i][-1] - np.sum(A[i][:i])) / A[i][i]

  return flows

def main():
  """
  Main function.
  """

  A = np.array([[1, 2, -1, 0], [-1, 3, 2, 0], [2, -1, 4, 1]])
  print("Traffic flow matrix:")
  print(A)

  flows = traffic_flow(A)
  print("Flow rates:")
  print(flows)

if __name__ == "__main__":
  main()
