def complete_square(x, a):
  """Completes the square for the given number x and coefficient a."""
  b = 2 * a * x
  c = a ** 2
  return b ** 2 + c


def main():
  """Prints the result of completing the square for the number 2."""
  print(complete_square(2, 1))


if __name__ == "__main__":
  main()
