#! /usr/bin/env python

import sys
from collections import deque
from itertools import permutations
from math import ceil

def load_file(file_name='input.txt'):
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print('Will use {} from command-line'.format(file_name))
    else:
        print('Will use default file of {}'.format(file_name))

    with open(file_name, 'r') as input_file:
        return input_file.readlines()


def move(d, x, y):
    length = len(d)
    for i in range(length):
        if x < y:
            if i == x:
                val = d.popleft()
                continue

            d.append(d.popleft())

            if i == y:
                d.append(val)
        else:
            i = length - 1 - i
            if i == x:
                val = d.pop()
                continue

            d.appendleft(d.pop())

            if i == y:
                d.appendleft(val)


def reverse(d, x, y):
    for i in range(ceil((y-x)/2)):
        d[i+x], d[y-i] = d[y-i], d[i+x]


def rotate(d, direction, steps):
    if direction == 'left':
        z = -1
    else:
        z = 1
    for i in range(steps):
        d.rotate(z)

def rotate_by_index(d, x):
    for i in range(len(d)):
        if d[i] == x:
            break
    amount = i + 1
    if i >= 4:
        amount += 1
    rotate(d, 'right', amount)

def swap_letter(d, x, y):
    for i in range(len(d)):
        if d[i] == x:
            d[i] = y
        elif d[i] == y:
            d[i] = x

def swap_position(d, x, y):
    d[x], d[y] = d[y], d[x]

def solve(plaintext, instructions, debug=False):
    length = len(plaintext)
    d = deque(list(plaintext))

    for instruction in instructions:
        instruction = instruction.strip()
        if debug:
            print('{}: {} -> '.format(instruction.ljust(38), ''.join(d)), end='')
        seg = instruction.split(' ')

        if seg[0] == 'move':
            move(d, int(seg[2]), int(seg[5]))
        elif seg[0] == 'reverse':
            reverse(d, int(seg[2]), int(seg[4]))
        elif seg[0] == 'rotate' and seg[1] in ('left', 'right'):
            rotate(d, seg[1], int(seg[2]))
        elif seg[0] == 'rotate' and seg[1] == 'based':
            rotate_by_index(d, seg[-1])
        elif seg[0] == 'swap' and seg[1] == 'letter':
            swap_letter(d, seg[2], seg[5])
        elif seg[0] == 'swap' and seg[1] == 'position':
            swap_position(d, int(seg[2]), int(seg[5]))

        if debug:
            print(''.join(d))
    return ''.join(d)

def main():
    instructions = load_file()

    print('Part 1: {}'.format(solve('abcdefgh', instructions)))

    scrambled = 'fbgdceah'
    for s in permutations(scrambled):
        s = ''.join(s)
        print('Part 2: {}\r'.format(s), end='')
        if solve(s, instructions) == scrambled:
            break
    print('\n')

if __name__ == '__main__':
    main()
