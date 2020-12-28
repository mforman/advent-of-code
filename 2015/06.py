from collections import defaultdict


def parse(line):
    tokens = line.split(" ")
    offset = 0
    if tokens[0] == "turn":
        cmd = tokens[1]
        offset = 1
    else:
        cmd = tokens[0]

    start = tuple([int(t) for t in tokens[1 + offset].split(",")])
    end = tuple([int(t) for t in tokens[3 + offset].split(",")])

    return (cmd, start, end)


GRID_SIZE = 1000


def light_range(s, e):
    ax, ay = s
    bx, by = e
    result = set()
    start = (ay * GRID_SIZE) + ax
    for y in range(by - ay + 1):
        for x in range(bx - ax + 1):
            result.add(start + (y * GRID_SIZE) + x)
    return result


def apply(lights, cmd, start, end):
    r = light_range(start, end)
    if cmd == "on":
        lights |= r
    elif cmd == "off":
        lights -= r
    elif cmd == "toggle":
        on = lights & r
        off = r - lights
        lights -= on
        lights |= off


def apply2(lights, cmd, start, end):
    r = light_range(start, end)
    if cmd == "on":
        for x in r:
            lights[x] += 1
    elif cmd == "off":
        for x in (x for x in r if lights[x] > 0):
            lights[x] -= 1
    elif cmd == "toggle":
        for x in r:
            lights[x] += 2


input = ["turn on 499,499 through 500,500"]
input = list((row.strip() for row in open("06.txt").readlines()))

input = [parse(i) for i in input]

lights = set()
for x in input:
    apply(lights, *x)

print(f"Part 1: {len(lights)}")

fancy_lights = defaultdict(int)
for x in input:
    apply2(fancy_lights, *x)

print(f"Part 2: {sum(fancy_lights.values())}")