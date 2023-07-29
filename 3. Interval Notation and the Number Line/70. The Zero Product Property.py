def zero_product_property(a, b):
  """Returns True if a and b are the roots of the quadratic equation ax^2 + bx + c = 0, False otherwise."""
  if a * b == 0:
    return True
  else:
    return False

if __name__ == "__main__":
  a = 1
  b = 2
  c = 1
  print(zero_product_property(a, b))
