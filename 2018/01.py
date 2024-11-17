# Day 1 - Calibrate Device

def convertInputToNumber(s):
    sign = s[:1]
    num = int(s[1:])   

    if sign == '-':
        num = num * -1

    return num

def solvePart1(items):
    frequency = 0

    for item in items:
        frequency += item
    
    return frequency

def solvePart2(items):
    frequency = 0
    seen = set([frequency])

    while True:
        for item in items:
            frequency += item
            if frequency in seen:
                return frequency
            seen.add(frequency)

# items = [1,-2,3,1]
with open('01.txt', 'r') as f:
    items = [convertInputToNumber(s) for s in f.read().splitlines()]


print ('Part 1: {0}'.format(solvePart1(items)))

print ('Part 2: {0}'.format(solvePart2(items)))
