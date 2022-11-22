from collections import Counter
import string

ALPHAS = [*string.ascii_lowercase]

def is_pangram(sentence: str):
    sentence = sentence.replace(".", "")
    sentence = sentence.replace(" ", "")
    sentence = sentence.lower()


    counter = Counter(sentence)
    return set(counter.keys()).issuperset(set(ALPHAS))
