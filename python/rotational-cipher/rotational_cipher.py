from string import ascii_lowercase, ascii_uppercase

LOWER = list(ascii_lowercase)
UPPER = list(ascii_uppercase)


def rotate(text, key):
    text = list(text)


    for x in range(len(text)):
        if text[x] not in UPPER and text[x] not in LOWER:
            continue


        if text[x].isupper():
            text[x] = UPPER[(UPPER.index(text[x]) + key) % len(UPPER)]
        else:
            text[x] = LOWER[(LOWER.index(text[x]) + key) % len(LOWER)]

    return "".join(text)
