def is_unbounded_interval(interval):
  """Returns True if the interval is unbounded, False otherwise."""
  lower_bound = interval[0]
  upper_bound = interval[1]
  return lower_bound is None or upper_bound is None

def main():
  unbounded_interval_1 = (-float("inf"), float("inf"))
  unbounded_interval_2 = (None, None)
  print("The unbounded interval 1 is", unbounded_interval_1, "and it is", is_unbounded_interval(unbounded_interval_1))
  print("The unbounded interval 2 is", unbounded_interval_2, "and it is", is_unbounded_interval(unbounded_interval_2))

if __name__ == "__main__":
  main()

// This code defines a function, is_unbounded_interval, which takes an interval as input and returns True if the interval is unbounded. The main function then defines two unbounded intervals and prints out whether each interval is unbounded.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as unbounded_intervals.py, you can run it by typing the following command into the command line:
