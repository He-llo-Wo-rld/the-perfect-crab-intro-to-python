import os
import sys
from typing import Union

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lib.helpers import check_that_these_are_equal

# Video alternative: https://vimeo.com/954334235/902b0b036d#t=84

# Now you try. Here's an exercise for you:
#
# @TASK: Write a function called `add_two` that:
#
# * Takes a number as input
# * Adds two to it
# * Returns the result

# YOUR FUNCTION GOES BELOW THIS LINE


def add_two(object: Union[int, float]) -> Union[int, float]:
    if not isinstance(object, (int, float)):
        raise TypeError(f"Invalid argument type {type(object).__name__}")
    return round(object + 2, 2)


# YOUR FUNCTION GOES ABOVE THIS LINE

# @TASK: To check your work, run this in the terminal:

#   python 013_add_two.py

# This will run the test at the bottom of this file.

# If you have trouble, look back at `add_one` _very_ closely, character by
# character, to see if you can see any differences to your version. Pay
# particular attention to the `:` at the end of the first line, and the spacing
# at the start of some of the lines.

print("Function: add_two")

check_that_these_are_equal(add_two(6), 8)
