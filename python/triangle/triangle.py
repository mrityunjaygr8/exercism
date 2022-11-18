def equilateral(sides):
    sorted_sides = sorted(sides)
    if not check_if_triangle(sorted_sides):
        return False
    return sorted_sides[0] == sorted_sides[1] == sorted_sides[2]


def isosceles(sides):
    sorted_sides = sorted(sides)
    if not check_if_triangle(sorted_sides):
        return False
    return (sorted_sides[0] == sorted_sides[1]) or (sorted_sides[1] == sorted_sides[2]) or (sorted_sides[0] == sorted_sides[2])


def scalene(sides):
    sorted_sides = sorted(sides)
    if not check_if_triangle(sorted_sides):
        return False
    return (sorted_sides[0] != sorted_sides[1]) and (sorted_sides[1] != sorted_sides[2]) and (sorted_sides[0] != sorted_sides[2])


def check_if_triangle(sides):
    if sides[0] == 0 or sides[2] == 0 or sides[1] == 0: 
        return False
    #
    # if type(sides[0]) != int or type(sides[0]) != int or type(sides[0]) != int:
    #     return False

    if sides[0] + sides[1] < sides[2]:
        return False
    if sides[1] + sides[2] < sides[0]:
        return False
    if sides[0] + sides[2] < sides[1]:
        return False
    return True
