PERFECT = "perfect"
ABUNDANT = "abundant"
DEFICIENT = "deficient"


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = [x + 1 for x in range(number // 2) if number % (x + 1) == 0]
    sum_fact = sum(factors)

    if sum_fact < number:
        return DEFICIENT

    if number < sum_fact:
        return ABUNDANT
        
    return PERFECT
