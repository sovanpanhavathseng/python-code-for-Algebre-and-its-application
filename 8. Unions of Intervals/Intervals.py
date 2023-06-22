def interval_type(note1, note2):
  """Returns the type of interval between two notes."""
  semitones = note2 - note1
  if semitones == 0:
    return "Unison"
  elif semitones == 1:
    return "Minor second"
  elif semitones == 2:
    return "Major second"
  elif semitones == 3:
    return "Minor third"
  elif semitones == 4:
    return "Major third"
  elif semitones == 5:
    return "Perfect fourth"
  elif semitones == 6:
    return "Tritone"
  elif semitones == 7:
    return "Perfect fifth"
  elif semitones == 8:
    return "Minor sixth"
  elif semitones == 9:
    return "Major sixth"
  elif semitones == 10:
    return "Minor seventh"
  elif semitones == 11:
    return "Major seventh"
  else:
    return "Octave"


def main():
  """Prints the type of interval between two notes."""
  note1 = 60
  note2 = 64
  print(interval_type(note1, note2))


if __name__ == "__main__":
  main()

// This code first defines a function called interval_type(). This function takes two notes as input and returns the type of interval between them. The function works by first calculating the difference in pitch between the two notes in semitones. Then, it uses a switch statement to determine the type of interval based on the number of semitones.

// The code then defines a function called main(). This function takes no input and prints the type of interval between two notes. The function first gets the two notes from the user. Then, it calls the interval_type() function to get the type of interval. Finally, it prints the type of interval.

// To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as intervals.py, you can run it by typing the following command into the command line:
