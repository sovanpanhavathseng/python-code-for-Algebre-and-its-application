def find_oblique_asymptotes(polynomial):
  """Finds the oblique asymptotes of a rational function.

  Args:
    polynomial: The rational function.

  Returns:
    A list of the oblique asymptotes.
  """

  degree_numerator = polynomial.numerator.degree
  degree_denominator = polynomial.denominator.degree
  leading_coefficient_numerator = polynomial.numerator.coefficients[0]
  leading_coefficient_denominator = polynomial.denominator.coefficients[0]

  if degree_numerator == degree_denominator:
    return []
  else:
    return [
        str(leading_coefficient_numerator / leading_coefficient_denominator)
        + "x"
        + str(degree_denominator - degree_numerator)
    ]


if __name__ == "__main__":
  polynomial = Polynomial([1, 2, 3, 0, 0])

  oblique_asymptotes = find_oblique_asymptotes(polynomial)

  print(oblique_asymptotes)
