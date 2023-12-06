import aocd

import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

if args.debug:
    log_level = logging.DEBUG
else:
    log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(message)s")


def ParseInput(input:list[str]) -> tuple[list[list[int]], dict[str, list[tuple[int, int, int]]]]:
    seeds = [[int(x)] for x in input[0][7:].split(" ")]

    mappings = {}
    name = ""
    current = [] 
    for line in input:
        match line.split(" "):
            case[d, s, r]:
                d = int(d)
                s = int(s)
                r = int(r)
                current.append((int(s), int(d), int(r)))
            case[label, "map:"]:
                if current:
                    mappings[name] = current
                name = label
                current = []
            case _:
                continue
    if current:
        mappings[name] = current

    return (seeds, mappings)


def GetMatch(item:int, lookup:list[tuple[int, int, int]]) -> int:
    for s, d, r in lookup:
        if item in range(s,s+r+1):
            return item - s + d
    return item

assert GetMatch(79, [(98, 50, 2),(50, 52, 48)]) == 81
assert GetMatch(14, [(98, 50, 2),(50, 52, 48)]) == 14
assert GetMatch(55, [(98, 50, 2),(50, 52, 48)]) == 57
assert GetMatch(13, [(98, 50, 2),(50, 52, 48)]) == 13

def GetLocations(seeds:list[list[int]], mappings:dict[str, list[tuple[int, int, int]]]) -> list[list[int]]:
    seq = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location'
    ]
    for seed in seeds:
        for k in seq:
            lookup = mappings[k]
            seed.append(GetMatch(seed[-1], lookup))
            logging.debug("Input: %s\nMap: %s\n%s\nFound: %s\n", seed[-2], k, lookup, seed[-1])
    return seeds

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def Part1(input:list[str]) -> int:
    seeds, mappings = ParseInput(input)
    locations = [x[-1] for x in GetLocations(seeds, mappings)]
    return min(locations)

sample = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".strip().split("\n")

assert Part1(sample) == 35

input:list[str] = aocd.get_data(day=5, year=2023).splitlines()

part1 = Part1(input)
print(f"Part 1: {part1}")
