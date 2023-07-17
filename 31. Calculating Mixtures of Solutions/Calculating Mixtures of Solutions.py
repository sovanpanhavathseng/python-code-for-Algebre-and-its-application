def calculate_mixture(volume_1, concentration_1, volume_2, concentration_2):
  """Calculates the quantity of a substance in a mixture of two solutions.

  Args:
    volume_1: The volume of the first solution.
    concentration_1: The percent concentration of the substance in the first solution.
    volume_2: The volume of the second solution.
    concentration_2: The percent concentration of the substance in the second solution.

  Returns:
    The quantity of the substance in the mixture.
  """

  quantity_1 = volume_1 * concentration_1 / 100
  quantity_2 = volume_2 * concentration_2 / 100
  return quantity_1 + quantity_2


if __name__ == "__main__":
  volume_1 = 250
  concentration_1 = 10
  volume_2 = 250
  concentration_2 = 50
  quantity = calculate_mixture(volume_1, concentration_1, volume_2, concentration_2)
  print("The quantity of the substance in the mixture is:", quantity)

// This code first defines a function called calculate_mixture(). This function takes four arguments: the volume of the first solution, the percent concentration of the substance in the first solution, the volume of the second solution, and the percent concentration of the substance in the second solution. The function then calculates the quantity of the substance in the mixture by adding the quantities of the substance from each solution.

// The code then defines a main function. This function sets the values of the four arguments and then calls the calculate_mixture() function. The function then prints the quantity of the substance in the mixture.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you saved the code as mixture.py, you could run it by typing the following command into the command line:
