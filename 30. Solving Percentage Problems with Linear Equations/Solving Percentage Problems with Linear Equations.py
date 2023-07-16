def solve_percentage_problem(original_price, percentage_increase):
  """
  Solves a percentage problem using a linear equation.

  Args:
    original_price: The original price of the item.
    percentage_increase: The percentage increase in price.

  Returns:
    The new price of the item.
  """

  percentage_increase = percentage_increase / 100
  new_price = original_price + (original_price * percentage_increase)
  return new_price


if __name__ == "__main__":
  original_price = 50
  percentage_increase = 20
  new_price = solve_percentage_problem(original_price, percentage_increase)
  print("The new price is: ${}".format(new_price))

// This code first defines a function called solve_percentage_problem(). This function takes two arguments: the original price of the item and the percentage increase in price. The function then converts the percentage increase to a decimal or fraction, and then calculates the new price of the item. The function then returns the new price.

// The code then defines a main function. The main function takes the original price and the percentage increase as input, and then calls the solve_percentage_problem() function to calculate the new price. The main function then prints the new price.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as percentage_problem.py, you can run it by typing the following command into the command line:
