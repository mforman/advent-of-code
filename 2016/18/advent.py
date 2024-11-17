#! /usr/bin/env python
import sys

SAFE = '.'
TRAP = '^'

def room_map(room):
    result = ''
    for y in room:
        result += ''.join(y)
        result += '\n'
    return result


def get_next_row(room):
    num_rows = len(room)
    prev = room[num_rows - 1]
    current = []
    num_cols = len(prev)
    for i in range(num_cols):
        # Traps are ON bits
        # L = 1
        # C = 2
        # R = 4
        # a new tile is a trap only in one of the following situations:
        #   3 - Its left and center tiles are traps, but its right tile is not.
        #   6 - Its center and right tiles are traps, but its left tile is not.
        #   1 - Only its left tile is a trap.
        #   4 - Only its right tile is a trap.

        value = 0

        if i > 0 and prev[i - 1] == TRAP:
            value += 1
        if prev[i] == TRAP:
            value += 2
        if i < (num_cols - 1) and prev[i + 1] == TRAP:
            value += 4

        if value in (0, 2, 5, 7):
            current.append(SAFE)
        else:
            current.append(TRAP)

    room.append(current)


def build_room(first_row, number_of_rows):
    room = [list(first_row)]

    for i in range(1, number_of_rows):
        get_next_row(room)

    return room

def count_safe(room):
    result = 0
    for row in room:
        for tile in row:
            result += tile == SAFE
    return result

def main():
    file_name = 'input.txt'
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print('Will use {} from command-line'.format(file_name))
    else:
        print('Will use default file of {}'.format(file_name))

    with open(file_name, 'r') as input_file:
        instructions = input_file.read().splitlines()

    room = build_room(instructions[0], 400000)

    # print(room_map(room))

    print('Safe tiles: {}'.format(count_safe(room)))


if __name__ == '__main__':
    main()
