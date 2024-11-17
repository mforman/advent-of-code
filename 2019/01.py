#!/usr/bin/env python3


def GetRequiredFuel(m):
    return (m // 3) - 2


def GetRequiredFuelRec(m):
    fuel = GetRequiredFuel(m)
    if fuel <= 0:
        return 0
    else:
        return fuel + GetRequiredFuelRec(fuel)


def SolvePart1():
    input = (int(row) for row in open("01.txt"))
    result = sum(map(GetRequiredFuel, input))

    return result


def SolvePart2():
    input = (int(row) for row in open("01.txt"))
    result = sum(map(GetRequiredFuelRec, input))

    return result


print(f"Part 1: {SolvePart1()}")
print(f"Part 2: {SolvePart2()}")
