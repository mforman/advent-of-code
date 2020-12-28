from itertools import combinations

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

input = [int(row) for row in open("09.txt")]


def find_invalid(items, scan_count):
    for pos, val in enumerate(items):
        if pos < scan_count:
            continue
        sums = set([sum(c) for c in combinations(items[(pos - scan_count) : pos], 2)])
        if val not in sums:
            return val


def find_set(items, value):
    items_len = len(items)
    for pos, _ in enumerate(items):
        for sample_size in range(2, items_len - pos):
            sample = items[pos : pos + sample_size]
            total = sum(sample)
            if total == value:
                return sample
            if total > value:
                break


invalid_item = find_invalid(input, 25)
print(f"Part 1: {invalid_item}")

contig = find_set(input, invalid_item)
result = min(contig) + max(contig)
print(f"Part 2: {result}")
