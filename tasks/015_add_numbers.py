import os
import sys
from typing import Union

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lib.helpers import check_that_these_are_equal

# Video alternative: https://vimeo.com/954334235/902b0b036d#t=444

# @TASK: Now you try. Here's an exercise for you:
#
# Write a function called `add_numbers` that:
#
# * Takes two numbers as input
# * Adds them together
# * Returns the result

# YOUR FUNCTION GOES BELOW THIS LINE


# def add_numbers(*args: Union[int, float]) -> Union[int, float]:
#   for arg in args:
#       if not isinstance(arg, (int, float)):
#           raise TypeError(f"Invalid argument type {type(arg).__name__}")
#   return sum(args)

def add_numbers(*args: Union[int, float]) -> Union[int, float]:
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("All arguments must be numbers (int or float)")
    return sum(args)

# YOUR FUNCTION GOES ABOVE THIS LINE

# @TASK: Check your work by running:

#   python 015_add_numbers.py

# Below is a test for your function.

print("add_numbers(2, 3) is:")

check_that_these_are_equal(add_numbers(2, 3), 5)

print("add_numbers(3, 5) is:")

check_that_these_are_equal(add_numbers(3, 5), 8)

# When you're done, move on to 016_operators.py
