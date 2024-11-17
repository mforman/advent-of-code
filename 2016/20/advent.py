#! /usr/bin/env python
import sys

def test_ip(ip, blacklist):
    for low, high in blacklist:
        if low <= ip <= high:
            break
    else:
        if ip < 2**32:
            return True
    return False

def main():
    file_name = 'sample.txt'
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print('Will use {} from command-line'.format(file_name))
    else:
        print('Will use default file of {}'.format(file_name))

    blacklist = []

    with open(file_name, 'r') as f:
        for l in f.readlines():
            seg = l.split('-')
            blacklist.append((int(seg[0]), int(seg[1].strip())))

    blacklist.sort()

    candidates = [high+1 for _, high in blacklist]
    valids = [c for c in candidates if test_ip(c, blacklist)]

    total = 0
    for ip in valids:
        while test_ip(ip, blacklist):
            total += 1
            ip += 1

    print(valids[0])
    print(total)


if __name__ == '__main__':
    main()
