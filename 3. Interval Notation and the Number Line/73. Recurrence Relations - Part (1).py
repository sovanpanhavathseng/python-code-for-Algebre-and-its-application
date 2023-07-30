def fibonacci(n):
  """
  Calculates the nth Fibonacci number using a recursive function.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
  for i in range(10):
    print(fibonacci(i))
