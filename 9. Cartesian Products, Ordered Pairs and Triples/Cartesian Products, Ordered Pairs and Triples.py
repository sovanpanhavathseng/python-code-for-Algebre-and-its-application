def cartesian_product(set_a, set_b):
  """
  Returns the Cartesian product of two sets.

  Args:
    set_a: The first set.
    set_b: The second set.

  Returns:
    A list of all ordered pairs (x, y) such that x belongs to set_a and y belongs to set_b.
  """

  cartesian_product = []
  for x in set_a:
    for y in set_b:
      cartesian_product.append((x, y))
  return cartesian_product

def ordered_pair(x, y):
  """
  Returns an ordered pair.

  Args:
    x: The first element of the ordered pair.
    y: The second element of the ordered pair.

  Returns:
    An ordered pair (x, y).
  """

  return (x, y)

def triple(x, y, z):
  """
  Returns a triple.

  Args:
    x: The first element of the triple.
    y: The second element of the triple.
    z: The third element of the triple.

  Returns:
    A triple (x, y, z).
  """

  return (x, y, z)

if __name__ == "__main__":
  set_a = {1, 2}
  set_b = {3, 4, 5}
  print(cartesian_product(set_a, set_b))
  print(ordered_pair(1, 3))
  print(triple(1, 3, 5))

// This code first defines three functions: cartesian_product, ordered_pair, and triple. The cartesian_product function takes two sets as input and returns a list of all ordered pairs of elements from the two sets. The ordered_pair function takes two elements as input and returns an ordered pair. The triple function takes three elements as input and returns a triple.

// The main function then creates two sets, set_a and set_b, and uses the cartesian_product function to calculate the Cartesian product of the two sets. The ordered_pair and triple functions are then used to print out some examples of ordered pairs and triples.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as cartesian_products.py, you can run it by typing the following command into the command line:
