from collections import Counter
from itertools import chain


def main():
    input = [
        "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
        "trh fvjkl sbzzf mxmxvkd (contains dairy)",
        "sqjhc fvjkl (contains soy)",
        "sqjhc mxmxvkd sbzzf (contains fish)",
    ]

    input = [row.strip() for row in open("21.txt").readlines()]

    items = []
    for line in input:
        f, a = line.split(" (")
        foods = f.split(" ")
        allergens = a[9:-1].split(", ")
        items.append((foods, allergens))

    # print(items)

    matches = {}
    all_foods = Counter()

    for foods, allergens in items:
        all_foods.update(foods)
        for a in allergens:
            if a not in matches:
                matches[a] = set(foods)
            else:
                matches[a] &= set(foods)

    all_allergens = set()
    for a in matches.values():
        all_allergens.update(a)

    safe = sum([all_foods[f] for f in all_foods if f not in all_allergens])
    print(f"Part 1: {safe} ")

    while True:
        for a, f in ((a, f) for a, f in matches.items() if len(f) == 1):
            for a1, f1 in ((a1, f1) for a1, f1, in matches.items() if a1 != a):
                matches[a1] -= f
        if not any(v for v in matches.values() if len(v) > 1):
            break

    final = ",".join([matches[k].pop() for k in sorted(matches)])
    print(f"Part 2: {final}")


if __name__ == "__main__":
    main()
