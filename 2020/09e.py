from itertools import combinations
import time

input = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]

input = list((int(row) for row in open("09.txt")))


def find_invalid_unicorn(items, sample_size):
    pos = sample_size
    item_length = len(items)
    while pos < item_length:
        sums = set([sum(c) for c in combinations(items[pos - sample_size : pos], 2)])
        if items[pos] not in sums:
            return items[pos]
        pos += 1


def find_bob(items, unicorn):
    pos = 0
    item_length = len(items)
    while pos < item_length:
        size = 2
        while pos + size < item_length:
            sample = items[pos : pos + size]
            total = sum(sample)
            if total == unicorn:
                return sample
            if total > unicorn:
                break
            size += 1
        pos += 1


start = time.perf_counter()
unicorn = find_invalid_unicorn(input, 25)
print(f"Part 1: {unicorn}")

bob = find_bob(input, unicorn)
print(f"Part 2: {min(bob) + max(bob)}")
end = time.perf_counter()

print(f"Duration {end - start}")
