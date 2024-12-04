import aocd
from typing import List

def parse(input:str) -> List[List[int]]:
    return [[int(val) for val in line.split(" ") ] for line in input.splitlines()]

def is_safe(report: List[int], allowed:int = 0) -> bool:
    items = zip(report, report[1:])
    decreasing = report[0] > report[1]
    failures = 0
    for a,b in items:
        if failures > allowed:
            return False
        
        if decreasing and a <= b:
            failures = failures + 1
            continue

        if (not decreasing) and a >= b:
            failures = failures + 1
            continue

        if 1 < abs(a-b) > 3:
            failures = failures + 1
            continue

    return failures <= allowed

def part1(reports: List[List[int]]) -> int:
    return sum([is_safe(item) for item in reports])

def part2(reports: List[List[int]]) -> int:
    return sum([is_safe(item, 1) for item in reports])

input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

input:str = aocd.get_data(day=2, year=2024)

items = parse(input)
print(part1(items))
print(part2(items))
