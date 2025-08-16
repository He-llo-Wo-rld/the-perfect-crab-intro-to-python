def to_alternating_case(string: str) -> str:
    """
    Steps:
    1. Check Type
    2.Inverting
    """
    if not isinstance(string, str):
        raise TypeError(f"Invalid type {type(string).__name__}, must be str")
    return "".join(s.lower() if s == s.upper() else s.upper() for s in string)


# Write a function that always returns 5

# Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/

# Good luck :


def unusual_five():
    return len("hello")


# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# Happy Coding!


def square_digits(num: int) -> int:
    if not isinstance(num, int):
        raise TypeError(f"Invalid type {type(num).__name__}, must be int")
    return int("".join(str(int(n) ** 2) for n in str(num)))


# Terminal game move function
# In this game, the hero moves from left to right. The player rolls the die and moves the number of spaces indicated by the die two times.

# Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.


def move(*args: int) -> int:
    """
    Steps:
    1.Check types
    2.Base + Move * 2
    """
    if not all(isinstance(arg, int) for arg in args):
        raise TypeError("Invalid type must be int")
    return args[0] + args[1] * 2


# Given an integral number, determine if it's a square number:

# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

# The tests will always use some integral number, so don't worry about that in dynamic typed languages.


def is_square(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError(f"Invalid type {type(n).__name__}")
    return False if n < 0 or int(n**0.5) ** 2 != n else True




# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.


def high_and_low(numbers):
    nums = [int(n) for n in numbers.split()]
    high = nums[0]
    low = nums[0]
    for n in nums:
        if n > high:
            high = n
        if n < low:
            low = n
    return f"{high} {low}"
