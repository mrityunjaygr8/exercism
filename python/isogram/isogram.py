from collections import Counter

def is_isogram(string: str):
    string = string.replace(" ", "")
    string = string.replace("-", "")
    string = string.lower()

    c = Counter(string)

    return len(c.keys()) == sum(c.values())
