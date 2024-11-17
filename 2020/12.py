def parse(s):
    return (s[0], int(s[1:]))


HEADINGS = {"N": (1, 0), "S": (-1, 0), "E": (0, 1), "W": (0, -1)}
DEGREES = {0: (1, 0), 180: (-1, 0), 90: (0, 1), 270: (0, -1)}


def scale_tuple(t, s):
    return tuple(s * x for x in t)


def add_tuples(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


def move(pos, direction, instruction):
    action, amount = instruction
    if action == "L":
        return (pos, (direction - amount) % 360)
    elif action == "R":
        return (pos, (direction + amount) % 360)
    elif action == "F":
        offset = DEGREES[direction]
    else:
        offset = HEADINGS[action]

    m = scale_tuple(offset, amount)
    new_pos = add_tuples(pos, m)
    return (new_pos, direction)


def rotate(waypoint, direction):
    a, b = waypoint
    if direction == "L":
        return (b, -a)
    else:
        return (-b, a)


def move_with_waypoint(pos, waypoint, instruction):
    action, amount = instruction
    if action in ["L", "R"]:
        wp = waypoint
        for _ in range(amount // 90):
            wp = rotate(wp, action)
        return (pos, wp)
    elif action == "F":
        m = scale_tuple(waypoint, amount)
        return (add_tuples(pos, m), waypoint)
    else:
        m = scale_tuple(HEADINGS[action], amount)
        return (pos, add_tuples(waypoint, m))


def manhattan(pos):
    return sum(tuple(abs(x) for x in pos))


def main():
    input = [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11",
    ]

    input = list(map(parse, input))
    input = [parse(row.strip()) for row in open("12.txt").readlines()]

    pos = (0, 0)
    direction = 90

    for i in input:
        pos, direction = move(pos, direction, i)

    print(f"Part 1: {manhattan(pos)}")

    pos = (0, 0)
    waypoint = (1, 10)

    for i in input:
        pos, waypoint = move_with_waypoint(pos, waypoint, i)

    print(f"Part 2: {manhattan(pos)}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
