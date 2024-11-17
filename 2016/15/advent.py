#! /usr/bin/env python
import locale
import sys

locale.setlocale(locale.LC_ALL, 'en_US')

def get_position(t, d):
    return (d[2] + t + d[0]) % d[1]

def get_state(t, discs):
    msg = 'State at time {}\n'.format(t)
    for d in discs:
        msg += 'Disc #{} ({}) is at {}\n'.format(str(d[0]).ljust(2, ' '), d[1], get_position(t, d))
    return msg

def main():
    file_name = 'input.txt'
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print('Will use {} from command-line'.format(file_name))
    else:
        print('Will use default file of {}'.format(file_name))

    with open(file_name, 'r') as input_file:
        instructions = input_file.read().splitlines()

    discs = []
    t = 0

    for i in instructions:
        segments = i.split(' ')
        index = int(segments[1][1:])
        positions = int(segments[3])
        start_time = int(segments[6][5:-1])
        intial_position = (int(segments[-1][:-1]) - start_time) % positions

        discs.append((index, positions, intial_position))

    print(get_state(t, discs))

    while True:
        ts = locale.format('%d', t, grouping=True)
        print('Time {}\r'.format(ts), end='')
        valid = True
        for d in discs:
            new_position = get_position(t, d)
            if valid and new_position != 0:
                valid = False

        if valid:
            break

        t += 1

    print(get_state(t, discs))

if __name__ == '__main__':
    main()
