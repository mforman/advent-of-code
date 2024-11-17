from functools import reduce

input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]

input = [row.strip() for row in open("03.txt").readlines()]

depth = len(input)
width = len(input[0])


def check_slope(move_x, move_y):
    x = 0
    y = 0
    trees = 0

    while y < depth - 1:
        x += move_x
        y += move_y
        if input[y][x % width] == "#":
            trees += 1

    return trees


print(f"Part 1: {check_slope(3,1)}")

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = reduce(lambda a, b: a * check_slope(*b), slopes, 1)
print(f"Part 2: {result}")
