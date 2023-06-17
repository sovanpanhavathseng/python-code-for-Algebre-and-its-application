def complement(x):
  """Returns the complement of x."""
  if x == 0:
    return 1
  else:
    return 0


def main():
  """Prints the complement of 0 and 1."""
  print(complement(0))
  print(complement(1))


if __name__ == "__main__":
  main()

This code works by first defining a function called complement(). This function takes a single integer as input, and it returns the complement of that integer. The complement of an integer is the number that, when added to the original integer, equals 1.

For example, the complement of 0 is 1, because 0 + 1 = 1. The complement of 1 is 0, because 1 + 0 = 1.

The complement() function works by first checking if the input integer is equal to 0. If it is, the function simply returns 1. Otherwise, the function returns 0.

The main() function in the code simply prints the complement of 0 and 1.

To run the code, you can save it as a Python file and then run it in a Python interpreter. For example, if you save the code as complement.py, you can run it by typing the following command into a terminal:
