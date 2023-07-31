import math


def quadratic_formula(a, b, c):
  """Returns the roots of the quadratic equation ax^2 + bx + c = 0."""
  discriminant = b ** 2 - 4 * a * c
  if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2
  else:
    return None, None


def main():
  """Prints the roots of the quadratic equation x^2 + 2x + 1 = 0."""
  a, b, c = 1, 2, 1
  roots = quadratic_formula(a, b, c)
  print("The roots are", roots)


if __name__ == "__main__":
  main()
