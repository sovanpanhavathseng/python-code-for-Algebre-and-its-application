def multiply_polynomials(polynomial1, polynomial2):
  """Multiplies two polynomials.

  Args:
    polynomial1: The first polynomial.
    polynomial2: The second polynomial.

  Returns:
    A polynomial representing the product of the two polynomials.
  """

  product_coefficients = []
  for coefficient1 in polynomial1.coefficients:
    for coefficient2 in polynomial2.coefficients:
      term_coefficient = coefficient1 * coefficient2
      term_power = polynomial1.degree + polynomial2.degree
      product_coefficients.append(term_coefficient * x ** term_power)

  return Polynomial(product_coefficients)


if __name__ == "__main__":
  polynomial1 = Polynomial([1, 2, 3])
  polynomial2 = Polynomial([4, 5, 6])

  product_polynomial = multiply_polynomials(polynomial1, polynomial2)

  print(product_polynomial)
