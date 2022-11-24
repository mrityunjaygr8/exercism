COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,

}
def value(colors):
    # bands = colors.split("-")
    sum = COLORS[colors[0]] * 10
    sum += COLORS[colors[1]]
    return sum
    # return int("".join(list([COLORS[bands[0]], COLORS[bands[1]]])))
