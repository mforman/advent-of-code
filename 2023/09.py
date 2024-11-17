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

def GetDiffs(lst: list[int]) -> list[int]:
    return [lst[i] - lst[i-1] for i in range(1,len(lst))]

assert GetDiffs([0, 3, 6, 9, 12, 15]) == [3,3,3,3,3]

def GetNextValue(lst:list[int], at_head:bool=False) -> int:
    vals = [lst]
    current = lst
    
    logging.debug("Starting: %s", lst)

    while True:
        d = GetDiffs(current)
        logging.debug("Diffs: %s", d)
        vals.append(d)
        if set(d) == {0}:
            break
        current = d
    
    a=0
    b=0
    for i in range(len(vals)-1,-1,-1):
        if at_head:
            a = vals[i][0]
            next = a-b
            vals[i].insert(0,next)
            b = next
        else:
            a = vals[i][-1]
            nxt = a+b
            vals[i].append(nxt)
            b = nxt 

    logging.debug("\nWith next: %s", vals)
    if at_head:
        return vals[0][0]
    else:
        return vals[0][-1]


assert GetNextValue([0, 3, 6, 9, 12, 15]) == 18
assert GetNextValue([1, 3, 6, 10, 15, 21]) == 28
assert GetNextValue([10, 13, 16, 21, 30, 45]) == 68

def ParseInput(input:list[str]) -> list[list[int]]:
    return [[int(x) for x in line.split(" ")] for line in input]

def Part1(input:list[str]) -> int:
    lst = ParseInput(input)
    next = [GetNextValue(x) for x in lst]
    return sum(next)

def Part2(input:list[str]) -> int:
    lst = ParseInput(input)
    next = [GetNextValue(x, at_head=True) for x in lst]
    return sum(next)

sample = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().splitlines()

assert Part1(sample) == 114
assert Part2(sample) == 2


input = aocd.get_data(day=9, year=2023).splitlines()

part1 = Part1(input)
part2 = Part2(input)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
