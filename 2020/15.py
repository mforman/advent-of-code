from collections import defaultdict


def solve(input, turns):
    nums = defaultdict(list)
    last = None

    for i, val in enumerate(input):
        nums[val].append(i + 1)
        last = val

    for i in (i for i in range(1, turns + 1) if i > len(input)):
        if len(nums[last]) <= 1:
            last = 0
        else:
            a, b = nums[last][-2:]
            last = b - a
        nums[last].append(i)

    return last


def main():
    # input = [0, 3, 6]
    input = [1, 20, 8, 12, 0, 14]

    print(f"Part 1: {solve(input, 2020)}")
    # print(f"Part 2: {solve(input, 30000000)}")


if __name__ == "__main__":
    # execute only if run as a script
    main()