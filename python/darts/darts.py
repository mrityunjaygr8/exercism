OUTER = 10
MIDDLE = 5
INNER = 1

def in_inner(x, y):
    if -INNER <= x <= INNER and -OUTER <= y <= OUTER:
        return True

    return False


def score(x, y):
    if x ** 2 + y ** 2 <= INNER ** 2:
        return 10
    if x ** 2 + y ** 2 <= MIDDLE ** 2:
        return 5
    if x ** 2 + y ** 2 <= OUTER ** 2:
        return 1
    return 0
