def translate(text: str):
    words = text.split() 
    final = []
    for word in words:
        final.append(process_word(word))
    return " ".join(final)

def process_word(word: str):
    vowels = ["a", "e", "i", "o", "u", "xr", "yt"]
    for x in vowels:
        if word.startswith(x):
            return word + "ay"

    t = word.split("qu")
    if len(t) > 1:
        return t[1]+t[0]+"qu"+"ay"

    consonant_ends = word
    for x in vowels:
        s = word.split(x)
        if len(s[0]) < len(consonant_ends):
            consonant_ends = s[0]

    if consonant_ends != word:
        return word[len(consonant_ends):] + consonant_ends + "ay"

    if len(word) == 2 and word[1] == "y":
        return "y"+word[0]+"ay"

    return ""
    
