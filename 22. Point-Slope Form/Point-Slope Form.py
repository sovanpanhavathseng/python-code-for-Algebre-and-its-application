def point_slope_form(m, x1, y1):
  """
  Returns the point-slope form of the equation of a line with slope m and
  that passes through the point (x1, y1).

  Args:
    m: The slope of the line.
    x1: The x-coordinate of the point (x1, y1).
    y1: The y-coordinate of the point (x1, y1).

  Returns:
    The point-slope form of the equation of the line.
  """

  return "y - {} = {}(x - {})".format(y1, m, x1)


if __name__ == "__main__":
  # Set the slope and point.
  m = 2
  x1 = 3
  y1 = 1

  # Print the point-slope form of the equation of the line.
  print(point_slope_form(m, x1, y1))

// This code first defines a function called point_slope_form() that takes three arguments: the slope, the x-coordinate of a point on the line, and the y-coordinate of a point on the line. The function then returns the point-slope form of the equation of the line.

// The if __name__ == "__main__" block at the end of the code is used to run the code if it is being executed as a script. In this case, the code will set the slope and point, and then print the point-slope form of the equation of the line.

// To run the code, you can save it as a Python file and then execute it from the command line. For example, if you save the code as point_slope_form.py, you can run it by typing the following command into the command line:
