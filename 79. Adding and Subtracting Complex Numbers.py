def add_complex_numbers(a, b):
  """Adds two complex numbers."""
  real_part = a.real + b.real
  imaginary_part = a.imag + b.imag
  return complex(real_part, imaginary_part)


def subtract_complex_numbers(a, b):
  """Subtracts two complex numbers."""
  real_part = a.real - b.real
  imaginary_part = a.imag - b.imag
  return complex(real_part, imaginary_part)


def main():
  """Prints the results of adding and subtracting complex numbers."""
  a = complex(2, 3)
  b = complex(5, 6)
  print("Adding:", add_complex_numbers(a, b))
  print("Subtracting:", subtract_complex_numbers(a, b))


if __name__ == "__main__":
  main()
