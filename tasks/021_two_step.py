# Video alternative: https://vimeo.com/954334279/dd2abfbdd7#t=0
import os
import sys
from ast import arg

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lib.helpers import check_that_these_are_equal

# Here's a function:


def add_one_and_divide_by_two_with_statements(num):
    added = num + 1
    halved = added / 2
    return halved


print("add_one_and_divide_by_two_with_statements(5) is:")

print(add_one_and_divide_by_two_with_statements(5))

# You could also do this with a single expression, like this:


def add_one_and_divide_by_two_with_an_expression(num):
    return (num + 1) / 2


print("add_one_and_divide_by_two_with_an_expression(5) is:")

print(add_one_and_divide_by_two_with_an_expression(5))

# The statements just break it up a bit more. We'll see some more uses for
# statements and variables soon, but for now let's practice using them.

# @TASK: Complete these functions.

# == Exercise One ==

print("")
print("Function: divide_by_two_and_add_one")


def divide_by_two_and_add_one(num: int | float) -> int | float:
    if not isinstance(num, (int, float)):
        raise TypeError(f"Invalid argument type {type(num).__name__}")
    return num / 2 + 1


check_that_these_are_equal(divide_by_two_and_add_one(6), 4.0)

# == Exercise Two ==

print("")
print("Function: multiply_by_forty_and_add_sixty")


def multiply_by_forty_and_add_sixty(num: int | float) -> int | float:
    if not isinstance(num, (int, float)):
        raise TypeError(f"Invalid argument type {type(num).__name__}")
    return num * 40 + 60


check_that_these_are_equal(multiply_by_forty_and_add_sixty(3423), 136980)

# == Exercise Three ==

print("")
print("Function: add_together_and_double")


def add_together_and_double(*args: int | float) -> int | float:
    """
    Steps:
    1. Check types
    2.sum and *
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("All arguments must be (int or float)")
    return sum(args) * 2


check_that_these_are_equal(add_together_and_double(3, 4), 14)

# When you're done, move on to 022_strings.py
