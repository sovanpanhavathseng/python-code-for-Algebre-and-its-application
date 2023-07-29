import math

def quadratic(a, b, c):
  """Returns the roots of a quadratic equation."""
  if a == 0:
    if b == 0:
      return []
    else:
      return [-c / b]
  else:
    delta = b * b - 4 * a * c
    if delta < 0:
      return []
    elif delta == 0:
      return [-b / (2 * a)]
    else:
      return [(-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)]

if __name__ == "__main__":
  a = 1
  b = 2
  c = 1
  roots = quadratic(a, b, c)
  print(roots)
