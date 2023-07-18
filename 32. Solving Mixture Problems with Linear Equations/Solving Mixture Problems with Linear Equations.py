def solve_mixture_problem(acid_concentration, tank_volume, water_to_add):
  """
  Solves a mixture problem using linear equations.

  Args:
    acid_concentration: The initial acid concentration in the tank, as a decimal.
    tank_volume: The initial volume of the tank, in liters.
    water_to_add: The amount of water to add to the tank, in liters.

  Returns:
    The amount of acid in the tank after the water is added, in liters.
  """

  acid_in_tank = acid_concentration * tank_volume
  total_volume = tank_volume + water_to_add
  acid_after_adding_water = acid_in_tank / total_volume * 100

  return acid_after_adding_water


if __name__ == "__main__":
  acid_concentration = 0.4
  tank_volume = 100
  water_to_add = 5

  acid_after_adding_water = solve_mixture_problem(acid_concentration, tank_volume, water_to_add)

  print("The amount of acid in the tank after adding water is", acid_after_adding_water, "liters.")

// This code first defines a function called solve_mixture_problem(). This function takes three arguments: the initial acid concentration in the tank, the initial volume of the tank, and the amount of water to add. The function then calculates the amount of acid in the tank after the water is added, and returns the value.

// The main function of the code then calls the solve_mixture_problem() function with the given values, and prints the result.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as mixture.py, you can run it by typing the following command into the command line:
