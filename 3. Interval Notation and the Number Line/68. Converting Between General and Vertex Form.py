def general_form(a, b, c):
  """Returns the equation of a quadratic function in general form."""
  return f"f(x) = {a}x^2 + {b}x + {c}"

def vertex_form(a, b, c):
  """Returns the equation of a quadratic function in vertex form."""
  vertex = (-b / (2 * a), (4 * a * c - b^2) / (4 * a))
  return f"f(x) = {a}(x - {vertex[0]})^2 + {vertex[1]}"

def convert_to_vertex_form(equation):
  """Converts a quadratic function from general form to vertex form."""
  a, b, c = equation.split(" ")[:3]
  vertex = (-b / (2 * a), (4 * a * c - b^2) / (4 * a))
  return f"f(x) = {a}(x - {vertex[0]})^2 + {vertex[1]}"

def convert_to_general_form(equation):
  """Converts a quadratic function from vertex form to general form."""
  a, b, c = equation.split(" ")[:3]
  vertex = (-b / (2 * a), (4 * a * c - b^2) / (4 * a))
  return f"f(x) = {a}x^2 + {b}x + {c}"

if __name__ == "__main__":
  a = 2
  b = 3
  c = 1
  print(general_form(a, b, c))
  print(vertex_form(a, b, c))
  print(convert_to_vertex_form(general_form(a, b, c)))
  print(convert_to_general_form(vertex_form(a, b, c)))
