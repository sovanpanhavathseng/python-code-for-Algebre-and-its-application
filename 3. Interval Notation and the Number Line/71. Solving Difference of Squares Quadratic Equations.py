def solve_difference_of_squares(a, b, c):
  """
  Solves a quadratic equation of the form ax^2 + bx + c = 0, where a is not equal to 0.
  The equation is first factored into the difference of two squares, and then the roots are solved.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    A list of the two roots of the equation.
  """

  if a == 0:
    raise ValueError("The coefficient of the x^2 term cannot be 0.")

  # Factor the equation into the difference of two squares.
  x_squared = a * x * x
  b_squared = b * b
  equation = x_squared - b_squared

  # Solve for the roots.
  root1 = (-b + math.sqrt(b_squared + equation)) / (2 * a)
  root2 = (-b - math.sqrt(b_squared + equation)) / (2 * a)

  return [root1, root2]


if __name__ == "__main__":
  a = 2
  b = 3
  c = 1

  roots = solve_difference_of_squares(a, b, c)
  print(roots)
