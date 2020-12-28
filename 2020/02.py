import re

# input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
input = (row for row in open("02.txt"))


def is_valid_part1(d):
    min = int(d["min"])
    max = int(d["max"])
    check = d["check"]
    password = d["password"]

    c = password.count(check)
    return c >= min and c <= max


def is_valid_part2(d):
    min = int(d["min"])
    max = int(d["max"])
    check = d["check"]
    password = d["password"]

    matches = 0
    for x in [min, max]:
        if password[x - 1] == check:
            matches += 1

    return matches == 1


parsed = [
    re.match(
        r"(?P<min>\d+)-(?P<max>\d+)\s(?P<check>\w):\s(?P<password>\w+)", i
    ).groupdict()
    for i in input
]


print(f"Part 1: {len(list(filter(is_valid_part1, parsed)))}")
print(f"Part 2: {len(list(filter(is_valid_part2, parsed)))}")

# 1-3 a: abcde
# min = 1
# max = 3
# check = "a"
# password = "abcde"
