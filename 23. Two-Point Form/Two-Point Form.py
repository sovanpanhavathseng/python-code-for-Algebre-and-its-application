def two_point_form(x1, y1, x2, y2):
  """Returns the equation of a line in two-point form."""
  m = (y2 - y1) / (x2 - x1)
  y_intercept = y1 - m * x1
  return "y - {0} = {1}(x - {2})".format(y_intercept, m, x1)

if __name__ == "__main__":
  print(two_point_form(2, 3, 4, 5))

// This code takes four arguments: the x- and y-coordinates of two points on the line. It then calculates the slope of the line and the y-intercept, and returns the equation of the line in two-point form.

// To run the code, you can save it as a Python file and then run it from the command line. For example, if you save the code as two_point_form.py, you can run it by typing the following command into the command line:
