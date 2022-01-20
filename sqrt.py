"""Calculates and prints the square root of a given number.
Usage: sqrt.py --n=<n>

Options:
--n=<n>    Number for which the square root should be calculated
"""

from docopt import docopt
import math

opt = docopt(__doc__)

def main(number):
  number = int(number)
  if number < 0:
        raise Exception("number should be positive")
  print(math.sqrt(number))
    

if __name__ == "__main__":
  main(opt["--n"])
