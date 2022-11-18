from math import log10, pow
def is_armstrong_number(number):
    div = 1
    digits = []

    while div < number:
        digit = (number % (div * 10)) // (div)
        digits.append(digit)
        div *= 10
    
    sum = 0
    for x in digits:
        sum += int(pow(x, log10(div)))
    return sum == number
