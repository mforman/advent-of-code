from collections import defaultdict

input = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4,
]

input = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]

input = [int(row) for row in open("10.txt")]

input.append(0)
input = list(sorted(input))
input.append(input[-1] + 3)


def solve_part1(items):
    diffs = defaultdict(int)
    for i, val in enumerate(items):
        if i == 0:
            continue
        diff = val - items[i - 1]
        diffs[diff] += 1
    return diffs[1] * diffs[3]


# https://www.reddit.com/r/adventofcode/comments/kacdbl/2020_day_10c_part_2_no_clue_how_to_begin/
def solve_part2(items):
    paths = defaultdict(int, {items[0]: 1})
    for i in items:
        for k in (i + j for j in range(1, 4) if (i + j) in items):
            paths[k] += paths[i]

    return paths[items[-1]]


print(f"Part 1: {solve_part1(input)}")
print(f"Part 2: {solve_part2(input)}")
