


import string
import random

class randomdata:
  def passrandomstring(self):
     
      length_of_string = 5

      letters_and_digits = string.ascii_lowercase + string.digits
      random_string = ""

      for number in range(length_of_string):
        random_string += random.choice(letters_and_digits)

      return random_string

