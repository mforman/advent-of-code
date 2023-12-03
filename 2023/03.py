import aocd

import argparse
import logging
import itertools
import math
from collections import defaultdict
from dataclasses import dataclass
from typing_extensions import Iterator

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

if args.debug:
    log_level = logging.DEBUG
else:
    log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(message)s")

@dataclass
class Number:
    buffer:str|None = None
    row:int|None = None
    start:int|None = None
    end:int|None = None

    def num(self) -> int|None:
        if not self.buffer:
            return None
        return int(''.join(self.buffer))

    def append(self, value:str) -> None:
        if not self.buffer:
            self.buffer = value
        else:
            self.buffer += value

def GetBounds(grid:list[str]) -> tuple[int, int]:
    return (len(grid), len(grid[0]))

def FindNumbers(input:list[str]) -> Iterator[Number]:
    num_rows, num_cols = GetBounds(input)
    logging.debug("Input grid has %s rows and %s columns", num_rows, num_cols)

    num = Number()
    for r in range(num_rows):
        for c in range(num_cols):
            elem = input[r][c]
            # if it's a digit, add it to the buffer
            if elem.isnumeric():
                if not num.start:
                    num.row = r
                    num.start = c
                num.append(elem)
                num.end = c
            # if it's not a digit or the end of the line,
            # flush the buffer
            if ((not elem.isnumeric()) or c == num_cols - 1) and num.buffer:
                logging.debug("Found %s", num)
                yield num
                num = Number()

def IsPart(grid:list[str], b:Number) -> None | tuple[str, tuple[int, int]]:
    logging.debug("Checking %s", b)
    num_rows, num_cols = GetBounds(grid)

    rows = range(b.row - 1, b.row + 2)
    cols = range(b.start - 1, b.end + 2)

    points = list(itertools.product(rows, cols))
    logging.debug("Will check %s", points)

    for r,c in points:
        if not (0 <= r < num_rows and 0 <= c < num_cols):
            logging.debug("(%s,%s) is ot of bounds",r,c)
            continue #out of bounds

        elem = grid[r][c]
        logging.debug("Found %s at (%s,%s)", elem, r, c)
        if elem == "." or elem.isnumeric():
            continue
        else:
            logging.debug("%s on row %s is a part because %s is at (%s,%s)", b.num(), b.row, elem, r, c)
            return (elem, (r,c))
    logging.debug("%s on row %s is not a part", b.num(), b.row)
    return None

sample = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip().splitlines()

def Part1(grid) -> int:
    nums = FindNumbers(grid)
    parts = [n.num() for n in nums if IsPart(grid, n)]
    return sum(parts)

assert Part1(sample) == 4361

def Part2(grid) -> int:
    d = defaultdict(list[int])
    nums = FindNumbers(grid)
    for n in nums:
        part = IsPart(grid, n)
        if not part:
            continue
        elem, point = part
        if elem != "*":
            continue
        d[point].append(n.num())

    gears = {k: v for k,v in d.items() if len(v) == 2}
    logging.debug("\n-------------------\nGears\n%s", gears)

    return sum([math.prod(v) for v in gears.values()])

assert Part2(sample) == 467835

input:list[str] = aocd.get_data(day=3, year=2023).splitlines()
print(f"Part 1 {Part1(input)}")
print(f"Part 2 {Part2(input)}")
