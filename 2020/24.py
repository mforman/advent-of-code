from collections import Counter, defaultdict

input = [
    "sesenwnenenewseeswwswswwnenewsewsw",
    "neeenesenwnwwswnenewnwwsewnenwseswesw",
    "seswneswswsenwwnwse",
    "nwnwneseeswswnenewneswwnewseswneseene",
    "swweswneswnenwsewnwneneseenw",
    "eesenwseswswnenwswnwnwsewwnwsene",
    "sewnenenenesenwsewnenwwwse",
    "wenwwweseeeweswwwnwwe",
    "wsweesenenewnwwnwsenewsenwwsesesenwne",
    "neeswseenwwswnwswswnw",
    "nenwswwsewswnenenewsenwsenwnesesenew",
    "enewnwewneswsewnwswenweswnenwsenwsw",
    "sweneswneswneneenwnewenewwneswswnese",
    "swwesenesewenwneswnwwneseswwne",
    "enesenwswwswneneswsenwnewswseenwsese",
    "wnwnesenesenenwwnenwsewesewsesesew",
    "nenewswnwewswnenesenwnesewesw",
    "eneswnwswnwsenenwnwnwwseeswneewsenese",
    "neswnwewnwnwseenwseesewsenwsweewe",
    "wseweeenwnesenwwwswnew",
]


def parse_line(line):
    result = []
    current_move = ""
    for c in line:
        if current_move in ["n", "s"]:
            result.append(current_move + c)
            current_move = ""
        elif c in ["e", "w"]:
            result.append(c)
        else:
            current_move = c
    return result


# (q,r)
moves = {
    "e": (1, 0),
    "ne": (1, -1),
    "se": (0, 1),
    "w": (-1, 0),
    "nw": (0, -1),
    "sw": (-1, 1),
}

input = [row.strip() for row in open("24.txt").readlines()]

move_list = [parse_line(line) for line in input]
flipped = set()

for item in move_list:
    pos = (0, 0)
    for move in (moves[m] for m in item):
        pos = tuple(q + r for q, r in zip(pos, move))
    if pos in flipped:
        flipped.remove(pos)
    else:
        flipped.add(pos)

print(f"Part 1: {len(flipped)}")


def cycle(input):
    adjacent = (tuple(map(sum, zip(pos, m))) for pos in input for m in moves.values())
    return {
        pos
        for pos, cnt in Counter(adjacent).items()
        if (pos in input and cnt in (1, 2)) or (pos not in input and cnt == 2)
    }


for d in range(100):
    flipped = cycle(flipped)
    # print(f"Day {d+1}: {len(flipped)}")

print(f"Part 2: {len(flipped)}")
