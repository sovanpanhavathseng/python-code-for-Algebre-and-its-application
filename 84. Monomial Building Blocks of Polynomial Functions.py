def monomial(coefficient, degree):
  """Returns a monomial with the given coefficient and degree.

  Args:
    coefficient: The coefficient of the monomial.
    degree: The degree of the monomial.

  Returns:
    A monomial.
  """

  if degree == 0:
    return coefficient
  else:
    return coefficient * x ** degree


if __name__ == "__main__":
  print(monomial(2, 0))
  print(monomial(3, 1))
  print(monomial(-1, 2))
