#! /usr/bin/env python
from hashlib import md5

def get_hash(salt, index, stretch = 0):
    i = repr(index).encode()
    h = md5(salt + i).hexdigest()
    for i in range(stretch):
        h = md5(h.encode()).hexdigest()
    return h

def n_in_a_row(item: str, n: int, target=None):
    length = len(item)
    if length < n:
        return None

    for i in range(n-1, length):
        segment = item[i-(n-1):i+1]
        if len(set(segment)) == 1:
            if target is None or target == segment[0]:
                return segment[0]

    return None


def main():
    # salt = b'abc'
    salt = b'qzyelonm'
    stretch = 2016
    index = 0
    window = 1000
    hashes = {}
    results = []

    while len(results) < 64:
        if index in hashes:
            current = hashes[index]
        else:
            current = get_hash(salt, index, stretch)
            hashes[index] = current

        triple = n_in_a_row(current, 3)

        if triple:
            for n in range(index + 1, index + window):
                if n in hashes:
                    candidate = hashes[n]
                else:
                    candidate = get_hash(salt, n, stretch)
                    hashes[n] = candidate

                if n_in_a_row(candidate, 5, triple):
                    results.append(current)
                    print('{}: {} index: {}({}) five: {}: {} offset: {}'.format(
                        str(len(results)).rjust(2, ' '),
                        current,
                        str(index).ljust(7, ' '),
                        triple,
                        str(n).ljust(7, ' '),
                        candidate,
                        n - index
                        ))
                    break

        if index - window in hashes:
            del hashes[index - window]

        index += 1

if __name__ == '__main__':
    main()
