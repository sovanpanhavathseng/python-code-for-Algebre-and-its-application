def divide_complex_numbers(a, b):
  """Divides two complex numbers.

  Args:
    a: The first complex number.
    b: The second complex number.

  Returns:
    The result of dividing a by b.
  """

  conjugate = complex(b.real, -b.imag)

  return (a * conjugate) / (b * conjugate)


if __name__ == "__main__":
  a = complex(2, 3)
  b = complex(1, 1)

  result = divide_complex_numbers(a, b)

  print(result)
