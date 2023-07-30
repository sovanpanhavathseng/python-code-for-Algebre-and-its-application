def complete_the_square(a, b, c):
  """
  Completes the square for a quadratic equation of the form ax^2 + bx + c = 0.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    A list of the two roots of the equation.
  """

  if a == 0:
    raise ValueError("The coefficient of the x^2 term cannot be 0.")

  # Calculate the constant term for the completed square.
  constant_term = (b * b) / (4 * a)

  # Add and subtract the constant term to complete the square.
  x_squared = a * x * x + b * x
  completed_square = x_squared + constant_term - constant_term

  # Solve for the roots of the completed square.
  root1 = (-b + math.sqrt(b * b - 4 * a * completed_square)) / (2 * a)
  root2 = (-b - math.sqrt(b * b - 4 * a * completed_square)) / (2 * a)

  return [root1, root2]


if __name__ == "__main__":
  a = 2
  b = 3
  c = 1

  roots = complete_the_square(a, b, c)
  print(roots)
