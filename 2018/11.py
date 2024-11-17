import numpy

serial_number = 3463

def power(x,y): 
    rack_id = (x + 1) + 10
    power = rack_id * (y + 1)
    power += serial_number
    power *= rack_id
    return (power // 100 % 10) - 5

grid = numpy.fromfunction(power, (300,300))

for width in range(3, 300):
    windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
    maximum = int(windows.max())
    location = numpy.where(windows == maximum)
    print(width, maximum, location[0][0] + 1, location[1][0] + 1)


# def build_grid(serial_number):
#     grid = []

#     for j in range(1, 301):
#         row = []
#         for i in range(1, 301):
#             rack_id = i + 10
#             power = rack_id * j
#             power += serial_number
#             power *= rack_id
#             hundreds = power // 100 % 10
#             power = hundreds - 5
#             row.append(power)
#         grid.append(row)
#     return grid

# def find_high(grid):
#     high = (-99999999, 0, 0)
#     for j in range(297):
#         for i in range(297):
#             score = sum(list(itertools.chain(*grid[i:i+3][j:j+3])))
#             if score > high[0]:
#                 high = (score, i+1, j+1)
#     return high

# grid = build_grid(18)
# high_score = find_high(grid)

# print(high_score)


