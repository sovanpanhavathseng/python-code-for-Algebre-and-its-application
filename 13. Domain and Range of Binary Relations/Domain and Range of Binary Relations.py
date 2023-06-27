def domain(relation):
  """Returns the domain of a binary relation."""
  domain = set()
  for pair in relation:
    domain.add(pair[0])
  return domain

def range(relation):
  """Returns the range of a binary relation."""
  range = set()
  for pair in relation:
    range.add(pair[1])
  return range

if __name__ == "__main__":
  relation = {(1, 2), (2, 3), (3, 4)}
  print("The domain of the relation is:", domain(relation))
  print("The range of the relation is:", range(relation))

// This code first defines two functions, domain() and range(), which take a binary relation as input and return the domain and range of the relation, respectively. The domain() function works by looping through the pairs in the relation and adding the first element of each pair to the domain set. The range() function works by looping through the pairs in the relation and adding the second element of each pair to the range set.

// The main function then defines a binary relation and calls the domain() and range() functions to print the domain and range of the relation.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as domain_range.py, you can run it by typing the following command into the command line:
