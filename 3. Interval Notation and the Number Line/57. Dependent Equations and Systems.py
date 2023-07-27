import numpy as np

def dependent_equations(a, b, c):
  """Returns True if the equations are dependent, False otherwise."""

  if a * b == c:
    return True
  else:
    return False

def main():
  """Runs the dependent equations function."""

  a = 1
  b = 2
  c = 3

  if dependent_equations(a, b, c):
    print("The equations are dependent.")
  else:
    print("The equations are independent.")

if __name__ == "__main__":
  main()
