import re
from collections import Counter

# items = [
#     '#1 @ 1,3: 4x4',
#     '#2 @ 3,1: 4x4',
#     '#3 @ 5,5: 2x2'
# ]

with open('03.txt', 'r') as f:
    items = f.read().splitlines()

claims = [[*map(int, re.findall(r'-?\d+', item))] for item in items]
squares = lambda c: ((i, j) for i in range(c[1], c[1] + c[3])
                            for j in range(c[2], c[2] + c[4]))
fabric = Counter(s for c in claims for s in squares(c))

part1 = sum(1 for v in fabric.values() if v > 1)
part2 = next(c[0] for c in claims if all(fabric[s] == 1 for s in squares(c)))

print ('Part 1: {0}'.format(part1))
print ('Part 2: {0}'.format(part2))


# def getPoint(x, y):
#     return '{},{}'.format(x, y)

# class Claim:
#     def __init__(self, id, x, y, w, h):
#         self.id = int(id)
#         self.x = int(x)
#         self.y = int(y)
#         self.w = int(w)
#         self.h = int(h)

# def parseInput(s):
#     p = re.compile(r'#(\d+)\s?@\s?(\d+),(\d+):\s+(\d+)x(\d+)')
#     m = p.match(s)
#     return Claim(m.group(1), m.group(2), m.group(3), m.group(4), m.group(5))

# def createLog(items):
#     log = {}

#     for item in items:
#         claim = parseInput(item)
#         for x in range(claim.x, claim.x + claim.w):
#             for y in range(claim.y, claim.y + claim.h):
#                 p = getPoint(x, y)
#                 claims = []
#                 if p in log:
#                     claims = log[p]
#                     claims.append(claim.id)
#                 else:
#                     claims.append(claim.id)
#                 log[p] = claims

#     return log


# def solvePart1(items):
#     log = createLog(items)
#     overlap = 0
#     for p in log:
#         if len(log[p]) > 1:
#             overlap += 1

#     return overlap

# def solvePart2(items):
#     log = createLog(items)

#     goodList = []
#     badList = []

#     for p in log:
#         claims = log[p]
#         if len(claims) == 1:
#             claim = claims[0]
#             if not claim in badList and not claim in goodList:
#                 goodList.append(claim)
#         else:
#             for claim in claims:
#                 if claim in goodList:
#                     goodList.remove(claim)
#                 if claim not in badList:
#                     badList.append(claim)

#     return goodList

# print ('Part 1: {0}'.format(solvePart1(items)))
# print ('Part 2: {0}'.format(solvePart2(items)))
