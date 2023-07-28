def foil(a, b, c, d):
  """
  Creates a quadratic expression using the FOIL method.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.
    d: The coefficient of the x^2 term in the second binomial.

  Returns:
    The quadratic expression.
  """

  expression = a * x ** 2 + (a * d + b * c) * x + c * d

  return expression

def main():
  """
  Main function.
  """

  a = 1
  b = 2
  c = 3
  d = 4

  expression = foil(a, b, c, d)
  print("Quadratic expression:")
  print(expression)

if __name__ == "__main__":
  main()