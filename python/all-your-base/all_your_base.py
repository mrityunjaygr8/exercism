def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    numbers = []
    len_digits = len(digits)
    for pow in range(len_digits):
        if not (0 <= digits[pow] < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
        numbers.append((input_base ** (len_digits - pow - 1)) * digits[pow])
    number = sum(numbers)
    if number == 0:
        return [0]
    base = []
    while number != 0:
        base.append(number % output_base)
        number = number // output_base

    return base[::-1]
