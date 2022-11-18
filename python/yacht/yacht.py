from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = "yatch"
ONES = "ones"
TWOS = "tows"
THREES = "thresss"
FOURS = "fours"
FIVES = "fives"
SIXES = "sizes"
FULL_HOUSE = "full"
FOUR_OF_A_KIND = "foak"
LITTLE_STRAIGHT = "lil"
BIG_STRAIGHT = "big"
CHOICE = "choice"


def score(dice, category):
    s_dice = sorted(dice)
    if category == YACHT:
        if s_dice[0] == s_dice[1] == s_dice[2] == s_dice[3] == s_dice[4]:
            return 50
        else:
            return 0
    elif category == ONES:
        c = filter(lambda x: x == 1, s_dice)
        count = 0
        for _ in c:
            count += 1
        return count

    elif category == TWOS:
        c = filter(lambda x: x == 2, s_dice)
        count = 0
        for _ in c:
            count += 1
        return count * 2
    elif category == THREES:
        c = filter(lambda x: x == 3, s_dice)
        count = 0
        for _ in c:
            count += 1
        return count * 3

    elif category == FOURS:
        c = filter(lambda x: x == 4, s_dice)
        count = 0
        for _ in c:
            count += 1
        return count * 4
    elif category == FIVES:
        c = filter(lambda x: x == 5, s_dice)
        count = 0
        for _ in c:
            count += 1
        return count * 5
    elif category == SIXES:
        c = filter(lambda x: x == 6, s_dice)
        count = 0
        for _ in c:
            count += 1
        return count * 6

    elif category == FULL_HOUSE:
        counter = Counter(s_dice)
        if len(counter) != 2:
            return 0
        for val in counter.values():
            if val not in [2, 3]:
                return 0
        return sum(s_dice)

    elif category == FOUR_OF_A_KIND:
        counter = Counter(s_dice)
        for key, val in counter.items():
            if val >= 4:
                return 4 * key
        return 0

    elif category == CHOICE:
        return sum(s_dice)

    elif category == LITTLE_STRAIGHT:
        if s_dice == [1, 2, 3, 4, 5]:
            return 30
        return 0

    elif category == BIG_STRAIGHT:
        if s_dice == [2, 3, 4, 5, 6]:
            return 30
        return 0
