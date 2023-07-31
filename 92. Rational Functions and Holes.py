def find_holes(polynomial):
  """Finds the holes of a rational function.

  Args:
    polynomial: The rational function.

  Returns:
    A list of the holes.
  """

  holes = []
  denominator = polynomial.denominator
  numerator = polynomial.numerator

  for i in range(len(denominator.coefficients)):
    if denominator.coefficients[i] == 0 and numerator.coefficients[i] != 0:
      holes.append(-i / denominator.degree)

  return holes


if __name__ == "__main__":
  polynomial = Polynomial([1, 2, 3, 0, 0])

  holes = find_holes(polynomial)

  print(holes)
