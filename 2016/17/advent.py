#! /usr/bin/env python
from hashlib import md5
import heapq
import sys

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

possible_moves = {
    0: ('U', UP),
    1: ('D', DOWN),
    2: ('L', LEFT),
    3: ('R', RIGHT)
}

def get_hash(salt, plaintext, stretch = 0):
    b = '{}{}'.format(salt, plaintext).encode()
    h = md5(b).hexdigest()
    for i in range(stretch):
        h = md5(h.encode()).hexdigest()
    return h

def get_open_doors(cipher):
    result = []
    for i in range(4):
        h = cipher[i:i+1]
        d = int(h, 16)
        if d > 10:
            result.append(possible_moves[i])
    return result

def get_moves(p, cipher):
    result = []
    moves = get_open_doors(cipher)

    for move in moves:
        candidate = move_it(p, move[1])
        if not is_wall(candidate):
            result.append((move[0], candidate))
    return result

def is_wall(p):
    for i in range(2):
        if p[i] > 3 or p[i] < 0:
            return True
    return False


def distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def move_it(a, b):
    return (a[0] + b[0], a[1] + b[1])


def find_path(start, goal, salt, shortest=True):
    queue = []
    initial = (start, '') # (position, path_to_here)
    heapq.heappush(queue, (0, initial)) # (priority, position)
    history = {initial: 0}

    while queue:
        _, item = heapq.heappop(queue)
        current, path = item

        if current == goal:
            continue

        cipher = get_hash(salt, path)

        moves = get_moves(current, cipher)
        if len(moves) == 0:
            del history[item] # Dead-end

        for move in moves:
            candidate = move[1]
            new_path = path + move[0]
            priority = distance(candidate, goal)
            next_item = (candidate, new_path)
            history[next_item] = len(new_path)
            heapq.heappush(queue, (priority, next_item))

    result = None
    winner = None

    for key, value in history.items():
        if key[0] != goal:
            continue
        if not winner or ((shortest and value < winner) or (not shortest and value > winner)):
            result = key[1]
            winner = value

    return result

def main():
    salts = {
        'hijkl': None,
        'ihgpwlah': 'DDRRRD',
        'kglvqrro': 'DDUDRLRRUDRD',
        'ulqzkmiv': 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
    }

    check_result = True

    start = (0, 3)
    goal = (3, 0)

    if len(sys.argv) > 1:
        salts = {sys.argv[1]: None}
        check_result = False


    for salt, desired in salts.items():
        path = find_path(start, goal, salt, shortest=False)

        if check_result:
            print('{} : {} : {}'.format(salt, path, path == desired))
        else:
            print('{} : {}'.format(salt, len(path)))

if __name__ == '__main__':
    main()
