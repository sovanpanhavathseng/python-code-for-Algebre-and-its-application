import numpy as np

def solve_system_elimination(equations):
  """
  Solves a system of linear equations by elimination.

  Args:
    equations: A list of lists, where each list represents an equation in standard form.

  Returns:
    A list of two numbers, representing the solution to the system of equations.
  """

  augmented_matrix = np.array(equations)
  for i in range(len(augmented_matrix) - 1):
    for j in range(i + 1, len(augmented_matrix)):
      if augmented_matrix[i][1] != 0 and augmented_matrix[j][1] != 0:
        multiplier = augmented_matrix[j][1] / augmented_matrix[i][1]
        augmented_matrix[j] = augmented_matrix[j] - multiplier * augmented_matrix[i]

  x = augmented_matrix[-1][0] / augmented_matrix[-1][1]
  y = augmented_matrix[-2][0] / augmented_matrix[-2][1]

  return [x, y]


if __name__ == "__main__":
  equations = [[2, 1, 5], [1, -1, 2]]
  solution = solve_system_elimination(equations)
  print(solution)

// This code first creates an augmented matrix from the list of equations. The augmented matrix is a matrix that contains the coefficients of the variables in the equations, as well as the constants on the right-hand side of the equations.

// The code then loops through the augmented matrix and eliminates one variable at a time. This is done by subtracting a multiple of one row from another row, in such a way that the coefficient of one variable in one of the rows becomes 0.

// Once all the variables have been eliminated, the code solves for the remaining variable and returns the solution.

// To run the code, you can save it as a Python file and then run it from the command line. For example, if you save the code as solve_system_elimination.py, you can run it by typing the following command into the command line:
