from collections import Counter


def main():
    moves = {"^": (0, 1), ">": (1, 0), "v": (0, -1), "<": (-1, 0)}

    input = "^>v<"
    input = open("03.txt").read().strip()

    pos = (0, 0)
    counter = Counter()
    counter.update({pos})
    for i in input:
        move = moves[i]
        pos = tuple(x + y for x, y in zip(pos, move))
        counter.update({pos})

    print(f"Part 1: {len(counter)}")

    pos = [(0, 0), (0, 0)]
    counter = Counter()
    counter.update({pos[0]})
    counter.update({pos[1]})
    for i, m in enumerate(input):
        s = i % 2
        move = moves[m]
        pos[s] = tuple(x + y for x, y in zip(pos[s], move))
        counter.update({pos[s]})

    print(f"Part 2: {len(counter)}")


if __name__ == "__main__":
    main()
