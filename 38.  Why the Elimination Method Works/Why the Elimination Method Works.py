def elimination_method(x_eq, y_eq):
  """
  Solves a system of linear equations using the elimination method.

  Args:
    x_eq: The first equation in the system.
    y_eq: The second equation in the system.

  Returns:
    The solution to the system of equations.
  """

  x_coeff = x_eq[0]
  y_coeff = y_eq[0]

  # Check if the coefficients of `y` are opposites.

  if x_coeff * y_coeff != -1:
    # If not, multiply one of the equations by -1.
    y_eq = y_eq * -1

  # Add the equations together.

  solution = x_eq + y_eq

  # Solve for `x`.

  x = solution[0] / solution[1]

  # Return the solution.

  return x

if __name__ == "__main__":
  # The system of equations.

  x_eq = [1, 1]
  y_eq = [2, -1]

  # Solve the system of equations.

  solution = elimination_method(x_eq, y_eq)

  # Print the solution.

  print(solution)

// This code first checks if the coefficients of y in the two equations are opposites. If they are not, the code multiplies one of the equations by -1 to make them opposites. Then, the code adds the two equations together to eliminate the variable y. Finally, the code solves for x and returns the solution.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as elimination_method.py, you can run it by typing the following command into the command line:
