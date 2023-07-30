def solve_perfect_square(a, b, c):
  """
  Solves a quadratic equation of the form ax^2 + bx + c = 0, where a is not equal to 0.
  The equation is first checked to see if it is a perfect square, and then the roots are solved.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    A list of the two roots of the equation.
  """

  if a == 0:
    raise ValueError("The coefficient of the x^2 term cannot be 0.")

  # Check if the equation is a perfect square.
  if b * b == 4 * a * c:
    root = math.sqrt(b * b - 4 * a * c) / (2 * a)
    return [root, root]
  else:
    return solve_difference_of_squares(a, b, c)


if __name__ == "__main__":
  a = 2
  b = 3
  c = 1

  roots = solve_perfect_square(a, b, c)
  print(roots)
