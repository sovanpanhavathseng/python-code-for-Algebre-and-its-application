def find_nonvertical_asymptotes(polynomial):
  """Finds the nonvertical asymptotes of a rational function.

  Args:
    polynomial: The rational function.

  Returns:
    A list of the nonvertical asymptotes.
  """

  degree_numerator = polynomial.numerator.degree
  degree_denominator = polynomial.denominator.degree

  if degree_numerator > degree_denominator:
    return [float("inf")]
  elif degree_numerator < degree_denominator:
    return [float("-inf")]
  else:
    return [
        float(coefficient) / float(denominator.coefficients[degree_denominator - 1])
        for coefficient in polynomial.numerator.coefficients[degree_numerator - 1:]
    ]


if __name__ == "__main__":
  polynomial = Polynomial([1, 2, 3, 0, 0])

  nonvertical_asymptotes = find_nonvertical_asymptotes(polynomial)

  print(nonvertical_asymptotes)
