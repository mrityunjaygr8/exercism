def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while number != 1:
        steps += 1
        is_even = number % 2 == 0
        if is_even:
            number = int(number / 2)
        else:
            number = 3 * number + 1
        
    return steps
