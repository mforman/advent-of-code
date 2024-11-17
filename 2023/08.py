import aocd

import argparse
import logging
import re

from aocd.models import count

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

if args.debug:
    log_level = logging.DEBUG
else:
    log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(message)s")


def ParseInput(input: list[str]) -> tuple[str, dict[str, tuple[str, str]]]:
    instruction = input[0]

    map_re = re.compile(r'(\w{3})')
    d = {k:tuple(v) for k,*v in [map_re.findall(x) for x in input[1:] if x]}
    return (instruction, d)

def GetNextMove(mapping:dict[str, tuple[str, str]], step:str, current:str) -> str:
    l, r = mapping[current]
    if step == 'L':
        return l
    else:
        return r

def Part1(input: list[str]) -> int:
    steps, mapping = ParseInput(input)

    current = 'AAA'
    pos = 0
    count = 0
    while True:
        step = steps[pos]
        current = GetNextMove(mapping, step, current)
        count += 1

        if current[-1] == "Z":
            return count

        pos += 1
        if pos == len(steps):
            pos = 0


sample = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip().splitlines()

sample2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip().splitlines()

assert Part1(sample) == 2
assert Part1(sample2) == 6


def Part2(input: list[str]) -> int: 
    steps, mapping = ParseInput(input)

    current = [k for k in mapping.keys() if k[-1] == "A"]
    pos = 0
    count = 0
    logging.debug("Step %s: %s", count, current)
    while True:
        step = steps[pos]
        current = [GetNextMove(mapping, step, c) for c in current]
        count += 1
        
        logging.debug("Step %s: Move %s to %s", count, step, current)
        if all([c[-1]=="Z" for c in current]):
            return count

        pos += 1
        if pos == len(steps):
            pos = 0
       

sample3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip().splitlines()

assert Part2(sample3) == 6

input = aocd.get_data(day=8, year=2023).splitlines()

part1 = Part1(input) 
part2 = Part2(input)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

