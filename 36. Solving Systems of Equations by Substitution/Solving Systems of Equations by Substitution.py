def solve_system_by_substitution(a, b, c, d, e, f):
  """
  Solves a system of equations by substitution.

  Args:
    a: The coefficient of x in the first equation.
    b: The constant term in the first equation.
    c: The coefficient of x in the second equation.
    d: The constant term in the second equation.
    e: The value of x.
    f: The value of y.

  Returns:
    A tuple of the values of x and y.
  """

  x = e / a
  y = (f - c * x) / d
  return x, y

if __name__ == "__main__":
  a = 1
  b = 2
  c = 3
  d = 4
  e = 5
  f = 6

  x, y = solve_system_by_substitution(a, b, c, d, e, f)
  print(x, y)

// This code first defines a function called solve_system_by_substitution(). This function takes in the coefficients and constants of the two equations, as well as the values of x and y, and returns the values of x and y.

// The function then solves the first equation for x, and substitutes that value into the second equation. This gives us a single equation with one variable, which we can then solve for y.

// Finally, the function returns the values of x and y.

// To run the code, we can save it as a Python file and then run it from the command line. For example, if we save the code as solve_system_by_substitution.py, we can run it by typing the following command into the command line:
