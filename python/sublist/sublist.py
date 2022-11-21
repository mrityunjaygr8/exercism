"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

def is_present(list_one, list_two):
    len_one = len(list_one)
    len_two = len(list_two)
    if set(list_one).issuperset(set(list_two)):
        for x in range(len_one - len_two + 1):
            if list_one[x:x+len_two] == list_two:
                print(list_one[x:x+len_two], list_two)
                return True

    return False


def sublist(list_one, list_two):
    len_one = len(list_one)
    len_two = len(list_two)
    if len_one == len_two and list_one == list_two:
        return EQUAL

    present = False

    if len_two < len_one:
        if len_two == 0:
            return SUPERLIST
    

        present = is_present(list_one, list_two)

        if present:
            return SUPERLIST
        else:
            return UNEQUAL


    if len_one < len_two:
        if len_one == 0:
            return SUBLIST

        present = is_present(list_two, list_one)

        if present:
            return SUBLIST
        else:
            return UNEQUAL

    return UNEQUAL
