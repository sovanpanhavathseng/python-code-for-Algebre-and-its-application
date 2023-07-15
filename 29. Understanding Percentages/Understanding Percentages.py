def calculate_percentage(part, whole):
  """Calculates the percentage of a part over a whole.

  Args:
    part: The part of the whole.
    whole: The whole.

  Returns:
    The percentage of the part over the whole.
  """

  percentage = (part / whole) * 100
  return percentage


def main():
  """Prints the percentage of 50 out of 100."""

  percentage = calculate_percentage(50, 100)
  print(f"50 out of 100 is {percentage}%")


if __name__ == "__main__":
  main()

// This code first defines a function called calculate_percentage(). This function takes two arguments, part and whole, and returns the percentage of part over whole. The function works by dividing part by whole and then multiplying the result by 100.

// The code then defines a function called main(). This function prints the percentage of 50 out of 100. The function calls the calculate_percentage() function to calculate the percentage, and then prints the result.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as percentages.py, you can run it by typing the following command into the command line:
