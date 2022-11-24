def is_valid(isbn: str):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    digits = list()
    list_isbn = list(isbn)
    # print(digits)
    for key, val in enumerate(list_isbn):
        # print(val)
        if val == 'X':
            if key == len(list_isbn) - 1:
                digits.append(10 * (10 - key))
                continue
            else:
                return False

        if val.isdigit():
            digits.append(int(val) * (10 - key))
        else:
            return False

    print(digits, sum(digits))
    
    digit_sum = sum(digits)
    return digit_sum % 11 == 0
