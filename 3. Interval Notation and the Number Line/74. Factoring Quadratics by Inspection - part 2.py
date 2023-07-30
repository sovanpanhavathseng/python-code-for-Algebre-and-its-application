def factor_quadratic_by_inspection(a, b, c):
  """
  Factors a quadratic equation of the form ax^2 + bx + c = 0 by inspection.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    A list of the two factors of the equation.
  """

  factors = []

  # Check if the quadratic is a perfect square.
  if b * b == 4 * a * c:
    root = math.sqrt(b * b - 4 * a * c) / (2 * a)
    factors.append((root, root))
    return factors

  # Check if the quadratic can be factored as the difference of two squares.
  if c == 0:
    return factors
  elif b % 2 == 0:
    b_half = b / 2
    if c % b_half == 0:
      factors.append((b_half, c / b_half))
      return factors

  # Check if the quadratic can be factored as the sum and product of two linear expressions.
  for i in range(1, int(math.sqrt(c)) + 1):
    if c % i == 0:
      factors.append((i, c / i))
  return factors


if __name__ == "__main__":
  a = 2
  b = 3
  c = 1

  factors = factor_quadratic_by_inspection(a, b, c)
  print(factors)
