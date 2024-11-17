#!/usr/bin/env python3

from itertools import permutations


def ProcessIntcode(nums):
    i = 0
    while True:
        code = nums[i]
        if code == 99:
            return
        elif code == 1:
            f = lambda a, b: a + b
        elif code == 2:
            f = lambda a, b: a * b
        else:
            raise ValueError

        a = nums[i + 1]
        b = nums[i + 2]
        c = nums[i + 3]
        nums[c] = f(nums[a], nums[b])
        i += 4


def SolvePart1(nums, n=12, v=2):
    nums[1] = n
    nums[2] = v
    try:
        ProcessIntcode(nums)
        return nums[0]
    except:
        return None


def SolvePart2(nums):
    target = 19690720
    for n, v in permutations(range(100), 2):
        test = nums.copy()
        current = SolvePart1(test, n, v)
        if current == target:
            return (100 * n) + v


sample = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

# ProcessIntcode(sample)
# print(sample)

with open("02.txt") as f:
    input = list(map(int, f.read().split(",")))

input1 = input.copy()
print(f"Part 1: {SolvePart1(input1)}")

input2 = input.copy()
print(f"Part 2: {SolvePart2(input2)}")
