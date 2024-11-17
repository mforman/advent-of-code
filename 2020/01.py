from itertools import combinations
from functools import reduce

# input = [1721, 979, 366, 299, 675, 1456]
input = list((int(row) for row in open("01.txt")))


def solve(input, count, value):
    for i in [i for i in combinations(input, count) if sum(i) == value]:
        return reduce(lambda x, y: x * y, i)


print(f"Part 1: {solve(input, 2, 2020)}")
print(f"Part 2: {solve(input, 3, 2020)}")

