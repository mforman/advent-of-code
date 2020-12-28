from itertools import product, chain

MOVES = [p for p in product([-1, 0, 1], repeat=2) if p != (0, 0)]


def count_occupied_adjacent(state, pos, steps=None):
    height = len(state)
    width = len(state[0])
    longest_dimension = max(height, width)
    count = 0
    for move in MOVES:
        for step in range(1, longest_dimension):
            x = pos[0] + (move[0] * step)
            y = pos[1] + (move[1] * step)

            # x, y = map(sum, zip(pos, move))
            if (x, y) == pos or not (0 <= y < height) or not (0 <= x < width):
                break
            if state[y][x] == "#":
                count += 1
            if state[y][x] != ".":
                break
            if steps and step <= steps:
                break
    return count


def apply_rules(state, flip, step_limit=None):
    new_state = []
    moves = 0
    for y, row in enumerate(state):
        new_row = []
        for x, seat in enumerate(row):
            occupied = count_occupied_adjacent(state, (x, y), step_limit)
            if seat == "L" and occupied == 0:
                new_row.append("#")
                moves += 1
            elif seat == "#" and occupied >= flip:
                new_row.append("L")
                moves += 1
            else:
                new_row.append(seat)
        new_state.append("".join(new_row))
    return (moves, new_state)


def solve(state, flip, step_limit):
    new_state = state
    while True:
        moves, new_state = apply_rules(new_state, flip, step_limit)
        if moves == 0:
            break

    return len([i for i in chain.from_iterable(new_state) if i == "#"])


def main():
    input = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    ]

    input = [row.strip() for row in open("11.txt").readlines()]

    new_state = input
    while True:
        moves, new_state = apply_rules(new_state, 4, step_limit=1)
        if moves == 0:
            break

    part1 = solve(input, 4, 1)
    part2 = solve(input, 5, None)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
