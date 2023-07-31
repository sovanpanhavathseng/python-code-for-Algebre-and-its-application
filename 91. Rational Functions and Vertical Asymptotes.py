def find_vertical_asymptotes(polynomial):
  """Finds the vertical asymptotes of a rational function.

  Args:
    polynomial: The rational function.

  Returns:
    A list of the vertical asymptotes.
  """

  vertical_asymptotes = []
  denominator = polynomial.denominator

  for i in range(len(denominator.coefficients)):
    if denominator.coefficients[i] == 0:
      vertical_asymptotes.append(-i / denominator.degree)

  return vertical_asymptotes


if __name__ == "__main__":
  polynomial = Polynomial([1, 2, 3, 0, 0])

  vertical_asymptotes = find_vertical_asymptotes(polynomial)

  print(vertical_asymptotes)
