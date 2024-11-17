import re

# lines = [
#     'position=< 9,  1> velocity=< 0,  2>',
#     'position=< 7,  0> velocity=<-1,  0>',
#     'position=< 3, -2> velocity=<-1,  1>',
#     'position=< 6, 10> velocity=<-2, -1>',
#     'position=< 2, -4> velocity=< 2,  2>',
#     'position=<-6, 10> velocity=< 2, -2>',
#     'position=< 1,  8> velocity=< 1, -1>',
#     'position=< 1,  7> velocity=< 1,  0>',
#     'position=<-3, 11> velocity=< 1, -2>',
#     'position=< 7,  6> velocity=<-1, -1>',
#     'position=<-2,  3> velocity=< 1,  0>',
#     'position=<-4,  3> velocity=< 2,  0>',
#     'position=<10, -3> velocity=<-1,  1>',
#     'position=< 5, 11> velocity=< 1, -2>',
#     'position=< 4,  7> velocity=< 0, -1>',
#     'position=< 8, -2> velocity=< 0,  1>',
#     'position=<15,  0> velocity=<-2,  0>',
#     'position=< 1,  6> velocity=< 1,  0>',
#     'position=< 8,  9> velocity=< 0, -1>',
#     'position=< 3,  3> velocity=<-1,  1>',
#     'position=< 0,  5> velocity=< 0, -1>',
#     'position=<-2,  2> velocity=< 2,  0>',
#     'position=< 5, -2> velocity=< 1,  2>',
#     'position=< 1,  4> velocity=< 2,  1>',
#     'position=<-2,  7> velocity=< 2, -2>',
#     'position=< 3,  6> velocity=<-1, -1>',
#     'position=< 5,  0> velocity=< 1,  0>',
#     'position=<-6,  0> velocity=< 2,  0>',
#     'position=< 5,  9> velocity=< 1, -2>',
#     'position=<14,  7> velocity=<-2,  0>',
#     'position=<-3,  6> velocity=< 2, -1>'
# ]

with open('10.txt', 'r') as f:
    lines = f.read().splitlines()

points = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]

def getBounds(points, i):
    minx = min(x + i * vx for (x, y, vx, vy) in points)
    maxx = max(x + i * vx for (x, y, vx, vy) in points)
    miny = min(y + i * vy for (x, y, vx, vy) in points)
    maxy = max(y + i * vy for (x, y, vx, vy) in points)

    return (minx, maxx, miny, maxy)

def printGrid(points, i):
    minx, maxx, miny, maxy = getBounds(points, i)
    grid = [['.'] * (maxx + 1) for j in range(maxy + 1)]

    for (x, y, vx, vy) in points:
        _x = x + i * vx
        _y = y + i * vy
        grid[_y][_x] = '#'

    for p in grid:
        print(''.join(p))

smallest = (0, 99999999999)
for i in range(20000):
    # if i % 500 == 0:
    #     print('{}: {}'.format(i, smallest))
    minx, maxx, miny, maxy = getBounds(points, i)
    area = (maxx - minx) * (maxy - miny)
    if area < smallest[1]:
        smallest = (i, area)

printGrid(points, smallest[0])
print(smallest)
