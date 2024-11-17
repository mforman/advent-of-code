from collections import defaultdict
from itertools import chain, filterfalse


def parse(input):
    def parse_nums(line):
        return [int(x) for x in line.split(",")]

    def parse_rule(line):
        l, r = line.split(": ")
        ranges = r.split(" or ")

        # The set would be better
        vals = set()
        for a, b in [tuple(map(int, x.split("-"))) for x in ranges]:
            vals.update(list(range(a, b + 1)))

        bounds = [y for y in [tuple(map(int, x.split("-"))) for x in ranges]]
        return (l, bounds)

    r, m, n = input.split("\n\n")
    rules = {k: v for k, v in [parse_rule(line) for line in r.split("\n")]}
    mine = parse_nums(m.split("\n")[-1])
    nearby = [parse_nums(line) for line in n.split("\n")[1:]]

    return rules, mine, nearby


def is_valid(n, rules):
    for a, b in rules:
        if a <= n <= b:
            return True
    return False


def solve1(rules, nearby):
    all_rules = list(chain.from_iterable(rules.values()))
    all_nearby = list(chain.from_iterable(nearby))

    return sum(filterfalse(lambda n: is_valid(n, all_rules), all_nearby))


def solve2(rules, nearby, mine):
    def all_valid(t, rules):
        return all((is_valid(n, rules) for n in t))

    all_rules = list(chain.from_iterable(rules.values()))
    valid_input = list(filter(lambda x: all_valid(x, all_rules), nearby))

    positions = list(zip(*valid_input))

    candidates = defaultdict(list)

    for k, v in rules.items():
        for i, p in enumerate(positions):
            if all_valid(p, v):
                candidates[k].append(i)

    while True:
        for k in candidates:
            if len(candidates[k]) == 1:
                for ik, iv in candidates.items():
                    if k == ik:
                        continue
                    if candidates[k][0] in iv:
                        iv.remove(candidates[k][0])

        for k in candidates:
            if len(candidates[k]) > 1:
                v = candidates[k]
                ac = list(chain.from_iterable(candidates.values()))
                for i in v:
                    if ac.count(i) == 1:
                        candidates[k] = [i]
                        break
        if max([len(v) for v in candidates.values()]) == 1:
            break

    result = 1
    for k, v in candidates.items():
        if k.startswith("departure"):
            result *= mine[v[0]]
    return result


def main():
    input = "\n".join(
        [
            "class: 0-1 or 4-19",
            "row: 0-5 or 8-19",
            "seat: 0-13 or 16-19",
            "",
            "your ticket:",
            "11,12,13",
            "",
            "nearby tickets:",
            "3,9,18",
            "15,1,5",
            "5,14,9",
        ]
    )

    # input = "\n".join(
    #     [
    #         "class: 1-3 or 5-7",
    #         "row: 6-11 or 33-44",
    #         "seat: 13-40 or 45-50",
    #         "",
    #         "your ticket:",
    #         "7,1,14",
    #         "",
    #         "nearby tickets:",
    #         "7,3,47",
    #         "40,4,50",
    #         "55,2,20",
    #         "38,6,12",
    #     ]
    # )

    input = "\n".join([row.strip() for row in open("16.txt").readlines()])

    rules, mine, nearby = parse(input)
    p1 = solve1(rules, nearby)
    print(f"Part 1: {p1}")
    p2 = solve2(rules, nearby, mine)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    # execute only if run as a script
    main()