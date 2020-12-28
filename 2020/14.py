from itertools import product


def parse(line):
    left, right = line.split(" = ")
    if left == "mask":
        return (right, None)
    else:
        pos = int(left[4:-1])
        val = int(right)
        return (None, (pos, val))


def solve1(input):
    mask = None
    mem = {}

    def apply_mask(value):
        b = "{0:b}".format(value).zfill(36)[::-1]
        for i, c in enumerate(b):
            m = mask[i]
            p = pow(2, i)
            if m == "X":
                continue
            elif m == "0" and value & p:
                value -= p
            elif m == "1":
                value = value | p
        return value

    for m, addr in (parse(line) for line in input):
        if m:
            mask = m[::-1]
        else:
            a, v = addr
            mem[a] = apply_mask(v)
    return sum(mem.values())


def solve2(input):
    def get_addresses(floated):
        if "X" in floated:
            for r in ("0", "1"):
                yield from get_addresses(floated.replace("X", r, 1))
        else:
            yield int(floated, 2)

    mask = None
    mem = {}
    for m, addr in (parse(line) for line in input):
        if m:
            mask = m
        else:
            a, v = addr
            a = "{:036b}".format(int(a))
            v = int(v)

            masked = ""
            for pm, pa in zip(mask, a):
                if pm == "0":
                    masked += pa
                else:
                    masked += pm

            # masked = apply_mask(a)
            addresses = get_addresses(masked)
            for a in addresses:
                mem[a] = v
    return sum(mem.values())


def main():
    input = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]

    input = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1",
    ]

    input = [row.strip() for row in open("14.txt").readlines()]

    print(f"Part 1: {solve1(input)}")
    print(f"Part 2: {solve2(input)}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
