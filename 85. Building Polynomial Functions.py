def build_polynomial(coefficients):
  """Returns a polynomial from the given coefficients.

  Args:
    coefficients: A list of the coefficients of the polynomial.

  Returns:
    A polynomial.
  """

  polynomial = Polynomial([])
  for coefficient in coefficients:
    polynomial += monomial(coefficient, len(coefficients) - 1)

  return polynomial


if __name__ == "__main__":
  coefficients = [1, 2, 3]

  polynomial = build_polynomial(coefficients)

  print(polynomial)
  print(polynomial.evaluate(2))
