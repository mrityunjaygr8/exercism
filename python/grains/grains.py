from math import pow
def square(number, sum=False):
    if (number < 1 or number > 64) and not sum:
        raise ValueError("square must be between 1 and 64")
    return int(pow(2, number - 1)) 


def total():
    return square(64 + 1, True) - 1
