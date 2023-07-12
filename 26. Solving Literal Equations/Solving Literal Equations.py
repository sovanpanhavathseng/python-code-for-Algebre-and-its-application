import sympy as sym

def solve_literal_equation(equation):
  """
  Solves a literal equation.

  Args:
    equation: A string representing a literal equation.

  Returns:
    The solution to the equation, as a string.
  """

  equation = sym.sympify(equation)
  solution = sym.solve(equation)
  return str(solution)


if __name__ == "__main__":
  equation = "2 * 3 + 4 / 2 - 1"
  print(solve_literal_equation(equation))

// his code first imports the sympy package, which is a Python library for symbolic mathematics. Then, it defines a function called solve_literal_equation() that takes a string representing a literal equation as input and returns the solution to the equation as a string. The function first converts the equation to a symbolic expression using the sym.sympify() function. Then, it uses the sym.solve() function to solve the equation. Finally, it returns the solution as a string.

// To run the code, you can save it as a .py file and then run it from the command line. For example, if you save the code as solve_literal_equation.py, you can run it by typing the following command into the command line:
