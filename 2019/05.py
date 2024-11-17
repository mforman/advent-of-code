#!/usr/bin/env python3


def ProcessIntcode(nums, arg):
    i = 0
    output = []
    while nums[i] != 99:
        args = {
            1: nums[i + 1] if int((nums[i] % 1000) / 100) else nums[nums[i + 1]],
            2: nums[i + 2]
            if int((nums[i] % 10000) / 1000) or nums[i] % 100 == 4
            else nums[nums[i + 2]],
        }
        code = nums[i] % 100
        target, result, i = {
            1: (nums[i + 3], args[1] + args[2], i + 4),
            2: (nums[i + 3], args[1] * args[2], i + 4),
            3: (nums[i + 1], arg, i + 2),
            4: (0, nums[0], i + 2),
            5: (0, nums[0], args[2] if args[1] else i + 3),
            6: (0, nums[0], args[2] if not args[1] else i + 3),
            7: (nums[i + 3], 1 if args[1] < args[2] else 0, i + 4),
            8: (nums[i + 3], 1 if args[1] == args[2] else 0, i + 4),
        }[code]
        nums[target] = result
        if code == 4:
            output.append(args[1])
    return output


with open("05.txt") as f:
    input = list(map(int, f.read().split(",")))

print(f"Part 1: {ProcessIntcode(input, 1)}")

with open("05.txt") as f:
    input = list(map(int, f.read().split(",")))
print(f"Part 2: {ProcessIntcode(input, 5)}")
