from aocd import get_data

input = get_data(day=1, year=2022)

split_input = input.split("\n" * 2)


def processGroup(group):
    return sum([int(x) for x in group.split('\n')])


totals = [processGroup(x) for x in split_input]
totals.sort(reverse=True)


print(f"Part 1: {totals[0]}")
print(f"Part 2: {sum(totals[0:3])}")
