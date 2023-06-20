def interval_notation(a, b):
  """
  Converts a range of real numbers to interval notation.

  Args:
    a: The lower bound of the range.
    b: The upper bound of the range.

  Returns:
    The interval notation for the range.
  """

  if a <= b:
    return "[" + str(a) + ", " + str(b) + "]"
  else:
    return "(" + str(a) + ", " + str(b) + ")"


def main():
  print(interval_notation(2, 5))
  print(interval_notation(-1, 3))
  print(interval_notation(-1, -2))


if __name__ == "__main__":
  main()

// This code first defines a function called interval_notation() that takes two numbers as input, a and b, and returns the interval notation for the range of real numbers between a and b. The function uses the if statement to check if a is less than or equal to b. If it is, the function returns the interval notation [a, b]. If a is greater than b, the function returns the interval notation (a, b).

// The main function of the code then calls the interval_notation() function three times, with the arguments 2, 5, -1, 3, and -1, -2. The code then prints the results of the function calls.

// To run the code, you can save it as a Python file and then run it from the command line. For example, if you save the code as interval_notation.py, you can run it by typing the following command into the command line:
