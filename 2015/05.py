import string

VOWELS = set(["a", "e", "i", "o", "u"])
ILLEGAL = set(["ab", "cd", "pq", "xy"])


def is_nice(s):
    v = 0
    found_double = False
    p = None
    for i, c in enumerate(s):
        if c in VOWELS:
            v += 1
        if i > 0:
            if p == c:
                found_double = True
            if "".join([p, c]) in ILLEGAL:
                return False
        p = c
    return v >= 3 and found_double


def is_nice2(s):
    pairs = {}
    found_pair = False
    found_between = False
    p1 = None
    p2 = None
    pair = None
    for i, c in enumerate(s):
        if i > 0:
            pair = "".join([p1, c])
            if pair in pairs:
                if pairs[pair] < i - 1:
                    found_pair = True
            else:
                pairs[pair] = i
        if i > 1:
            if c == p2:
                found_between = True
        if found_pair and found_between:
            return True
        p2 = p1
        p1 = c
    return False


input = [
    "ugknbfddgicrmopn",
    "aaa",
    "jchzalrnumimnmhp",
    "haegwjzuvuyypxyu",
    "dvszwmarrgswjxmb",
]

input = [
    "qjhvhtzxzqqjkmpb",
    "xxyxx",
    "uurcxstgmygtbstg",
    "ieodomkazucvgmuy",
]

input = list((row for row in open("05.txt").readlines()))

c = len([i for i in input if is_nice(i)])
print(f"Part 1: {c}")

c2 = len([i for i in input if is_nice2(i)])
print(f"Part 2: {c2}")