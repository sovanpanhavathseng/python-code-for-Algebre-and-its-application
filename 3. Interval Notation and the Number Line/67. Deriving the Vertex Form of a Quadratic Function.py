def vertex_form(a, b, c):
  """Returns the equation of a quadratic function in vertex form."""
  vertex = (-b / (2 * a), (4 * a * c - b^2) / (4 * a))
  return f"f(x) = {a}(x - {vertex[0]})^2 + {vertex[1]}"

def derive_vertex_form(a, b, c):
  """Derives the vertex form of a quadratic function."""
  vertex = (-b / (2 * a), (4 * a * c - b^2) / (4 * a))
  equation = f"f(x) = {a}x^2 + {b}x + {c}"
  equation = equation.replace("x^2", "(x - {0})^2".format(vertex[0]))
  equation = equation.replace("x", "(x - {0}) + {1}".format(vertex[0], vertex[1]))
  return equation

if __name__ == "__main__":
  a = 2
  b = 3
  c = 1
  print(derive_vertex_form(a, b, c))
