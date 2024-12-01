import aocd
from collections import Counter
from typing import Tuple

def parseinput(input:str) -> Tuple[list, list]:
    list1 = []
    list2 = []

    for line in input.splitlines():
        items = line.split(' ')
        list1.append(int(items[0]))
        list2.append(int(items[-1]))
    return (list1, list2)

def part1(list1, list2) -> int:
    list1.sort()
    list2.sort()
    return sum([abs(a-b) for a,b in zip(list1, list2)])


def part2(list1, list2) -> int:
    c1 = Counter(list1)
    c2 = Counter(list2)

    return sum([k * v * c2[k] for k,v in c1.items()])


input = """3   4
4   3
2   5
1   3
3   9
3   3
""" 

input:str = aocd.get_data(day=1, year=2024)
list1, list2 = parseinput(input)
print(part1(list1, list2))
print(part2(list1, list2))


