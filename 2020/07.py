input = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]

input = [
    "shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags.",
]

input = [row.strip() for row in open("07.txt").readlines()]


def parse_line(line):
    tokens = line.split()
    colour = " ".join(tokens[:2])
    bags = {}

    pos = 4
    while pos < len(tokens):
        if tokens[pos] == "no":
            break
        qty = int(tokens[pos])
        inner_colour = " ".join(tokens[pos + 1 : pos + 3])
        bags[inner_colour] = qty
        pos += 4

    return (colour, bags)


graph = dict([parse_line(line) for line in input])


def find_colour(graph, targets, result=None):
    found = set()
    if not result:
        result = set()

    for colour, bags in graph.items():
        for inner_colour in bags:
            if inner_colour in targets and colour not in result:
                found.add(colour)

    if not found:
        return result
    else:
        return find_colour(graph, found, result | found)


def count_bags(graph, start):
    if not start in graph:
        return 0
    bag = graph[start]
    total = 0
    for colour, qty in bag.items():
        total += qty + (qty * count_bags(graph, colour))
    return total


part1 = find_colour(graph, ["shiny gold"])
print(f"Part 1: {len(part1)}")

part2 = count_bags(graph, "shiny gold")
print(f"Part 2: {part2}")
