import math


class Polynomial:
  """A class to represent polynomials.

  Attributes:
    coefficients: A list of the coefficients of the polynomial.
  """

  def __init__(self, coefficients):
    """Initializes a polynomial.

    Args:
      coefficients: A list of the coefficients of the polynomial.
    """

    self.coefficients = coefficients

  def __repr__(self):
    """Returns a string representation of the polynomial."""

    string = ""
    for coefficient in self.coefficients:
      string += f"{coefficient}x^{len(self.coefficients) - 1 - i}"
      i += 1

    return string[1:]

  def evaluate(self, x):
    """Evaluates the polynomial at x.

    Args:
      x: The value to evaluate the polynomial at.

    Returns:
      The value of the polynomial at x.
    """

    value = 0
    for coefficient, power in zip(self.coefficients, range(len(self.coefficients))):
      value += coefficient * math.pow(x, power)

    return value


if __name__ == "__main__":
  polynomial = Polynomial([1, 2, 3])

  print(polynomial)
  print(polynomial.evaluate(2))
