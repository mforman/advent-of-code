import aocd

import argparse
import logging
import math
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

if args.debug:
    log_level = logging.DEBUG
else:
    log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(message)s")

def ParseGame(input:str) -> tuple[int, list[tuple[int, str]]]:
    id, items, *_ = input.replace("Game ", "").split(":")
    id = int(id) # Convert game id to int
    items = items[1:] # remove the leading space
    items = items.replace(";", "").replace(",", "").split(" ")
    it = iter(items)
    pairs = [(int(amt), colour) for amt, colour in [*zip(it, it)]]
    return (id, pairs)

assert ParseGame("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == (1, [(3, "blue"), (4, "red"), (1, "red"), (2, "green"), (6, "blue"), (2, "green")])


def CheckGame(game:list[tuple[int, str]], limits:dict[str, int]) -> bool:
    for amt, colour in game:
        logging.debug(f"CheckGame: {amt} {colour}")
        if amt > limits[colour]:
            return False
    return True

limits = {"red": 12, "green": 13, "blue":14}

assert CheckGame([(3, "blue"), (4, "red"), (1, "red"), (2, "green"), (6, "blue"), (2, "green")], limits)
assert not CheckGame([(8, "green"), (6, "blue"), (20, "red"), (5, "blue"), (4, "red"), (13, "green"), (5, "green"), (1, "red")], limits)

def Part1(input:list[str], limits:dict[str, int]) -> int:
    all_games = [ParseGame(item) for item in input]
    checked = [(id, CheckGame(items, limits)) for id, items in all_games]
    return sum(id for id, valid in checked if valid)

sample = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")

assert Part1(sample, limits) == 8


def FindLowerBound(game:list[tuple[int, str]]) -> dict[str, int]:
    values = defaultdict(int)
    for amt, colour in game:
        if amt > values[colour]:
            values[colour] = amt
    return dict(values)


assert FindLowerBound([(3, "blue"), (4, "red"), (1, "red"), (2, "green"), (6, "blue"), (2, "green")]) == {"red":4, "green":2, "blue":6}

def Part2(input:list[str]) -> int:
    all_games = [ParseGame(item) for item in input]
    lower_bound = [FindLowerBound(items) for _, items in all_games]
    return sum([math.prod(x.values()) for x in lower_bound])

assert Part2(sample) == 2286

input:list[str] = aocd.get_data(day=2, year=2023).split("\n")

print(f"Part 1: {Part1(input, limits)}")
print(f"Part 2 {Part2(input)}")
