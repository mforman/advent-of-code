#!/usr/bin/env python3

DIRECTIONS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def parse_move(m):
    direction = m[:1]
    distance = int("".join(m[1:]))
    x, y = DIRECTIONS[direction]
    return (x * distance, y * distance)


def get_all_points(moves):
    positions = {}
    x, y = (0, 0)
    steps = 0

    def get_range(i):
        if i < 0:
            return [-1] * abs(i)
        else:
            return [1] * i

    for lr, ud in moves:
        for i in get_range(lr):
            steps += 1
            x += i
            if (x, y) not in positions:
                positions[(x, y)] = steps
        for i in get_range(ud):
            steps += 1
            y += i
            if (x, y) not in positions:
                positions[(x, y)] = steps

    return positions


def get_distance(point):
    a, b = point
    return abs(a) + abs(b)


def solve_part1(a, b):
    pa = get_all_points(a)
    pb = get_all_points(b)

    overlap = set(pa.keys()).intersection(set(pb.keys()))

    return min(map(get_distance, overlap))


def solve_part1(a, b):
    pa = get_all_points(a)
    pb = get_all_points(b)

    overlap = set(pa.keys()).intersection(set(pb.keys()))

    return min(map(get_distance, overlap))


def solve_part2(a, b):
    pa = get_all_points(a)
    pb = get_all_points(b)

    overlap = set(pa.keys()).intersection(set(pb.keys()))

    return min(map(lambda x: pa[x] + pb[x], overlap))


assert parse_move("U8") == (0, 8)
assert parse_move("D10") == (0, -10)
assert parse_move("L5") == (-5, 0)
assert parse_move("R1") == (1, 0)

a = ["R8", "U5", "L5", "D3"]
b = ["U7", "R6", "D4", "L4"]

with open("03.txt") as f:
    lines = list(map(lambda s: s.split(","), f.readlines()))
    a = lines[0]
    b = lines[1]

moves_a = list(map(parse_move, a))
moves_b = list(map(parse_move, b))


print(f"Part 1: {solve_part1(moves_a, moves_b)}")
print(f"Part 2: {solve_part2(moves_a, moves_b)}")
