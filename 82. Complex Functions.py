def complex_function(x):
  """Returns the complex function f(x) = x^2 + 2x + 1.

  Args:
    x: The input value.

  Returns:
    The result of the complex function.
  """

  return x ** 2 + 2 * x + 1


if __name__ == "__main__":
  x = 2

  result = complex_function(x)

  print(result)
