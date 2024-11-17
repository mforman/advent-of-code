from itertools import count


def solve_part1(start, buses):
    earliest = 0
    delay = start
    for bus in (int(b) for b in buses.split(",") if b != "x"):
        if start % bus == 0:
            return 0
        next = (start // bus) + 1
        w = (bus * next) - start
        if w < delay:
            earliest = bus
            delay = w
    return earliest * delay


def solve_part2(input):
    # https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfncyoc?utm_source=share&utm_medium=web2x&context=3
    n = 0
    buses = tuple((i, int(b)) for i, b in enumerate(input.split(",")) if b != "x")

    step = 1
    for i, b in buses:
        n = next(c for c in count(n, step) if (c + i) % b == 0)
        step *= b
    return n

    # def is_valid(v, t):
    #     return (v + t[1]) % t[0] == 0

    # buses = [(i, int(t)) for i, t in enumerate(input.split(",")) if t != "x"]
    # times, deps = zip(*buses)

    # solved = 1
    # t = buses[0][0] + buses[0][1]
    # increment = math.prod(deps[:solved])


def main():
    input = ["939", "7,13,x,x,59,x,31,19"]

    input = [row.strip() for row in open("13.txt").readlines()]

    time = int(input[0])
    buses = input[1]

    print(f"Part 1: {solve_part1(time, buses)}")
    print(f"Part 2: {solve_part2(buses)}")
    # print(solve_part2("17,x,13,19"))


if __name__ == "__main__":
    # execute only if run as a script
    main()
