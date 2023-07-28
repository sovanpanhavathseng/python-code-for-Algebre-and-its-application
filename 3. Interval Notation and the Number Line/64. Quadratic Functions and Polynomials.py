import math

def quadratic(a, b, c):
  """
  Returns the value of the quadratic function ax^2 + bx + c at x.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    The value of the quadratic function at x.
  """

  return a * x ** 2 + b * x + c

def roots(a, b, c):
  """
  Returns the roots of the quadratic equation ax^2 + bx + c = 0.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    The roots of the quadratic equation.
  """

  d = b ** 2 - 4 * a * c

  if d > 0:
    roots = (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)
  elif d == 0:
    roots = -b / (2 * a)
  else:
    roots = None

  return roots

def main():
  """
  Main function.
  """

  a = 1
  b = 2
  c = 3

  print("Quadratic function:")
  print(quadratic(a, b, c))

  roots = roots(a, b, c)
  if roots is not None:
    print("Roots of the quadratic equation:")
    print(roots)

if __name__ == "__main__":
  main()
