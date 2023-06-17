def relative_complement(set_a, set_b):
  """
  Returns the relative complement of set_a in set_b.

  Args:
    set_a: The first set.
    set_b: The second set.

  Returns:
    The relative complement of set_a in set_b.
  """

  relative_complement = set()
  for element in set_b:
    if element not in set_a:
      relative_complement.add(element)

  return relative_complement


if __name__ == "__main__":
  set_a = {1, 2, 3, 4, 5}
  set_b = {1, 2, 3, 4, 5, 6, 7, 8, 9}

  relative_complement = relative_complement(set_a, set_b)

  print(relative_complement)

// This code first defines a function called relative_complement(). This function takes two sets as input, and returns the relative complement of the first set in the second set.

// The function works by first creating a new set called relative_complement. This set will store the elements that are in the second set but not in the first set.

// The function then iterates over the elements of the second set. For each element, the function checks if the element is also in the first set. If it is not, then the element is added to the relative_complement set.

// Finally, the function returns the relative_complement set.

// The main function of the code then defines two sets, set_a and set_b. These sets are used to test the relative_complement() function.

// The relative_complement() function is then called, and the result is printed to the console.

// I hope this helps! Let me know if you have any other questions.
