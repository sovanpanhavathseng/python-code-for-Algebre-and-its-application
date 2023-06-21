def is_bounded_interval(interval):
  """Returns True if the interval is bounded, False otherwise."""
  lower_bound = interval[0]
  upper_bound = interval[1]
  return lower_bound is not None and upper_bound is not None

def is_unbounded_interval(interval):
  """Returns True if the interval is unbounded, False otherwise."""
  return not is_bounded_interval(interval)

def main():
  bounded_interval = [-2, 3]
  unbounded_interval = (-float("inf"), float("inf"))
  print("The bounded interval is", bounded_interval, "and it is", is_bounded_interval(bounded_interval))
  print("The unbounded interval is", unbounded_interval, "and it is", is_unbounded_interval(unbounded_interval))

if __name__ == "__main__":
  main()

// This code defines two functions, is_bounded_interval and is_unbounded_interval, which take an interval as input and return True if the interval is bounded or unbounded, respectively. The main function then defines two intervals, a bounded interval and an unbounded interval, and prints out whether each interval is bounded or unbounded.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as bounded_unbounded_intervals.py, you can run it by typing the following command into the command line:
