#! /usr/bin/env python

from copy import copy
from itertools import filterfalse, permutations, repeat
import heapq

seed = 1350

def distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def larger(point):
    x = point[0]
    y = point[1]
    if (x > y):
        return x
    return y

def is_wall(point):
    x = point[0]
    y = point[1]
    z = (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
    z += seed
    b = bin(z)
    ones = len([i for i in b if i == '1'])
    return ones % 2 == 1

def is_space(point):
    return not is_wall(point)

def get_symbol(point, moves=None):
    if moves and point in moves:
        return 'O'
    if is_wall(point):
        return '#'
    return '.'


def get_map(width, height, moves=None):
    floor_plan = ''
    cols = ([str(i).rjust(2, ' ') for i in range(width)])
    for i in range(len(str(width))):
        floor_plan += ''.join(repeat(' ', len(str(height)) + 1))
        for j in range(width):
            if i < len(str(width))-1 and cols[j][i+1] != '0':
                floor_plan += ' '
            else:
                floor_plan += cols[j][i]
        floor_plan += '\n'
    for y in range(height):
        floor_plan += str(y).rjust(2, ' ') + ' '
        floor_plan += ''.join([get_symbol((x, y), moves) for x in range(width)])
        floor_plan += '\n'
    return floor_plan


def main():
    initial = (1, 1)
    goal = (31, 39)

    # floor_plan = get_map(max(goal), max(goal), [initial])
    # print(floor_plan)

    queue = []
    heapq.heappush(queue, (0, initial)) # (priority, position)
    graph = {initial: []} # { position: [moves to get here] } len == cost

    directions = [(d * (i%2), d*((i+1)%2)) for d in (-1, 1) for i in (0, 1)]

    while queue:
        _, current = heapq.heappop(queue) # ignore the priority when popping
        if current == goal:
            break

        moves = [(current[0] + d[0], current[1] + d[1]) for d in directions]
        #moves = filterfalse(lambda c: c[0] >= 0 and c[1] >= 0 and is_space(c), moves)

        for move in moves:
            if move[0] < 0 or move[1] < 0 or is_wall(move):
                continue

            path = copy(graph[current])
            path.append(current)
            if move not in graph or len(path) < len(graph[move]):
                graph[move] = path
                priority = distance(move, goal)
                heapq.heappush(queue, (priority, move))

    path = graph[goal]
    print('Found goal in {} moves.'.format(len(path)))
    path.append(goal)

    floor_plan = get_map(larger(goal)+5, larger(goal)+5, graph[goal])
    print(floor_plan)

if __name__ == '__main__':
    main()
