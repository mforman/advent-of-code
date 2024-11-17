from itertools import product
from collections import Counter


def move(input, dim=3):
    adjacent = (
        tuple(map(sum, zip(pos, m)))
        for pos in input
        for m in product([-1, 0, 1], repeat=dim)
        if any(m)
    )
    return {
        pos
        for pos, cnt in Counter(adjacent).items()
        if cnt == 3 or (pos in input and cnt == 2)
    }


def parse(input, dim):
    return {
        (x, y) + (0,) * (dim - 2)
        for y, row in enumerate(input)
        for x, val in enumerate(row)
        if val == "#"
    }


def cycle(cube, dim):
    for i in range(6):
        cube = move(cube, dim)
    return cube


def main():
    input = [
        ".#.",
        "..#",
        "###",
    ]

    input = [
        "#...#.#.",
        "..#.#.##",
        "..#..#..",
        ".....###",
        "...#.#.#",
        "#.#.##..",
        "#####...",
        ".#.#.##.",
    ]
    # cube3 = {
    #     (x, y, 0)
    #     for y, row in enumerate(input)
    #     for x, val in enumerate(row)
    #     if val == "#"
    # }

    # cube4 = {
    #     (x, y, 0, 0)
    #     for y, row in enumerate(input)
    #     for x, val in enumerate(row)
    #     if val == "#"
    # }

    # for i in range(6):
    #     cube3 = move(cube3, 3)
    #     cube4 = move(cube4, 4)

    cube = cycle(parse(input, 3), 3)
    print(f"Part 1: {len(cube)}")

    cube = cycle(parse(input, 4), 4)
    print(f"Part 2: {len(cube)}")


if __name__ == "__main__":
    main()
