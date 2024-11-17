#! /usr/bin/env python
import locale
import sys

locale.setlocale(locale.LC_ALL, 'en_US')

replacements = {
    '0': '1',
    '1': '0'
}

def dragon(a: str):
    b = list(a[::-1])
    for i in range(len(b)):
        if b[i] in replacements:
            b[i] = replacements[b[i]]

    return '{}0{}'.format(a, ''.join(b))

def checksum(a: str):
    temp = []
    val = list(a)
    for i in range(0, len(a), 2):
        if a[i] == a[i + 1]:
            temp.append('1')
        else:
            temp.append('0')

    result = ''.join(temp)

    if len(result) % 2 == 1:
        return result
    else:
        return checksum(result)


def main():
    seed = '10000'
    desired = 20

    if len(sys.argv) > 1:
        seed = sys.argv[1]

    if len(sys.argv) > 2:
        desired = int(sys.argv[2])

    print('Seed Value: {}\nDesired Length: {}\n'.format(seed, desired))

    data = seed

    while len(data) < desired:
        data = dragon(data)

    if len(data) > desired:
        data = data[:desired]

    chksm = checksum(data)

    print(chksm)

if __name__ == '__main__':
    main()
