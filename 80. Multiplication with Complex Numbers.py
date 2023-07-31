def multiply_complex_numbers(a, b):
  """Multiplies two complex numbers."""
  real_part = a.real * b.real - a.imag * b.imag
  imaginary_part = a.real * b.imag + a.imag * b.real
  return complex(real_part, imaginary_part)


def main():
  """Prints the results of multiplying complex numbers."""
  a = complex(2, 3)
  b = complex(5, 6)
  print("Multiplying:", multiply_complex_numbers(a, b))


if __name__ == "__main__":
  main()
