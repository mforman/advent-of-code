from typing import Optional

import aocd

def parseLine(line: str) -> int:
    first: Optional[str] = None
    last: Optional[str] = None
    for c in line:
        if c.isnumeric():
            last = c
            if not first:
                first = c
    assert first is not None
    assert last is not None
    return int(first+last)

assert(parseLine('1abc2')==12)
assert(parseLine('pqr3stu8vwx')==38)

def part1(input:str) -> int: 
    return sum([parseLine(x) for x in input.split("\n")])

sample1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

assert(part1(sample1)==142)


nums = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}.items()


def replaceTokens(line: str) -> str:
    for k,v in nums:
        line = line.replace(k,v)
    return line

assert(replaceTokens("eightwothree")=="e8t2ot3e")

def part2(input:str) -> int: 
    return sum([parseLine(replaceTokens(x)) for x in input.split("\n")])

sample2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

assert(part2(sample2)==281)

input:str = aocd.get_data(day=1, year=2023)
print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")

