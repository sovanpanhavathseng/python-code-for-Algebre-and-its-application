def add_polynomials(polynomial1, polynomial2):
  """Adds two polynomials.

  Args:
    polynomial1: The first polynomial.
    polynomial2: The second polynomial.

  Returns:
    A polynomial representing the sum of the two polynomials.
  """

  coefficients = []
  for i in range(len(polynomial1.coefficients)):
    coefficient = polynomial1.coefficients[i] + polynomial2.coefficients[i]
    coefficients.append(coefficient)

  return Polynomial(coefficients)


def subtract_polynomials(polynomial1, polynomial2):
  """Subtracts two polynomials.

  Args:
    polynomial1: The first polynomial.
    polynomial2: The second polynomial.

  Returns:
    A polynomial representing the difference of the two polynomials.
  """

  coefficients = []
  for i in range(len(polynomial1.coefficients)):
    coefficient = polynomial1.coefficients[i] - polynomial2.coefficients[i]
    coefficients.append(coefficient)

  return Polynomial(coefficients)


if __name__ == "__main__":
  polynomial1 = Polynomial([1, 2, 3])
  polynomial2 = Polynomial([4, 5, 6])

  sum_polynomial = add_polynomials(polynomial1, polynomial2)
  difference_polynomial = subtract_polynomials(polynomial1, polynomial2)

  print(sum_polynomial)
  print(difference_polynomial)
