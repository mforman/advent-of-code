def parse(s):
    tokens = s.split()
    return (tokens[0], int(tokens[1]))


input = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]

input = list([parse(line) for line in input])

input = [parse(row.strip()) for row in open("08.txt")]


def process(instructions):
    accumulator = 0
    pos = 0
    visited = set()

    while pos < len(instructions):
        if pos in visited:
            return (-1, accumulator)
        else:
            visited.add(pos)
        op, i = instructions[pos]
        if op == "acc":
            accumulator += i
            pos += 1
        elif op == "nop":
            pos += 1
        elif op == "jmp":
            pos += i
    return (0, accumulator)


print(f"Part 1: {process(input)[1]}")

pos = 0
val = 0
while pos < len(input):
    op, i = input[pos]
    if op == "nop":
        input[pos] = ("jmp", i)
    elif op == "jmp":
        input[pos] = ("nop", i)

    rc, val = process(input)
    if rc == 0:
        break
    if rc == -1:
        input[pos] = (op, i)
    pos += 1

print(f"Part 2: {val}")
