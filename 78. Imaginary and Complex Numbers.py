import math


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


def multiply_complex_numbers(a, b):
  """Multiplies two complex numbers."""
  real_part = a.real * b.real - a.imag * b.imag
  imaginary_part = a.real * b.imag + a.imag * b.real
  return complex(real_part, imaginary_part)


def divide_complex_numbers(a, b):
  """Divides two complex numbers."""
  denominator = b.real ** 2 + b.imag ** 2
  real_part = (a.real * b.real + a.imag * b.imag) / denominator
  imaginary_part = (a.imag * b.real - a.real * b.imag) / denominator
  return complex(real_part, imaginary_part)


def main():
  """Prints the results of adding, subtracting, multiplying, and dividing complex numbers."""
  a = complex(2, 3)
  b = complex(5, 6)
  print("Adding:", add_complex_numbers(a, b))
  print("Subtracting:", subtract_complex_numbers(a, b))
  print("Multiplying:", multiply_complex_numbers(a, b))
  print("Dividing:", divide_complex_numbers(a, b))


if __name__ == "__main__":
  main()
